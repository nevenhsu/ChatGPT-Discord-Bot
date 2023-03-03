from collections import defaultdict


class MemoryInterface:
    def append(self, user_id: str, text: dict[str, str]) -> None:
        pass

    def get(self, user_id: str) -> list:
        return []

    def remove(self, user_id: str) -> None:
        pass


class Memory(MemoryInterface):
    def __init__(self):
        self.storage = defaultdict(list)

    def append(self, user_id: str, text: dict[str, str]) -> None:
        self.storage[user_id].append(text)

    def get(self, user_id: str) -> list:
        HISTORY_MESSAGE_COUNT = 4
        return self.storage.get(user_id, [])[-HISTORY_MESSAGE_COUNT:]

    def remove(self, user_id: str) -> None:
        self.storage[user_id] = []
