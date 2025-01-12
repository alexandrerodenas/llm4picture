from enum import Enum

class InferenceResult(Enum):
    VALID = "VALID"
    INVALID = "INVALID"
    UNKNOWN = "UNKNOWN"

    @staticmethod
    def from_value(value: str):
        if "invalid" in value.lower():
            return InferenceResult.INVALID
        if "valid" in value.lower():
            return InferenceResult.VALID
        print("Unknown value: ", value)
        return InferenceResult.UNKNOWN

    def get_target_folder(self, config) -> str:
        if self == InferenceResult.VALID:
            return config.valid_output_folder
        elif self == InferenceResult.INVALID:
            return config.invalid_output_folder
        else:
            return config.unknowns_output_folder