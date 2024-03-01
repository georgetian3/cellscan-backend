from datetime import datetime
from sqlalchemy import Column, UnicodeText
from sqlmodel import Field, SQLModel
from sqlmodel 

class MeasurementUpload(SQLModel):
    time_measured: datetime

    longitude: float
    latitude: float
    altitude: float

    cell_id: int
    signal_strength: float
    mcc: int

    misc: str = Field(sa_column=Column(UnicodeText()))

class Measurement(MeasurementUpload, table=True):
    __tablename__ = 'measurement'
    id: int = Field(primary_key=True)
    time_uploaded: datetime
    ip: str