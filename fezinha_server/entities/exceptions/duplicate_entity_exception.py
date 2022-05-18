

class DuplicateEntityException(Exception):
    def __init__(self, entity: str, identifier: str):#O que é __init__? Pq usou self?
        super().__init__(f"The {entity} {identifier} is already persisted") #O que é super? Otexto mostrado não deveria
        #ser em português, já que os usuários são brasileiros?
