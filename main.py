import os
import shutil
from configuration import Config
from inference import OllamaInference, MockedInference
from inference_result import ImageClassification


def move_image_to_folder(image_path: str, target_folder: str):
    target_path = os.path.join(target_folder, os.path.basename(image_path))
    shutil.move(image_path, target_path)

def analyse(config: Config):
    inference = OllamaInference(model=config.model, prompt=config.prompt)
    # inference = MockedInference()
    for image_name in os.listdir(config.image_folder):
        image_path = os.path.join(config.image_folder, image_name)

        if image_path.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            respond: ImageClassification = inference.infer(image_path)
            print(f"{image_name}: {respond}")

            move_image_to_folder(image_path, respond.get_target_folder(config))



if __name__ == '__main__':
    config = Config('config.yaml')
    analyse(config)