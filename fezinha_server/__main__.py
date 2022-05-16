import uuid

import pymysql

from fezinha_server import config
from fezinha_server.entities.user import User
from fezinha_server.repositories.user_repository import UserRepository

if __name__ == '__main__':
    connection = pymysql.connect(host=config.DB_HOST, port=config.DB_PORT, user=config.DB_USERNAME,
                                 password=config.DB_PASSWORD, database=config.DB_DATABASE)

    user_repository = UserRepository(connection)
