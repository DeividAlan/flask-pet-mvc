from typing import Dict
from src.models.sqlite.interface.person_repository import PersonRepositoryInterface, PersonWithPet
from src.errors.errors_types.http_not_found import HttpNotFoundError
from .interfaces.person_finder_controller import PersonFinderControllerInterface

class PersonFinderController(PersonFinderControllerInterface):
    def __init__(self, person_repository: PersonRepositoryInterface) -> None:
        self.__person_repository = person_repository

    def finder(self, person_id: int) -> Dict:
        person_info = self.__find_person_in_db(person_id)
        format_response = self.__format_response(person_info)
        return format_response

    def __find_person_in_db(self, person_id: int) -> Dict:
        person_with_pet: PersonWithPet = self.__person_repository.get_person(person_id)

        if not person_with_pet:
            raise HttpNotFoundError("Person not found")

        return person_with_pet._asdict()

    def __format_response(self, person_info: Dict) -> Dict:
        return {
            "data": {
                "type": "Person",
                "count": 1,
                "attributes": person_info
            }
        }
