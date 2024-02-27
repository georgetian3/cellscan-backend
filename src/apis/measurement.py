from typing import List
from models.measurement import MeasurementUpload, Measurement
from apis.base import BaseRouter
from apis.documented_response import create_documentation, JDR, JDR204

class MeasurementApi(BaseRouter):
    """ Location API """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        @self.get('/measurements', **create_documentation(
            JDR(200, 'All measurements', List[Measurement])
        ))
        async def get_measurements():
            return await self.services.measurement.get_measurements()

        @self.post('/measurements', **create_documentation(JDR204))
        async def upload_measurements(measurements: List[MeasurementUpload]):
            await self.services.measurement.upload_measurements(measurements)
