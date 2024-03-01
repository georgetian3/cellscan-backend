from datetime import datetime
from sqlalchemy import Column, Text
from sqlmodel import Field, SQLModel
from sqlalchemy.dialects.mysql import LONGTEXT


class MeasurementUpload(SQLModel):
    time_measured: datetime

    longitude: float
    latitude: float
    altitude: float

    cell_id: int
    signal_strength: float

    misc: str = Column(LONGTEXT),

class Measurement(MeasurementUpload, table=True):
    __tablename__ = 'measurement'
    id: int = Field(primary_key=True)
    time_uploaded: datetime
    ip: str