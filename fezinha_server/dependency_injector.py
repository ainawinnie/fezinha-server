from injector import Module, Binder, singleton
from pymysql.connections import Connection

from fezinha_server.repositories.user_repository import UserRepository
from fezinha_server.services.authentication_service import AuthenticationService
from fezinha_server.services.user_service import UserService


class DependencyInjector(Module):

    def __init__(self, connection: Connection):
        self.connection = connection

    def configure(self, binder: Binder):
        user_repository = UserRepository(self.connection)

        authentication_service = AuthenticationService(user_repository)
        user_service = UserService(user_repository)

        binder.bind(UserRepository, to=user_repository, scope=singleton)
        binder.bind(AuthenticationService, to=authentication_service, scope=singleton)
        binder.bind(UserService, to=user_service, scope=singleton)
