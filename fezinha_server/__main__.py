from datetime import timedelta

import pymysql
from flask import Flask
from flask_injector import FlaskInjector
from injector import Injector

from fezinha_server import config, register_controllers
from fezinha_server.dependency_injector import DependencyInjector
from fezinha_server.security import authentication_utils

__db_connection = pymysql.connect(host=config.DB_HOST, port=config.DB_PORT, user=config.DB_USERNAME,
                                  password=config.DB_PASSWORD, database=config.DB_DATABASE)

dependency_injector = Injector([DependencyInjector(__db_connection)])

app = Flask(__name__)
app.config['SECRET_KEY'] = config.ENCRYPT_SECRET_KEY
app.config['JWT_AUTH_URL_RULE'] = "/api/auth/authenticate"
app.config['JWT_EXPIRATION_DELTA'] = timedelta(hours=config.HOURS_TO_EXPIRATION_TOKEN)

jwt = authentication_utils.fill_jwt_auth_function(app, dependency_injector)

register_controllers.register_controllers(app)
FlaskInjector(app=app, injector=dependency_injector)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=config.HOST_PORT)
