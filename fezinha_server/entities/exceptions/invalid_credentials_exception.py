from typing import Optional


class InvalidCredentialsException(Exception): #É para registrar senha inválida?
    def __init__(self, login: Optional[str]): #O que significa o optional?
        super(f"Invalid credentials for {login}")
