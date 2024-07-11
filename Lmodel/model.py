
# model.py
import os
import google.generativeai as genai
from PIL import Image

def process_image(api_key, model_name, images_folder):
    # Configure Google Generative AI
    genai.configure(api_key=api_key)

    # Initialize the multimodal model
    multimodal_model = genai.GenerativeModel(model_name)

    # Get a list of files in the folder
    files = os.listdir(images_folder)

    # Sort files in reverse order
    files.sort(reverse=True)

    # Find the last image file
    image_file = None
    for file in files:
        if file.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_file = os.path.join(images_folder, file)
            break

    if image_file:
        # Open the last image file found
        img = Image.open(image_file)

        # Define prompt
        prompt = 'Describe this image in few words.'

        # Generate content
        contents = [img, prompt]
        responses = multimodal_model.generate_content(contents, stream=False)

        # Prepare and return responses
        response_texts = [response.text for response in responses]
        return response_texts
    else:
        return ["No image files found in the speciffied folder."]

# print(process_image('AIzaSyBi_SLAuZ2jh9nDMLavLU12GwnRoZaczhY', 'gemini-pro-vision', r'C:\Users\Sridhar\.cache\image_captioner\files'))
