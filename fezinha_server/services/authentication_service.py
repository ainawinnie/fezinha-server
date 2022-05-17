from fezinha_server.entities.exceptions.entity_not_found_exception import EntityNotFoundException
from fezinha_server.entities.exceptions.invalid_parameter_exception import InvalidParameterException
from fezinha_server.entities.user import User
from fezinha_server.repositories.user_repository import UserRepository
from fezinha_server.entities.exceptions.invalid_credentials_exception import InvalidCredentialsException
from fezinha_server.utils import bcrypt_utils


class AuthenticationService:

    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def authenticate(self, login: str, password: str) -> User:
        if not login or not password:
            raise InvalidParameterException(["login", "password"], "authenticate")

        user = self.user_repository.find_user_by_login(login)

        if not user:
            raise EntityNotFoundException("User", login)

        if not bcrypt_utils.check_encrypted_password(password, user.password):
            raise InvalidCredentialsException(login)

        return user
