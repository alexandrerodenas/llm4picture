from enum import Enum

from pydantic import BaseModel

class ImageClassification(Enum):
    VALID = "VALID"
    INVALID = "INVALID"
    UNKNOWN = "UNKNOWN"

    def get_target_folder(self, config) -> str:
        if self == ImageClassification.VALID:
            return config.valid_output_folder
        elif self == ImageClassification.INVALID:
            return config.invalid_output_folder
        else:
            return config.unknowns_output_folder

class InferenceResult(BaseModel):
    classification: ImageClassification
    explanation: str
