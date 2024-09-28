import pytest
from .person_creator_controller import PersonCreatorController

class MockPersonRepository():
    def insert_person(self, first_name: str, last_name: str, age: int, pet_id: int) -> None:
        pass

def test_create():
    person_info = {
        "first_name": "Jhon",
        "last_name": "Doe",
        "age": 30,
        "pet_id": 123
    }

    controller = PersonCreatorController(MockPersonRepository())
    response = controller.create(person_info)

    assert response["data"]["type"] == "Person"
    assert response["data"]["count"] == 1
    assert response["data"]["attributes"] == person_info

def test_create_error():
    person_info = {
        "first_name": "Jhon123",
        "last_name": "Doe",
        "age": 30,
        "pet_id": 123
    }

    controller = PersonCreatorController(MockPersonRepository())

    with pytest.raises(Exception):
        controller.create(person_info)
