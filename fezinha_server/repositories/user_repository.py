from typing import Optional
from uuid import UUID

from pymysql.connections import Connection

from fezinha_server.entities.user import User
from fezinha_server.repositories import user_queries


class UserRepository:

    def __init__(self, connection: Connection):
        self.connection = connection

    def create_user(self, user: User):
        query = user_queries.INSERT_USER
        dto = UserRepository.__convert_user_to_dto(user)

        cursor = self.connection.cursor()
        cursor.execute(query, dto)
        self.connection.commit()

    def update_user(self, user: User):
        query = user_queries.UPDATE_USER
        dto = UserRepository.__convert_user_to_dto(user)

        cursor = self.connection.cursor()
        cursor.execute(query, dto)
        self.connection.commit()

    def delete_user(self, user_id: UUID):
        query = user_queries.DELETE_USER

        cursor = self.connection.cursor()
        cursor.execute(query, {"id": str(user_id)})
        self.connection.commit()

    def get_user_by_id(self, user_id: UUID) -> Optional[User]:
        query = user_queries.SELECT_USER

        cursor = self.connection.cursor()
        cursor.execute(query, {"id": str(user_id)})

        return UserRepository.__convert_cursor_tuple_to_user(cursor.fetchone())

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
