import os
import shutil
import ollama
from configuration import Config

def move_image_to_folder(image_path, target_folder):
    target_path = os.path.join(target_folder, os.path.basename(image_path))
    shutil.move(image_path, target_path)

def analyse(config: Config):
    for image_name in os.listdir(config.image_folder):
        image_path = os.path.join(config.image_folder, image_name)

        if image_path.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            res = ollama.chat(
                model="llava:7b",
                messages=[
                    {
                        'role': 'user',
                        'content': config.prompt,
                        'images': [image_path]
                    }
                ]
            )

            respond = sanitize_respond(res['message']['content'])
            print(f"{image_name}: {respond}")

            if respond == "VALID":
                target_folder = config.valid_output_folder
            elif respond == "INVALID":
                target_folder = config.invalid_output_folder
            else:
                target_folder = config.unknowns_output_folder

            move_image_to_folder(image_path, target_folder)

def sanitize_respond(respond: str):
    if "INVALID" in respond:
        return "INVALID"
    if "UNKNOWN" in respond:
        return "UNKNOWN"
    if "VALID" in respond:
        return "VALID"
    return "UNKNOWN"

if __name__ == '__main__':
    config = Config('config.yaml')
    analyse(config)