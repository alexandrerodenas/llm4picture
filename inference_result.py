from enum import Enum

class InferenceResult(Enum):
    VALID = "VALID"
    INVALID = "INVALID"
    UNKNOWN = "UNKNOWN"

    @staticmethod
    def from_value(value: str):
        if "INVALID" in value:
            return "INVALID"
        if "UNKNOWN" in value:
            return "UNKNOWN"
        if "VALID" in value:
            return "VALID"
        return "UNKNOWN"