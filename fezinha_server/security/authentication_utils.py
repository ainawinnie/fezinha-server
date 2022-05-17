from functools import wraps

from flask import Flask, current_app
from flask_jwt import JWT, JWTError, _jwt_required
from injector import Injector

from fezinha_server.entities.exceptions.invalid_credentials_exception import InvalidCredentialsException
from fezinha_server.repositories.user_repository import UserRepository
from fezinha_server.security.auth_user import AuthUser
from fezinha_server.services.authentication_service import AuthenticationService
from fezinha_server.utils import utils


def fill_jwt_auth_function(app: Flask, injector: Injector) -> JWT:

    def authenticate(login: str, password: str):
        authentication_service = injector.get(AuthenticationService)
        try:
            return AuthUser(authentication_service.authenticate(login, password))
        except InvalidCredentialsException as ex:
            raise JWTError("Invalid credentials", str(ex))

    def identity(payload: dict):
        user_repository = injector.get(UserRepository)
        user_id = utils.str_to_uuid(payload.get("identity"))
        return user_repository.find_user_by_id(user_id)

    return JWT(app, authenticate, identity)
