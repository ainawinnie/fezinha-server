from typing import Optional

import jaydebeapi

from tests.h2_mysql.wrapper_h2_cursor import WrapperH2Cursor


class WrapperH2Connection:
    connection: Optional[jaydebeapi.Connection]

    def __init__(self, connection: jaydebeapi.Connection):
        self.connection = connection
        self.h2_cursor = None

    def cursor(self):
        self.h2_cursor = WrapperH2Cursor(self.connection.cursor())
        return self.h2_cursor

    def commit(self):
        self.connection.commit()

    def close(self):
        pass
