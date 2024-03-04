from datetime import datetime
from sqlalchemy import Column, UnicodeText
from sqlmodel import Field, SQLModel

class MeasurementUpload(SQLModel):
    time_measured: datetime
    longitude: float
    latitude: float
    altitude: float
    # large number required to create LONGTEXT in MySQL
    cell_info: str = Field(sa_column=Column(UnicodeText(32000000)))
    misc: str = Field(sa_column=Column(UnicodeText(32000000)))

class Measurement(MeasurementUpload, table=True):
    __tablename__ = 'measurement'
    id: int = Field(primary_key=True)
    time_uploaded: datetime
    ip: str