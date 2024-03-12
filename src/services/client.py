import json
from models.client import Client
from services.base_service import BaseService
import aiohttp

class ClientService(BaseService):

    async def get_client(self) -> Client:
        async with aiohttp.ClientSession() as session:
            async with session.get('https://api.github.com/repos/georgetian3/cellscan-app/releases/latest') as response:
                data = await response.text()
                try:
                    latest_version = json.loads(data)['tag_name'][1:]
                except:
                    latest_version = None
                return Client(latest_version=latest_version)