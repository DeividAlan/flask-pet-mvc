import pytest
from src.models.sqlite.settings.connection import db_connection_handler
from .pet_repository import PetRepository
from .person_repository import PersonRepository

# db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="interaction with the bank")
def test_list_pets():
    repo = PetRepository(db_connection_handler)
    response = repo.list_pets()
    print()
    print(response)

@pytest.mark.skip(reason="interaction with the bank")
def test_delete_pet():
    name = "belinha"

    repo = PetRepository(db_connection_handler)
    repo.delete_pet(name)

@pytest.mark.skip(reason="interaction with the bank")
def test_insert_person():
    first_name = "first name"
    last_name = "last name"
    age = 77
    pet_id = 2

    repo = PersonRepository(db_connection_handler)
    repo.insert_person(first_name, last_name, age, pet_id)

@pytest.mark.skip(reason="interaction with the bank")
def test_get_person():
    person_id = 1

    repo = PersonRepository(db_connection_handler)
    response = repo.get_person(person_id)
    print()
    print(response)
