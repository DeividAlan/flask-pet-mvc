from typing import Dict, List
from src.models.sqlite.interface.pet_repository import PetRepositoryInterface
from src.models.sqlite.entities.pet import PetTable
from .interfaces.pet_list_controller import PetListControllerInterface

class PetListController(PetListControllerInterface):
    def __init__(self, pet_repository: PetRepositoryInterface) -> None:
        self.__pet_repository = pet_repository

    def list(self) -> Dict:
        pets_list = self.__get_pets_in_db()
        format_response = self.__format_response(pets_list)
        return format_response

    def __get_pets_in_db(self) -> List[PetTable]:
        pets_list = self.__pet_repository.list_pets()
        return pets_list

    def __format_response(self, pets_list: List[PetTable]) -> Dict:
        formatted_pets_list = []
        for pet in pets_list:
            formatted_pets_list.append({
                "id": pet.id,
                "name": pet.name,
                "type": pet.type
            })

        return {
            "data": {
                "type": "Pets",
                "count": len(formatted_pets_list),
                "attributes": formatted_pets_list
            }
        }
