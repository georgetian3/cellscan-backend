import asyncio

import nest_asyncio
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import URL
from sqlmodel import SQLModel
from config import ConfigDatabase

from models.measurement import *

nest_asyncio.apply()

from sqlalchemy.ext.compiler import compiles
from sqlalchemy.types import DateTime

# https://stackoverflow.com/questions/29711102/sqlalchemy-mysql-millisecond-or-microsecond-precision
@compiles(DateTime, 'mysql')
def compile_datetime_mysql(type_, compiler, **kw):
    return 'DATETIME(6)'

class Database:
    def __init__(self, config: ConfigDatabase):
        self.engine = create_async_engine(URL.create(**config._asdict()))
        # self.engine = create_async_engine('sqlite+aiosqlite:///test.db')
        self.async_session_maker: AsyncSession = sessionmaker(self.engine, class_=AsyncSession)
        self.create_tables()

    def async_session(self) -> AsyncSession:
        return self.async_session_maker()
    
    def create_tables(self):
        async def _create_tables():
            async with self.engine.begin() as conn:
                await conn.run_sync(SQLModel.metadata.create_all)
        asyncio.run(_create_tables())

    def reset(self):
        async def _reset():
            async with self.engine.begin() as conn:
                await conn.run_sync(SQLModel.metadata.drop_all)
        asyncio.run(_reset())
        self.create_tables()