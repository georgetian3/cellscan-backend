from fastapi.responses import FileResponse
from apis.base import BaseRouter

class ClientAPI(BaseRouter):
    """ Client API """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        @self.api_route('/apk/latest', methods=['GET', 'HEAD'], response_class=FileResponse, status_code=200, description='Download latest APK')
        async def get_latest_apk():
            return await self.services.client.get_latest_apk()
