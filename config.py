from typing import NamedTuple
import os

class ConfigDatabase(NamedTuple):
    drivername: str = 'mysql+aiomysql'
    username: str = os.getenv('DB_USER')
    password: str = os.getenv('DB_PASS')
    host: str = 'db'
    port: int = 3306
    database: str = 'mysql'

class Config(NamedTuple):
    database: ConfigDatabase = ConfigDatabase()