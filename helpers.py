import os
import io
import requests
import json
import base64
from PIL import Image
from dotenv import load_dotenv, find_dotenv

# Load environment variables
_ = load_dotenv(find_dotenv())
hf_api_key = os.environ['HF_API_KEY']
TTI_ENDPOINT = os.environ['HF_API_TTI_BASE']
ITT_ENDPOINT = os.environ['HF_API_ITT_BASE']

# Convert PIL image to base64
def image_to_base64_str(pil_image):
    byte_arr = io.BytesIO()
    pil_image.save(byte_arr, format='PNG')
    byte_arr = byte_arr.getvalue()
    return base64.b64encode(byte_arr).decode('utf-8')

# Convert base64 to PIL image
def base64_to_pil(img_base64):
    base64_decoded = base64.b64decode(img_base64)
    byte_stream = io.BytesIO(base64_decoded)
    return Image.open(byte_stream)

# Function to interact with Hugging Face APIs
def get_completion(inputs, parameters=None, ENDPOINT_URL=""):
    headers = {
        "Authorization": f"Bearer {hf_api_key}",
        "Content-Type": "application/json"
    }
    data = {"inputs": inputs}
    if parameters:
        data.update({"parameters": parameters})
    response = requests.post(ENDPOINT_URL, headers=headers, data=json.dumps(data))
    return json.loads(response.content.decode("utf-8"))
