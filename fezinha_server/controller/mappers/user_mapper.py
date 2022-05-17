from typing import Optional

from fezinha_server.entities.user import User
from fezinha_server.utils import utils


class UserMapper:

    @staticmethod
    def to_entity(dto: dict) -> Optional[User]:
        if not dto:
            return None

        return User(id=utils.str_to_uuid(dto.get("id")), name=dto.get("name"), login=dto.get("login"),
                    password=dto.get("password"))

    @staticmethod
    def to_dto(user: User) -> Optional[dict]:
        if not user:
            return None

        return {
            "id": str(user.id),
            "name": user.name,
            "login": user.login,
            "password": user.password
        }
