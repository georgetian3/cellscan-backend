from config import Config
from models.database import Database
from services.measurement import MeasurementService


class Services:
    """ Services """
    
    def __init__(self, config: Config, database: Database):
        self.measurement = MeasurementService(config, database)