from src.domain.models import Clients
from src.infra.config import DBConnectionHandler
from src.infra.entities import Clients as ClientsModel


class ClientRepository:
    """class to manager Clients Repository"""

    @classmethod
    def insert_client(cls, type_person: str, name_person: str):
        """insert data in user entity
        :param - type_person: type of person Física or Jurídica
        :param - name_person: name of person
        :return - tuple with new client inserted
        """

        with DBConnectionHandler() as db_connection:
            try:
                new_client = ClientsModel(type=type_person, name=name_person)
                db_connection.session.add(new_client)
                db_connection.session.commit()

                return Clients(
                    id=new_client.id, type=new_client.type, name=new_client.name
                )
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
