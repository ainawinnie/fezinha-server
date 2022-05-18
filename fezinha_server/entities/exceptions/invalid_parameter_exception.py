from typing import List


class InvalidParameterException(Exception):
    def __init__(self, parameters: List[str], operation: str):
        super().__init__(f"Invalid parameters to {operation}: {parameters}")
