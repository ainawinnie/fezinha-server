from flask import Flask

from fezinha_server.controller import user_controller


def register_controllers(app: Flask):
    app.register_blueprint(user_controller.controller)
