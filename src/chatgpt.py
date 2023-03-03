from src.models import ModelInterface
from src.memory import MemoryInterface


class ChatGPT:
    def __init__(self, model: ModelInterface, memory: MemoryInterface = None):
        self.model = model
        self.memory = memory

    def get_response(self, user_id: str, text: str) -> str:
        prompt = {"role": "user", "content": text}
        prev = [] if self.memory is None else self.memory.get(user_id)
        messages = [*prev, prompt]
        response = self.model.chat_completion(messages)
        if self.memory is not None:
            self.memory.append(user_id, prompt)
            self.memory.append(user_id, {"role": "assistant", "content": response})
        return response

    def clean_history(self, user_id: str) -> None:
        self.memory.remove(user_id)


class DALLE:
    def __init__(self, model: ModelInterface):
        self.model = model

    def generate(self, text: str) -> str:
        return self.model.image_generation(text)
