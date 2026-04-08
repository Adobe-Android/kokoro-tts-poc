import os
import sys
import tempfile
import wave
import textwrap

from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()  # reads variables from a .env file and sets them in os.environ

print(f"DEBUG: Current Python executable: {sys.executable}")
hf_token = os.environ.get('HF_TOKEN')
print(f"DEBUG: HF_TOKEN exists in environ: {hf_token is not None}")

if not hf_token:
    print("ERROR: HF_TOKEN not found in environment variables.")
    sys.exit(1)

# Initialize the Inference Client for the Kokoro-82M model
# We specify provider="replicate" to ensure it routes correctly
client = InferenceClient(
    model="hexgrad/Kokoro-82M",
    token=hf_token,
    provider="replicate"
)

voice="af_bella" # defaults to af_bella if voice is not specified in the extra_body.

def query(text):
    print(f"DEBUG: Generating audio for chunk ({len(text)} chars)...")
    try:
        # text_to_speech returns the audio bytes directly
        audio = client.text_to_speech(text, extra_body={"voice": voice})
        print(f"DEBUG: Successfully received {len(audio)} bytes of audio.")
        return audio
    except Exception as e:
        print(f"DEBUG: Exception type: {type(e)}")
        print(f"DEBUG: Error during inference: {e}")
        if hasattr(e, 'response'):
            print(f"DEBUG: HTTP Status Code: {e.response.status_code}")
            print(f"DEBUG: HTTP Response content: {e.response.content}")
        return None

def main():
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    else:
        input_file = "input.txt"

    try:
        with open(input_file, "r", encoding="utf-8") as f:
            text = f.read().strip()
    except FileNotFoundError:
        print(f"ERROR: Input file '{input_file}' not found.")
        sys.exit(1)

    # Split text into chunks to avoid the 60-second timeout
    # We'll split by newline, then further split if too long.
    raw_chunks = text.split('\n')
    chunks = []
    for c in raw_chunks:
        c = c.strip()
        if not c: continue
        if len(c) > 500:
            # Split large chunks further
            sub_chunks = textwrap.wrap(c, width=500, break_long_words=False)
            chunks.extend(sub_chunks)
        else:
            chunks.append(c)

    print(f"DEBUG: Split text into {len(chunks)} chunks.")

    # We will collect temporary paths for all successful chunks to combine them later
    temp_files = []

    for i, chunk in enumerate(chunks):
        print(f"--- Processing chunk {i+1}/{len(chunks)} ---")
        audio_bytes = query(chunk)
        if audio_bytes:
            # Write bytes to a temporary file
            fd, temp_path = tempfile.mkstemp(suffix=".wav")
            with os.fdopen(fd, 'wb') as f:
                f.write(audio_bytes)
            temp_files.append(temp_path)
        else:
            print(f"WARNING: Failed to generate audio for chunk {i+1}. Skipping.")

    if temp_files:
        output_file = f"advanced_{voice}_output.wav"
        
        # Read the first file to get the wave parameters (channels, sample width, framerate, etc.)
        with wave.open(temp_files[0], 'rb') as w_in:
            params = w_in.getparams()
        
        # Open the output file and write all frames
        with wave.open(output_file, 'wb') as w_out:
            w_out.setparams(params)
            for temp_path in temp_files:
                with wave.open(temp_path, 'rb') as w_in:
                    w_out.writeframes(w_in.readframes(w_in.getnframes()))
                # Clean up the temporary file
                os.remove(temp_path)
                
        print(f"DEBUG: Finished! Combined audio saved to {output_file}")
    else:
        print("ERROR: No audio was generated.")

if __name__ == "__main__":
    main()
