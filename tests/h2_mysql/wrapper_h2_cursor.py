from datetime import datetime
from typing import Optional, List, Any, Iterable

from jaydebeapi import Cursor, DatabaseError
from pymysql import IntegrityError


class WrapperH2Cursor:
    cursor: Cursor
    all_items: Optional[List[Any]]

    def __init__(self, cursor: Cursor):
        self.cursor = cursor

    def execute(self, query: str, parameters: Optional[Iterable[Any]] = None):
        parsed_query = query
        if parameters:
            processed_parameters = WrapperH2Cursor.__escape_args(parameters)
            parsed_query = parsed_query % processed_parameters

        try:
            return self.cursor.execute(parsed_query)
        except DatabaseError as ex:
            if "JdbcSQLIntegrityConstraintViolationException" in str(ex):
                error = IntegrityError("error unique")
                raise error
            raise ex

    def fetchall(self) -> List[tuple]:
        rows = self.cursor.fetchall()

        if not rows:
            return list()

        return [WrapperH2Cursor.__convert_row(row) for row in rows]

    def fetchone(self) -> Optional[tuple]:
        return WrapperH2Cursor.__convert_row(self.cursor.fetchone())

    def __iter__(self):
        if not self.all_items:
            self.all_items = self.fetchall()

        self.iterator_index = 0
        return self

    def __next__(self):
        if not len(self.all_items):
            self.all_items = None
            raise StopIteration

        return self.all_items.pop()

    def close(self):
        self.cursor.close()

    @staticmethod
    def __escape_args(parameters: Iterable[Any]) -> Iterable[Any]:
        if isinstance(parameters, dict):
            result = dict()
            for key in parameters.keys():
                result[key] = "'" + str(parameters[key]) + "'"
        else:
            result = list()
            for item in parameters:
                result.append("'" + str(item) + "'")

        return result



    @staticmethod
    def __convert_row(row: Optional[tuple]) -> Optional[tuple]:
        if not row:
            return None

        return tuple([WrapperH2Cursor.__convert_column(column) for column in row])

    @staticmethod
    def __convert_column(column: Optional[Any]) -> Optional[Any]:
        if not column:
            return None

        try:
            if WrapperH2Cursor.__str_date_has_milliseconds(column):
                column = datetime.strptime(column, "%Y-%m-%d %H:%M:%S.%f")
            else:
                column = datetime.strptime(column, "%Y-%m-%d %H:%M:%S")
        except Exception:
            # the value is not a valid datetime
            pass

        return column

    @staticmethod
    def __str_date_has_milliseconds(str_date: Optional[str]) -> bool:
        """
        In the h2 the datetime is persisted as timestamp
        """
        if not str_date:
            return False
        return len(str_date) > 19
