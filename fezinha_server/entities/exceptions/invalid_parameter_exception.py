from typing import List


class InvalidParameterException(Exception):
    def __init__(self, parameters: List[str], operation: str):
        super(f"Invalid parameters to {operation}: {parameters}")
