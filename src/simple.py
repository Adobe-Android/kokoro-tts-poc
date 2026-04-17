import os
import sys

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
client = InferenceClient(
    model="hexgrad/Kokoro-82M",
    token=hf_token
)

voice="af_bella" # defaults to af_bella if voice is not specified in the extra_body.

def query(text):
    # print(f"DEBUG: Generating audio for: '{text}'")
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

    audio = query(text)

    if audio:
        # Save the audio to a file for verification
        output_file = f"simple_{voice}_output.wav"
        with open(output_file, "wb") as f:
            f.write(audio)
        print(f"DEBUG: Audio saved to {output_file}")

if __name__ == "__main__":
    main()
