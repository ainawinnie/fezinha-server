import uuid

from fezinha_server.entities.exceptions.invalid_parameter_exception import InvalidParameterException
from fezinha_server.entities.user import User
from fezinha_server.repositories.user_repository import UserRepository
from fezinha_server.utils import bcrypt_utils


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def create_user(self, user: User):
        UserService.assert_user(user)
        user.id = uuid.uuid4()
        user.password = bcrypt_utils.encrypt_password(user.password)

        self.user_repository.create_user(user)

    @staticmethod
    def assert_user(user: User):
        invalid_fields = list()
        if not user.name:
            invalid_fields.append("name")
        if not user.login:
            invalid_fields.append("login")
        if not user.password:
            invalid_fields.append("password")
        if invalid_fields:
            raise InvalidParameterException(invalid_fields, "create user")
