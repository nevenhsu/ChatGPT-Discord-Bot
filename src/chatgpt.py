from src.models import ModelInterface
from src.memory import MemoryInterface


class ChatGPT:
    def __init__(self, model: ModelInterface, memory: MemoryInterface):
        self.model = model
        self.memory = memory

    def get_response(self, id: str, text: str) -> str:
        self.memory.append(id, {'role': 'user', 'content': text})
        response = self.model.chat_completion(self.memory.get(id))
        role = response['choices'][0]['message']['role']
        content = response['choices'][0]['message']['content']
        self.memory.append(id, {'role': role, 'content': content})
        return content

    def clean_history(self, user_id: str, prompt: str) -> None:
        self.memory.reset(user_id, prompt)


class DALLE:
    def __init__(self, model: ModelInterface):
        self.model = model

    def generate(self, text: str) -> str:
        return self.model.image_generation(text)
