from enum import Enum

class InferenceResult(Enum):
    VALID = "VALID"
    INVALID = "INVALID"
    UNKNOWN = "UNKNOWN"

    @staticmethod
    def from_value(value: str):
        if "INVALID" in value:
            return InferenceResult.INVALID
        if "VALID" in value:
            return InferenceResult.VALID
        return InferenceResult.UNKNOWN

    def get_target_folder(self, config) -> str:
        if self == InferenceResult.VALID:
            return config.valid_output_folder
        elif self == InferenceResult.INVALID:
            return config.invalid_output_folder
        else:
            return config.unknowns_output_folder