import aiohttp
import asyncio
from config import Config

class Fragment:
    def __init__(self):
        self.session = None
        self.config = Config()

    async def __aenter__(self):
        self.session = aiohttp.ClientSession()
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.session.close()

    async def get(self, id):
        try:
            async with self.session.get(f"{self.config.BASE_URL}{id}") as response:
                 if response.status == 200:
                    return await response.json()
                 elif response.status == 404:
                    print(f"Fragmento {id} no existe")
                    return None
                 else:
                    print(f"Error inesperado con fragmento {id}: {response.status}")
                    return None
        except Exception as e:
            print(f"error{id}: {e}")
            return None