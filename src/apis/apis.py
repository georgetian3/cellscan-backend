import json
from fastapi import FastAPI
from apis.client import ClientAPI

from apis.measurement import MeasurementApi


class Api(FastAPI):
    """ QiQi API """
    def __init__(self, *args, **kwargs):
        super().__init__(
            title='CellScan API',
            version='1.0.0',
            root_path='/api/v1',
        )
        self.include_router(MeasurementApi(*args, **kwargs))
        self.include_router(ClientAPI(*args, **kwargs))
        
    def get_openapi(self):
        with open('openapi.json', 'w') as f:
            json.dump(self.openapi(), f, indent=2)