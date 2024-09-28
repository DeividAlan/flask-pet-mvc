from typing import List
from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.pet import PetTable
from ..interface.pet_repository import PetRepositoryInterface

class PetRepository(PetRepositoryInterface):
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection

    def list_pets(self) -> List[PetTable]:
        with self.__db_connection as database:
            try:
                pets = database.session.query(PetTable).all()
                return pets
            except NoResultFound:
                return []

    def delete_pet(self, name: str) -> None:
        with self.__db_connection as database:
            try:
                (
                    database.session
                        .query(PetTable)
                        .filter(PetTable.name == name)
                        .delete()
                )
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception
