from datetime import datetime
from sqlmodel import Field, SQLModel


class MeasurementUpload(SQLModel):
    time_measured: datetime

    longitude: float
    latitude: float
    altitude: float

    cell_id: int
    signal_strength: float

    misc: str

class Measurement(MeasurementUpload, table=True):
    __tablename__ = 'measurement'
    id: int = Field(primary_key=True)
    time_uploaded: datetime
    ip: str