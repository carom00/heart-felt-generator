# heart-felt-generator
Generate an image and poem using VQGAN-CLIP, GPT-3 and deep style transfer.

### TODO:
- Read prompts from txt file
- Summarize input before generating CLIP to distill

## How To Install
Install the requirements - pip install -r requirements.txt

For the image generator, run the image_generator_init.py script, it will download all the needed files.

If you want to install it without the script, make sure to install all the python requirements,
download the prefered models for the generator, install exempi (sudo apt install exempi), create a folder called
steps (mkdir steps) and clone CLIP (https://github.com/openai/CLIP) Taming Transformers (https://github.com/CompVis/taming-transformers)
in the same folder with the scripts.

Finally you rename .env.default to .env and add the needed values


## How To Run
Edit the start.txt with the text you want and file name to be saved and run python start.py (based on the python installation
python can be python3 or py)
