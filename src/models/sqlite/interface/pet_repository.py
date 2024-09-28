from abc import ABC, abstractmethod
from typing import List
from src.models.sqlite.entities.pet import PetTable

class PetRepositoryInterface(ABC):

    @abstractmethod
    def list_pets(self) -> List[PetTable]:
        pass

    @abstractmethod
    def delete_pet(self, name: str) -> None:
        pass
