from typing import List, NamedTuple, Optional
from abc import ABC, abstractmethod
from src.models.sqlite.entities.person import PersonTable

class PersonWithPet(NamedTuple):
    first_name: str
    last_name: str
    pet_name: Optional[str]
    pet_type: Optional[str]

class PersonRepositoryInterface(ABC):

    @abstractmethod
    def insert_person(self, first_name: str, last_name: str, age: int, pet_id: int) -> None:
        pass

    @abstractmethod
    def get_person(self, person_id: int) -> Optional[PersonWithPet]:
        pass

    @abstractmethod
    def list_people(self) -> List[PersonTable]:
        pass

    @abstractmethod
    def delete_person(self, name: str) -> None:
        pass
