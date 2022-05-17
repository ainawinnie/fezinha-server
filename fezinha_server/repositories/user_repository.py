from typing import Optional
from uuid import UUID

from pymysql import IntegrityError
from pymysql.connections import Connection

from fezinha_server.entities.exceptions.duplicate_entity_exception import DuplicateEntityException
from fezinha_server.entities.user import User
from fezinha_server.repositories import user_queries


class UserRepository:

    def __init__(self, connection: Connection):
        self.connection = connection

    def create_user(self, user: User):
        query = user_queries.INSERT_USER
        dto = UserRepository.__convert_user_to_dto(user)

        cursor = self.connection.cursor()
        try:
            cursor.execute(query, dto)
            self.connection.commit()
        except IntegrityError as ex:
            UserRepository.__handle_integrity_error(ex, user.login)

    def update_user(self, user: User):
        query = user_queries.UPDATE_USER
        dto = UserRepository.__convert_user_to_dto(user)

        cursor = self.connection.cursor()
        try:
            cursor.execute(query, dto)
            self.connection.commit()
        except IntegrityError as ex:
            UserRepository.__handle_integrity_error(ex, "user")

    def delete_user(self, user_id: UUID):
        query = user_queries.DELETE_USER

        cursor = self.connection.cursor()
        cursor.execute(query, {"id": str(user_id)})
        self.connection.commit()

    def find_user_by_id(self, user_id: UUID) -> Optional[User]:
        query = user_queries.SELECT_USER

        cursor = self.connection.cursor()
        cursor.execute(query, {"id": str(user_id)})

        return UserRepository.__convert_cursor_tuple_to_user(cursor.fetchone())

    def find_user_by_login(self, login: str) -> Optional[User]:
        query = user_queries.SELECT_USER_LOGIN

        cursor = self.connection.cursor()
        cursor.execute(query, {"login": login})

        return UserRepository.__convert_cursor_tuple_to_user(cursor.fetchone())

    @staticmethod
    def __handle_integrity_error(exception: IntegrityError, identifier: str):
        if "UNIQUE" not in exception.args[1] and "Duplicate" not in exception.args[1]:
            raise exception

        raise DuplicateEntityException("user", identifier)

    @staticmethod
    def __convert_cursor_tuple_to_user(cursor_user: tuple) -> Optional[User]:
        if not cursor_user:
            return None

        return User(id=UUID(cursor_user[0]), name=cursor_user[1], login=cursor_user[2], password=cursor_user[3])

    @staticmethod
    def __convert_user_to_dto(user: User) -> dict:
        return {
            "id": str(user.id),
            "login": user.login,
            "name": user.name,
            "password": user.password
        }
