# [Presentation Slides](https://docs.google.com/presentation/d/1CF6ahEiaTC_Cksk7uV8EE14BOjT7soY3wsrWhVp5vzk/edit#slide=id.g2fc51b79cda_2_144) | Describe and Generate Game

This project is a game application that uses Gradio to combine text-to-image and image-to-text capabilities through Hugging Face APIs. Users upload an image, and the app generates a caption for the image, then creates a new image based on the caption, creating a fun "telephone game" between captions and generated images.

## Features
- **Image Captioning**: Generate a caption for an uploaded image.
- **Image Generation**: Use the generated caption to create a new image.
- **Streamlined Workflow**: One-click button to generate a caption and a new image, simplifying the game loop.

## Requirements
Install the required libraries with:

```bash
pip install -r requirements.txt
```

## Setup
1. **Clone the Repository**:

    ```bash
    git clone https://github.com/KM-Zubair/GenAI-Game-on-Gradio
    cd describe-and-generate-game
    ```

2. **Set up Environment Variables**: Create a `.env` file in the root directory with your Hugging Face API key and endpoints:

    ```plaintext
    HF_API_KEY=your_huggingface_api_key_here
    HF_API_TTI_BASE=your_text_to_image_endpoint
    HF_API_ITT_BASE=your_image_to_text_endpoint
    ```

3. **Run the App**: Start the Gradio interface by running `app.py`.

    ```bash
    python app.py
    ```

4. **Access the Game**: Open the link provided by Gradio to interact with the game in your browser.

## File Structure
- **helpers.py**: Contains helper functions for API calls and image processing.
- **game_functions.py**: Defines the core functions for image captioning and generation.
- **app.py**: Builds the Gradio interface for the Describe-and-Generate Game.

--- 
