import argparse

import models.database
from apis.apis import Api
from config import Config
from services.services import Services

config = Config()
database = models.database.Database(config.database)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--reset', action='store_true')
    args = parser.parse_args()
    if args.reset:
        database.reset()
        exit()

api = Api(config, Services(config=config, database=database))