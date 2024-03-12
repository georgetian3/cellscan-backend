from config import Config
from models.database import Database
from services.measurement import MeasurementService
from services.client import ClientService


class Services:
    """ Services """
    
    def __init__(self, config: Config, database: Database):
        self.measurement = MeasurementService(config, database)
        self.client = ClientService(config, database)