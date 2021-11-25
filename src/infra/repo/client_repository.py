from collections import namedtuple
from src.infra.config import DBConnectionHandler
from src.infra.entities import Clients

class ClientRepository:
    """ class to manager Clients Repository  """

    @classmethod
    def insert_client(cls, type_person : str, name_person : str):
        """ insert data in user entity
        :param - type_person: type of person Física or Jurídica
        :param - name_person: name of person
        :return - None  
        """

        insert_data = namedtuple("clients", "id, type, name")

        with DBConnectionHandler() as db_connection:
            try:
                new_client = Clients(type=type_person, name=name_person)
                db_connection.session.add(new_client)
                db_connection.session.commit()

                return insert_data(id=new_client.id, type=new_client.type, name=new_client.name)
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()