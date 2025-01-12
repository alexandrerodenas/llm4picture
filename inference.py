from abc import ABC, abstractmethod
import random

import ollama
from ollama import ChatResponse
import json

from inference_result import ImageClassification, InferenceResult


class Inference(ABC):
    @abstractmethod
    def infer(self, image_path: str) -> ImageClassification:
        pass

class OllamaInference(Inference):
    def __init__(self, model: str, prompt: str):
        self.model = model
        self.prompt = prompt

    def infer(self, image_path: str) -> ImageClassification:
        res: ChatResponse = ollama.chat(
            model=self.model,
            messages=[
                {
                    'role': 'user',
                    'content': self.prompt,
                    'images': [image_path]
                }
            ],
            format=InferenceResult.model_json_schema(),
        )
        print(res.message.content)
        return InferenceResult(**json.loads(res.message.content)).classification

class MockedInference(Inference):
    def infer(self, image_path: str) -> ImageClassification:
        return random.choice([ImageClassification.VALID, ImageClassification.INVALID, ImageClassification.UNKNOWN])