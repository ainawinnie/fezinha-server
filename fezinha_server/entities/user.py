from dataclasses import dataclass
from uuid import UUID


@dataclass
class User:
    id: UUID
    name: str
    login: str
    password: str

    def __eq__(self, other):
        return isinstance(other, User) and self.id == other.id
