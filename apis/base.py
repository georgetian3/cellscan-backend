import fastapi
from config import Config

from services.services import Services


class BaseRouter(fastapi.APIRouter):
    def __init__(self, config: Config, services: Services, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.services = services
        self.config = config
