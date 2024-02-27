from config import Config
from models.database import Database

class BaseService:
    def __init__(self, config: Config, database: Database):
        self.config = config
        self.database = database