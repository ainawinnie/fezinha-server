import os
import unittest

from flask import Flask
from pymysql.connections import Connection

from fezinha_server.utils import utils
from tests.integ import db_connection


class BaseTest(unittest.TestCase):
    ENCRYPT_SECRET_KEY = "ENCRYPT_SECRET_KEY"
    DEFAULT_ID = "00000000-0000-0000-0000-000000000000"

    def setUp(self):
        self.db_connection: Connection = db_connection
        create_db_file_path = os.path.join(utils.get_root_dir(), "resources", "database", "create-database.sql")
        init_db_file_path = os.path.join(utils.get_root_dir(), "resources", "database", "initial-load.sql")

        self.execute_sql_file(create_db_file_path)
        self.execute_sql_file(init_db_file_path)

    def create_app(self):
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True
        self.app.config['SECRET_KEY'] = self.ENCRYPT_SECRET_KEY
        self.app.config['JWT_AUTH_URL_RULE'] = "/api/auth/authenticate"

        return self.app

    def execute_sql_file(self, file_path: str):
        file = open(file_path)
        cursor = self.db_connection.cursor()
        for query in file.read().split(";"):
            if query.strip():
                cursor.execute(query.strip())
        file.close()

    def tearDown(self):
        cursor = self.db_connection.cursor()
        cursor.execute(f"DROP ALL OBJECTS")
