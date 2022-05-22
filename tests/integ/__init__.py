import jaydebeapi
import pymysql

from fezinha_server import config
from fezinha_server.utils import utils
from tests.h2_mysql.wrapper_h2_connection import WrapperH2Connection

TEST_DATABASE = "test_db"

config.DB_PORT = 25231
config.DB_HOST = "localhost"
config.DB_USERNAME = "root"
config.DB_PASSWORD = ""
config.DB_DATABASE = TEST_DATABASE

TEST_DB_URL = f"jdbc:h2:mem:{config.DB_DATABASE};DATABASE_TO_UPPER=false;MODE=MYSQL"

driver_path = f"{utils.get_root_dir()}/resources/database/h2-1.4.200.jar"
h2_connection = jaydebeapi.connect("org.h2.Driver", TEST_DB_URL, ["", ""], driver_path)
db_connection = WrapperH2Connection(h2_connection)


def get_test_connection(*args, **kwargs):
    return db_connection


pymysql.connect = get_test_connection
