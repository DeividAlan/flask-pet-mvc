from src.models.sqlite.interface.pet_repository import PetRepositoryInterface
from .interfaces.pet_delete_controller import PetDeleteControllerInterface

class PetDeleteController(PetDeleteControllerInterface):
    def __init__(self, pet_repository: PetRepositoryInterface) -> None:
        self.__pet_repository = pet_repository

    def delete(self, name: str) -> None:
        self.__pet_repository.delete_pet(name)
