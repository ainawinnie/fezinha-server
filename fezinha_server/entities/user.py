from dataclasses import dataclass
from uuid import UUID


@dataclass #Para que serve o dataclass mesmo?
class User:
    id: UUID
    name: str
    login: str
    password: str
