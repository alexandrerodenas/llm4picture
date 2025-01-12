from abc import ABC, abstractmethod
import random

import ollama

from inference_result import InferenceResult


class Inference(ABC):
    @abstractmethod
    def infer(self, image_path: str) -> str:
        pass

class OllamaInference(Inference):
    def __init__(self, model: str, prompt: str):
        self.model = model
        self.prompt = prompt

    def infer(self, image_path: str) -> str:
        res = ollama.chat(
            model=self.model,
            messages=[
                {
                    'role': 'user',
                    'content': self.prompt,
                    'images': [image_path]
                }
            ]
        )
        return InferenceResult.from_value(res['message']['content'])


class MockedInference(Inference):
    def infer(self, image_path: str) -> str:
        return random.choice(["VALID", "INVALID", "UNKNOWN"])