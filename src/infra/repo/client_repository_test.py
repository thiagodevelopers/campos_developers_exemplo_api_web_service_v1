from faker import Faker
from src.infra.config import DBConnectionHandler
from .client_repository import ClientRepository

faker = Faker()
client_repository = ClientRepository()
db_connection_handler = DBConnectionHandler()


def test_insert_client_repository():
    """Test insert in client"""

    type_person = "fisica"
    name_person = faker.name()

    engine = db_connection_handler.get_engine()

    new_client = client_repository.insert_client(type_person, name_person)
    query_client = engine.execute(
        "SELECT * FROM clients WHERE ID='{}';".format(new_client.id)
    ).fetchone()

    assert new_client.id == query_client.id
    assert new_client.name == query_client.name
