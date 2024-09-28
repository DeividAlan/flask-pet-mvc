#pylint: disable=unused-argument
from typing import Optional
import pytest
from src.models.sqlite.interface.person_repository import PersonWithPet
from .person_finder_controller import PersonFinderController

class MockPersonRepository():
    def get_person(self, person_id: int) -> Optional[PersonWithPet]:
        return PersonWithPet(
            first_name = "John",
            last_name = "Doe",
            pet_name = "rex",
            pet_type = "dog"
        )

class MockPersonRepositoryNoResult():
    def get_person(self, person_id: int) -> Optional[PersonWithPet]:
        return None

def test_finder():
    person_id = 1
    controller = PersonFinderController(MockPersonRepository())
    response = controller.finder(person_id)

    assert response["data"]["type"] == "Person"
    assert response["data"]["count"] == 1
    assert response["data"]["attributes"] == {
        "first_name": "John",
        "last_name": "Doe",
        "pet_name": "rex",
        "pet_type": "dog"
    }

def test_finder_error():
    person_id = 1
    controller = PersonFinderController(MockPersonRepositoryNoResult())

    with pytest.raises(Exception):
        controller.finder(person_id)
