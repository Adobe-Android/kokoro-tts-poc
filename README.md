# tts-poc

A proof-of-concept text-to-speech project using...

![Hugging Face](https://huggingface.co/front/assets/huggingface_logo-noborder.svg)

* [Hugging Face](https://hf.co/)
* [hexgrad/Kokoro-82M](https://huggingface.co/hexgrad/Kokoro-82M) model for TTS (text-to-speech)
* [fal](https://fal.ai/models/fal-ai/kokoro/american-english/playground) for inference.

## Compatibility

Works with Linux, macOS, and Windows. Requires Python 3.12 or later.

Tested with Python 3.12, 3.13, and 3.14.

## Usage

### Clone the repo

```shell
git clone https://github.com/Adobe-Android/tts-poc.git
```

### Prepare the virtual environment

#### Recommended

Use the Python 3.5+ [venv](https://docs.python.org/3/library/venv.html).

Nothing to install. You can skip to the next [section](#go-to-the-project-directory).

#### Optional

Use [virtualenv](https://pypi.org/project/virtualenv/).

Install [virtualenv](https://pypi.org/project/virtualenv/) if it is not already installed.

```powershell
python -m pipx install virtualenv
```

If you do not have pipx installed, either install it with pip (command below) or first [install pipx](#troubleshooting-install-pipx).

```powershell
python -m pip install --user virtualenv
```

#### Go to the project directory

```shell
cd tts-poc
```

#### Create the virtual environment inside of our newly cloned directory

```powershell
python -m venv venv
```

or

```powershell
virtualenv venv
```

#### Activate the virtual environment using the appropriate files for our environment. I'll include commands for the most common scenarios below. More information can be found in the [virtualenv documentation](https://virtualenv.pypa.io/en/latest/how-to/usage.html#activate-a-virtual-environment)

Bash (macOS, Linux, or other Unix)

```shell
source venv/bin/activate
```

PowerShell (Windows)

```powershell
.\venv\Scripts\Activate.ps1
```

Command Prompt (Windows)

```batchfile
.\venv\Scripts\activate.bat
```

### Install the necessary packages

```powershell
python -m pip install -r requirements.txt
```

### Run (Simple)

```powershell
.venv/Scripts/python ./src/simple.py
```

### Sample (Simple)

Voice: af_bella

🎵 [Click here to listen to the audio sample](https://retroware.nyc3.cdn.digitaloceanspaces.com/tts-poc/samples/simple_af_bella_output.wav)

### Run (Advanced)

```powershell
.venv/Scripts/python ./src/advanced.py bee.txt
```

### Sample (Advanced)

Voice: af_bella

🎵 [Click here to listen to the audio sample](https://retroware.nyc3.cdn.digitaloceanspaces.com/tts-poc/samples/advanced_af_bella_output.wav)

### Other Samples

Voice: af_alloy

🎵 [Click here to listen to the audio sample](https://retroware.nyc3.cdn.digitaloceanspaces.com/tts-poc/samples/simple_af_alloy_output.wav)

Voice: af_aoede

🎵 [Click here to listen to the audio sample](https://retroware.nyc3.cdn.digitaloceanspaces.com/tts-poc/samples/simple_af_aoede_output.wav)

Voice: af_jessica

🎵 [Click here to listen to the audio sample](https://retroware.nyc3.cdn.digitaloceanspaces.com/tts-poc/samples/simple_af_jessica_output.wav)

Voice: af_kore

🎵 [Click here to listen to the audio sample](https://retroware.nyc3.cdn.digitaloceanspaces.com/tts-poc/samples/simple_af_kore_output.wav)

Voice: af_nicole

🎵 [Click here to listen to the audio sample](https://retroware.nyc3.cdn.digitaloceanspaces.com/tts-poc/samples/simple_af_nicole_output.wav)

Voice: af_nova

🎵 [Click here to listen to the audio sample](https://retroware.nyc3.cdn.digitaloceanspaces.com/tts-poc/samples/simple_af_nova_output.wav)

Voice: af_river

🎵 [Click here to listen to the audio sample](https://retroware.nyc3.cdn.digitaloceanspaces.com/tts-poc/samples/simple_af_river_output.wav)

Voice: af_sarah

🎵 [Click here to listen to the audio sample](https://retroware.nyc3.cdn.digitaloceanspaces.com/tts-poc/samples/simple_af_sarah_output.wav)

Voice: af_sky

🎵 [Click here to listen to the audio sample](https://retroware.nyc3.cdn.digitaloceanspaces.com/tts-poc/samples/simple_af_sky_output.wav)

Voice: am_adam

🎵 [Click here to listen to the audio sample](https://retroware.nyc3.cdn.digitaloceanspaces.com/tts-poc/samples/simple_am_adam_output.wav)

Voice: am_echo

🎵 [Click here to listen to the audio sample](https://retroware.nyc3.cdn.digitaloceanspaces.com/tts-poc/samples/simple_am_echo_output.wav)

Voice: am_eric

🎵 [Click here to listen to the audio sample](https://retroware.nyc3.cdn.digitaloceanspaces.com/tts-poc/samples/simple_am_eric_output.wav)

Voice: am_fenrir

🎵 [Click here to listen to the audio sample](https://retroware.nyc3.cdn.digitaloceanspaces.com/tts-poc/samples/simple_am_fenrir_output.wav)

Voice: am_liam

🎵 [Click here to listen to the audio sample](https://retroware.nyc3.cdn.digitaloceanspaces.com/tts-poc/samples/simple_am_liam_output.wav)

Voice: am_michael

🎵 [Click here to listen to the audio sample](https://retroware.nyc3.cdn.digitaloceanspaces.com/tts-poc/samples/simple_am_michael_output.wav)

Voice: am_onyx

🎵 [Click here to listen to the audio sample](https://retroware.nyc3.cdn.digitaloceanspaces.com/tts-poc/samples/simple_am_onyx_output.wav)

Voice: am_puck

🎵 [Click here to listen to the audio sample](https://retroware.nyc3.cdn.digitaloceanspaces.com/tts-poc/samples/simple_am_puck_output.wav)

## Libraries

### Top-level Project Dependencies

[python-dotenv](https://pypi.org/project/python-dotenv/) - Required for securely specifying the HF_TOKEN.

```powershell
python -m pip install python-dotenv
```

No transitive packages are installed by python-dotenv.

[huggingface-hub](https://pypi.org/project/huggingface-hub/) - Required for routing inference through Hugging Face.

```powershell
python -m pip install huggingface-hub
```

For transitive packages, see associated table [below](#transitive-packages-installed-by-huggingface-hub).

[jupyter](https://pypi.org/project/jupyter/) - Required for the [Jupyter Notebook](/src/demo.ipynb). This is optional.

```powershell
python -m pip install jupyter
```

For transitive packages, see associated table [below](#transitive-packages-installed-by-jupyter).

### Transitive Packages Installed by huggingface-hub

| Package | Version |
| ------- | ------- |
| annotated-doc | 0.0.4 |
| anyio | 4.13.0 |
| certifi | 2026.2.25 |
| click | 8.3.2 |
| colorama | 0.4.6 |
| filelock | 3.25.2 |
| fsspec | 2026.3.0 |
| h11 | 0.16.0 |
| hf-xet | 1.4.3 |
| httpcore | 1.0.9 |
| httpx | 0.28.1 |
| huggingface_hub | 1.9.1 |
| idna | 3.11 |
| markdown-it-py | 4.0.0 |
| mdurl | 0.1.2 |
| packaging | 26.0 |
| Pygments | 2.20.0 |
| PyYAML | 6.0.3 |
| rich | 14.3.3 |
| shellingham | 1.5.4 |
| tqdm | 4.67.3 |
| typer | 0.24.1 |
| typing_extensions | 4.15.0 |

### Transitive Packages Installed by jupyter

| Package | Version |
| ------- | ------- |
| anyio | 4.13.0 |
| argon2-cffi | 25.1.0 |
| argon2-cffi-bindings | 25.1.0 |
| arrow | 1.4.0 |
| asttokens | 3.0.1 |
| async-lru | 2.3.0 |
| attrs | 26.1.0 |
| babel | 2.18.0 |
| beautifulsoup4 | 4.14.3 |
| bleach | 6.3.0 |
| certifi | 2026.2.25 |
| cffi | 2.0.0 |
| charset-normalizer | 3.4.7 |
| colorama | 0.4.6 |
| comm | 0.2.3 |
| debugpy | 1.8.20 |
| decorator | 5.2.1 |
| defusedxml | 0.7.1 |
| executing | 2.2.1 |
| fastjsonschema | 2.21.2 |
| fqdn | 1.5.1 |
| h11 | 0.16.0 |
| httpcore | 1.0.9 |
| httpx | 0.28.1 |
| idna | 3.11 |
| ipykernel | 7.2.0 |
| ipython | 9.12.0 |
| ipython_pygments_lexers | 1.1.1 |
| ipywidgets | 8.1.8 |
| isoduration | 20.11.0 |
| jedi | 0.19.2 |
| Jinja2 | 3.1.6 |
| json5 | 0.14.0 |
| jsonpointer | 3.1.1 |
| jsonschema | 4.26.0 |
| jsonschema-specifications | 2025.9.1 |
| jupyter | 1.1.1 |
| jupyter_client | 8.8.0 |
| jupyter-console | 6.6.3 |
| jupyter_core | 5.9.1 |
| jupyter-events | 0.12.0 |
| jupyter-lsp | 2.3.1 |
| jupyter_server | 2.17.0 |
| jupyter_server_terminals | 0.5.4 |
| jupyterlab | 4.5.6 |
| jupyterlab_pygments | 0.3.0 |
| jupyterlab_server | 2.28.0 |
| jupyterlab_widgets | 3.0.16 |
| lark | 1.3.1 |
| MarkupSafe | 3.0.3 |
| matplotlib-inline | 0.2.1 |
| mistune | 3.2.0 |
| nbclient | 0.10.4 |
| nbconvert | 7.17.0 |
| nbformat | 5.10.4 |
| nest-asyncio | 1.6.0 |
| notebook | 7.5.5 |
| notebook_shim | 0.2.4 |
| packaging | 26.0 |
| pandocfilters | 1.5.1 |
| parso | 0.8.6 |
| pip | 26.0.1 |
| platformdirs | 4.9.4 |
| prometheus_client | 0.24.1 |
| prompt_toolkit | 3.0.52 |
| psutil | 7.2.2 |
| pure_eval | 0.2.3 |
| pycparser | 3.0 |
| Pygments | 2.20.0 |
| python-dateutil | 2.9.0.post0 |
| python-json-logger | 4.1.0 |
| pywinpty | 3.0.3 |
| PyYAML | 6.0.3 |
| pyzmq | 27.1.0 |
| referencing | 0.37.0 |
| requests | 2.33.1 |
| rfc3339-validator | 0.1.4 |
| rfc3986-validator | 0.1.1 |
| rfc3987-syntax | 1.1.0 |
| rpds-py | 0.30.0 |
| Send2Trash | 2.1.0 |
| setuptools | 82.0.1 |
| six | 1.17.0 |
| soupsieve | 2.8.3 |
| stack-data | 0.6.3 |
| terminado | 0.18.1 |
| tinycss2 | 1.4.0 |
| tornado | 6.5.5 |
| traitlets | 5.14.3 |
| typing_extensions | 4.15.0 |
| tzdata | 2026.1 |
| uri-template | 1.3.0 |
| urllib3 | 2.6.3 |
| wcwidth | 0.6.0 |
| webcolors | 25.10.0 |
| webencodings | 0.5.1 |
| websocket-client | 1.9.0 |
| widgetsnbextension | 4.0.15 |

### Additional Notes

The program expects to read from a text file in the project root directory. The expected name is input.txt. You can also pass any text file name as an argument to the program.

## References

* <https://realpython.com/python-virtual-environments-a-primer/>

* <https://learnpython.com/blog/how-to-use-virtualenv-python/>

* <https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/>

## Troubleshooting (Running in VS Code)

If you see errors like 'No module named...'

![Issue](/screenshots/python-venv-issue.png)

Make sure you select the Python interpreter in your virtual environment.

![Hugging Face](/screenshots/run-python-venv.png)

## Troubleshooting (Install pipx)

```powershell
python -m pip install --user -U pipx
python -m pipx ensurepath
```

## Troubleshooting (Windows)

If you are having trouble on Windows specifically, I'd suggest you clean out the following directories. I've found these issues to be common when you've maintained a Windows install long enough to have downloaded at least a few Python versions over time, even if you only have the latest installed now.

```powershell
C:\Users\tngam\.local - delete bin and pipx folders
C:\Users\tngam\AppData\Roaming\Python - delete all folders
```

If you are on macOS or Linux, you probably aren't having these sorts of problems, but feel free to open an issue.
