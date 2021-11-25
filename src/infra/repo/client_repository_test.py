from faker import Faker
from .client_repository import ClientRepository

faker = Faker()
client_repository = ClientRepository()

def test_insert_client_repository():
    """ Test insert in client """

    type_person = "fisica"
    name_person = faker.name()

    new_client = client_repository.insert_client(type_person, name_person)

    print(new_client)