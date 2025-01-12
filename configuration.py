import os
import yaml

class Config:
    def __init__(self, config_file):
        with open(config_file, 'r') as file:
            config = yaml.safe_load(file)

        self.image_folder = config['image_folder']
        self.unknowns_output_folder = config['unknowns_output_folder']
        self.valid_output_folder = config['valid_output_folder']
        self.invalid_output_folder = config['invalid_output_folder']
        self.prompt = config['prompt']
        self._create_directories()

    def _create_directories(self):
        os.makedirs(self.image_folder, exist_ok=True)
        os.makedirs(self.unknowns_output_folder, exist_ok=True)
        os.makedirs(self.valid_output_folder, exist_ok=True)
        os.makedirs(self.invalid_output_folder, exist_ok=True)