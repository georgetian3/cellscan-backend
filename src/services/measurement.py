from datetime import datetime
from typing import List
from services.base_service import BaseService
from models.measurement import MeasurementUpload, Measurement
from pytz import UTC
import sqlalchemy

# TODO: remove `string`

class MeasurementService(BaseService):

    async def get_measurements(self) -> List[Measurement]:
        async with self.database.async_session() as session:
            return await session.scalars(sqlalchemy.select(Measurement))

    async def upload_measurements(self, measurements: List[MeasurementUpload], ip: str) -> None:
        time_uploaded = datetime.now().astimezone(UTC)
        async with self.database.async_session() as session:
            for measurement in measurements:
                # sanitize
                # TODO
                # insert into db
                session.add(Measurement(**measurement.model_dump(), time_uploaded=time_uploaded, ip=ip))
            await session.commit()