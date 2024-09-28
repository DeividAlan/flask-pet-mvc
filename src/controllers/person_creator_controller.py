from typing import Dict
import re
from src.models.sqlite.interface.person_repository import PersonRepositoryInterface

class PersonCreatorController():
    def __init__(self, person_repository: PersonRepositoryInterface) -> None:
        self.__person_repository = person_repository

    def create(self, person_info: Dict) -> Dict:
        first_name = person_info["first_name"]
        last_name = person_info["last_name"]
        age = person_info["age"]
        pet_id = person_info["pet_id"]

        self.__validate_name(first_name)
        self.__validate_name(last_name)
        self.__insert_person_in_db(first_name, last_name, age, pet_id)
        format_response = self.__format_response(person_info)
        return format_response

    def __validate_name(self, name: str) -> None:
        non_valid_characters = re.compile(r'[^a-zA-Z]')

        if non_valid_characters.search(name):
            raise Exception("Invalid name")

    def __insert_person_in_db(self, first_name: str, last_name: str, age: int, pet_id: int) -> None:
        self.__person_repository.insert_person(first_name, last_name, age, pet_id)


    def __format_response(self, person_info: Dict) -> Dict:
        return {
            "data": {
                "type": "Person",
                "count": 1,
                "attributes": person_info
            }
        }
