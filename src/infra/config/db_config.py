"""
Author: Thiago de Souza Santos
Create: 25/11/2021
Description: file connection in database

Initiate database:
create all tables:

from src.infra.config import *
db_conn = DBConnectionHandler()
engine = db_conn.get_engine()
Base.metadata.create_all(engine)

"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBConnectionHandler:
    """Sqlalchemy database connection"""

    def __init__(self):
        self.__connection_string = (
            "postgresql+psycopg2://postgres:Postgres2021!@localhost/clients"
        )
        self.session = None

    def get_engine(self):
        """Return connection engine
        :param - None
        :return - engine connection to database
        """

        engine = create_engine(self.__connection_string, echo=True)

        return engine
    
    def __enter__(self):
        engine = create_engine(self.__connection_string)
        session_maker = sessionmaker()
        self.session = session_maker(bind=engine)

        return self

    def __exit__(self, exc_type, exc_val, ext_tb):
        self.session.close() #pylint: disable=no-member
