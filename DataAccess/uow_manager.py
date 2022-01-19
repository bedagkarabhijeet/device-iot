
import psycopg2


from uow import UOW

from initializer import configuration

class UOWManager:
    """
    UOW manager pattern.

    We create a database connection and context
    All the queries are executed under same context
    Post context completion check if there is any exception;
    In case there is an exception then we call rollback and call commit otherwise
    """
    def __init__(self):
        self.__db_connection = psycopg2.connect(configuration.get("connection_string"))

    def __enter__(self):
        cursor = self.__db_connection.cursor()
        return UOW(cursor)

    def __exit__(self, exc_type: str, exc_value: str, exc_traceback: str):
        if exc_value:
            self.__db_connection.rollback()
        else:
            self.__db_connection.commit()

        self.__db_connection.close()
