from typing import List
from abc import ABC, abstractmethod
from src.models.sqlite.entities.person import PersonTable

class PersonRepositoryInterface(ABC):

    @abstractmethod
    def insert_person(self, first_name: str, last_name: str, age: int, pet_id: int) -> None:
        pass

    @abstractmethod
    def get_person(self, person_id: int) -> PersonTable:
        pass

    @abstractmethod
    def list_people(self) -> List[PersonTable]:
        pass

    @abstractmethod
    def delete_person(self, name: str) -> None:
        pass
