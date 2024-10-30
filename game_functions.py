from helpers import get_completion, TTI_ENDPOINT, ITT_ENDPOINT, image_to_base64_str, base64_to_pil

# Caption an image using ITT_ENDPOINT
def captioner(image):
    base64_image = image_to_base64_str(image)
    result = get_completion(base64_image, None, ITT_ENDPOINT)
    return result[0]['generated_text']

# Generate an image from text prompt using TTI_ENDPOINT
def generate(prompt):
    output = get_completion(prompt, None, TTI_ENDPOINT)
    return base64_to_pil(output)
