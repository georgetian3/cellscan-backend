import json
import pathlib
import aiohttp
from fastapi.responses import FileResponse
from models.client import Client
from services.base_service import BaseService


class ClientService(BaseService):

    async def get_latest_apk(self) -> FileResponse | None:
        async with aiohttp.ClientSession() as session:
            # NOTE: need to manually place APK in /src/ folder, or run `download-apk.sh`
            try:
                latest_apk_name = list(pathlib.Path('.').glob('*.apk'))[0]
            except:
                return

            return FileResponse(
                latest_apk_name,
                filename=latest_apk_name,
                media_type='application/vnd.android.package-archive'
            )            