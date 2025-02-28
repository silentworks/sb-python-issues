from gotrue import AsyncSupportedStorage


class FastApiSessionStorage(AsyncSupportedStorage):
    def __init__(self, storage):
        self.storage = storage

    async def get_item(self, key: str) -> str | None:
        if key in self.storage:
            return self.storage[key]

    async def set_item(self, key: str, value: str) -> None:
        self.storage[key] = value

    async def remove_item(self, key: str) -> None:
        if key in self.storage:
            self.storage.pop(key, None)
