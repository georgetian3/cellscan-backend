import json

from fastapi.responses import FileResponse
from models.client import Client
from services.base_service import BaseService
import aiohttp
import pathlib

class ClientService(BaseService):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.latest_version: str = None

    async def get_latest_apk(self) -> Client:
        async with aiohttp.ClientSession() as session:
            async with session.get('https://api.github.com/repos/georgetian3/cellscan-app/releases/latest') as response:
                data = json.loads(await response.text())
            latest_apk_name = data['assets'][0]['name']
            if not pathlib.Path(latest_apk_name).is_file():
                async with session.get(data['assets'][0]['browser_download_url']) as response:
                    with open(latest_apk_name, 'wb') as f:
                        f.write(await response.read())
            return FileResponse(
                latest_apk_name,
                filename=latest_apk_name,
                media_type='application/vnd.android.package-archive'
            )            