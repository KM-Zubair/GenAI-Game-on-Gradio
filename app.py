import gradio as gr
from game_functions import captioner, generate

# Define a function that combines captioning and generation
def caption_and_generate(image):
    caption = captioner(image)
    generated_image = generate(caption)
    return [caption, generated_image]

# Build Gradio Interface
with gr.Blocks() as demo:
    gr.Markdown("# Describe-and-Generate Game")
    image_upload = gr.Image(label="Upload an image", type="pil")
    caption = gr.Textbox(label="Generated Caption")
    image_output = gr.Image(label="Generated Image")
    btn_caption_and_generate = gr.Button("Caption and Generate")

    # Button action
    btn_caption_and_generate.click(fn=caption_and_generate, inputs=[image_upload], outputs=[caption, image_output])

# Launch app
demo.launch()

