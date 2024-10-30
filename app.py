import gradio as gr
from game_functions import captioner, generate

# Define a function that captions the image
def caption_image(image):
    return captioner(image)

# Define a function that generates an image from a prompt
def generate_image(caption):
    return generate(caption)

# Define a function that combines captioning and generation in a single step
def caption_and_generate(image):
    caption = captioner(image)
    generated_image = generate(caption)
    return [caption, generated_image]

# Define a function for looping the game (repeated caption-generation)
def loop_game(image, iterations):
    captions_images = []
    current_image = image
    for _ in range(iterations):
        caption = captioner(current_image)
        generated_image = generate(caption)
        captions_images.append((caption, generated_image))
        current_image = generated_image  # Use generated image as input for next iteration
    return captions_images

# Build Gradio Interface
with gr.Blocks() as demo:
    gr.Markdown("# Describe-and-Generate Game")

    # Upload Section
    image_upload = gr.Image(label="Upload an Image", type="pil")
    
    # Separate Caption Generation
    btn_caption = gr.Button("Generate Caption")
    caption_output = gr.Textbox(label="Generated Caption")

    # Separate Image Generation
    btn_generate = gr.Button("Generate Image from Caption")
    image_output = gr.Image(label="Generated Image")

    # Single-Step Caption and Generate
    btn_caption_and_generate = gr.Button("Caption and Generate (One Click)")
    caption_output_all_in_one = gr.Textbox(label="Generated Caption (Single Step)")
    image_output_all_in_one = gr.Image(label="Generated Image (Single Step)")

    # Loop Section
    loop_iterations = gr.Slider(minimum=1, maximum=5, step=1, label="Number of Loop Iterations")
    btn_loop = gr.Button("Run Loop")
    loop_output = gr.Gallery(label="Looped Images (Caption + Generated Image)")

    # Button Actions
    btn_caption.click(fn=caption_image, inputs=[image_upload], outputs=[caption_output])
    btn_generate.click(fn=generate_image, inputs=[caption_output], outputs=[image_output])
    btn_caption_and_generate.click(fn=caption_and_generate, inputs=[image_upload], outputs=[caption_output_all_in_one, image_output_all_in_one])
    btn_loop.click(fn=loop_game, inputs=[image_upload, loop_iterations], outputs=[loop_output])

# Launch app
demo.launch()
