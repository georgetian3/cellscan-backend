from typing import List
from models.measurement import MeasurementUpload, Measurement
from apis.base import BaseRouter
from apis.documented_response import create_documentation, JDR, JDR204
from fastapi import Request

class MeasurementApi(BaseRouter):
    """ Measurement API """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        @self.get('/measurements', **create_documentation(
            JDR(200, 'All measurements', List[Measurement])
        ))
        async def get_measurements():
            return await self.services.measurement.get_measurements()
        
        @self.get('/measurements/last', **create_documentation(
            JDR(200, 'Last measurement', Measurement | None)
        ))
        async def get_last_measurement():
            return await self.services.measurement.get_last_measurement()

        @self.post('/measurements', **create_documentation(JDR204))
        async def upload_measurements(measurements: List[MeasurementUpload], request: Request):
            await self.services.measurement.upload_measurements(measurements, request.client.host.split(':')[0])
