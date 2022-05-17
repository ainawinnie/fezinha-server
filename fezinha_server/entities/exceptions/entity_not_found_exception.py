

class EntityNotFoundException(Exception):
    def __init__(self, entity: str, identifier: str):
        super().__init__(f"The {entity} {identifier} was not found")
