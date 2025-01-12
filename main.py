import os
import shutil
import ollama
from configuration import Config
from inference import OllamaInference, MockedInference


def move_image_to_folder(image_path, target_folder):
    target_path = os.path.join(target_folder, os.path.basename(image_path))
    shutil.move(image_path, target_path)

def analyse(config: Config):
    inference = OllamaInference(model=config.model, prompt=config.prompt)
    # inference = MockedInference()
    for image_name in os.listdir(config.image_folder):
        image_path = os.path.join(config.image_folder, image_name)

        if image_path.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            respond = inference.infer(image_path)
            print(f"{image_name}: {respond}")

            if respond == "VALID":
                target_folder = config.valid_output_folder
            elif respond == "INVALID":
                target_folder = config.invalid_output_folder
            else:
                target_folder = config.unknowns_output_folder

            move_image_to_folder(image_path, target_folder)



if __name__ == '__main__':
    config = Config('config.yaml')
    analyse(config)