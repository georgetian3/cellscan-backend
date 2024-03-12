from models.client import Client
from apis.base import BaseRouter
from apis.documented_response import create_documentation, JDR

class ClientAPI(BaseRouter):
    """ Client API """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        @self.get('/client', **create_documentation(
            JDR(200, 'Get client info', Client)
        ))
        async def get_client():
            return await self.services.client.get_client()
