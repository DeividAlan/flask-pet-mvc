#pylint: disable=unused-argument
from typing import List
from src.models.sqlite.entities.pet import PetTable
from .pet_list_controller import PetListController

class MockPetRepository():
    def list_pets(self) -> List[PetTable]:
        return [
            PetTable(id=1, name="Fluffy", type="cat"),
            PetTable(id=2, name="Max", type="dog")
        ]

class MockPetRepositoryNoResult():
    def list_pets(self) -> List[PetTable]:
        return []

def test_lister():
    attributes = [
        { "id": 1, "name": "Fluffy", "type": "cat" },
        { "id": 2, "name": "Max", "type": "dog" }
    ]

    controller = PetListController(MockPetRepository())
    response = controller.list()

    assert response["data"]["type"] == "Pets"
    assert response["data"]["count"] == 2
    assert response["data"]["attributes"] == attributes

def test_lister_empty():
    controller = PetListController(MockPetRepositoryNoResult())
    response = controller.list()

    assert response["data"]["type"] == "Pets"
    assert response["data"]["count"] == 0
    assert not response["data"]["attributes"]
