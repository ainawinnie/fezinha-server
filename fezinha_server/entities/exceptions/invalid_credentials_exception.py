from typing import Optional


class InvalidCredentialsException(Exception):
    def __init__(self, login: Optional[str]):
        super().__init__(f"Invalid credentials for {login}")
