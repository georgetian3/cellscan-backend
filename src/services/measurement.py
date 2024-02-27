from datetime import datetime
from typing import List
from services.base_service import BaseService
from models.measurement import MeasurementUpload, Measurement
from pytz import UTC
import sqlalchemy

# TODO: remove `string`
ALL_OPERATING_SYSTEMS = frozenset(['Android', 'iOS', 'string'])

class MeasurementService(BaseService):

    async def get_measurements(self) -> List[Measurement]:
        async with self.database.async_session() as session:
            return await session.scalars(sqlalchemy.select(Measurement))

    async def upload_measurements(self, measurements: List[MeasurementUpload]) -> None:
        time_uploaded = datetime.now().astimezone(UTC)
        async with self.database.async_session() as session:
            for measurement in measurements:
                # sanitize
                if measurement.operating_system not in ALL_OPERATING_SYSTEMS:
                    continue
                # insert into db
                session.add(Measurement(**measurement.model_dump(), time_uploaded=time_uploaded))
            await session.commit()