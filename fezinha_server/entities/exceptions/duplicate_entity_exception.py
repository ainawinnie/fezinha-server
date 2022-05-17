

class DuplicateEntityException(Exception):
    def __init__(self, entity: str, identifier: str):
        super().__init__(f"The {entity} {identifier} is already persisted")
