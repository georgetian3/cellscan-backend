from typing import NamedTuple
import os

class ConfigDatabase(NamedTuple):
    drivername  : str = os.getenv('CELLSCAN_DB_DRIVER', 'sqlite+aiosqlite')
    username    : str = os.getenv('CELLSCAN_DB_USER')
    password    : str = os.getenv('CELLSCAN_DB_PASS')
    host        : str = os.getenv('CELLSCAN_DB_HOST')
    port        : int = os.getenv('CELLSCAN_DB_PORT')
    database    : str = os.getenv('CELLSCAN_DB_DB', 'cellscan.db')

class Config(NamedTuple):
    database: ConfigDatabase = ConfigDatabase()