from fastapi import Response
from fastapi.responses import FileResponse
from apis.base import BaseRouter
from apis.documented_response import JDR404

class ClientAPI(BaseRouter):
    """ Client API """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        @self.api_route('/apk/latest',
            methods=['GET', 'HEAD'],
            description='Download latest APK',
        )
        async def get_latest_apk():
            file = await self.services.client.get_latest_apk()
            if file is None:
                return Response(status_code=404)
            return file
