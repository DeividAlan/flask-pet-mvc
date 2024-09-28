from typing import List, Optional
from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.person import PersonTable
from src.models.sqlite.entities.pet import PetTable
from ..interface.person_repository import PersonRepositoryInterface, PersonWithPet

class PersonRepository(PersonRepositoryInterface):
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection

    def insert_person(self, first_name: str, last_name: str, age: int, pet_id: int) -> None:
        with self.__db_connection as database:
            try:
                person_data = PersonTable(
                    first_name = first_name,
                    last_name = last_name,
                    age = age,
                    pet_id = pet_id,
                )

                database.session.add(person_data)
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception

    def list_people(self) -> List[PersonTable]:
        with self.__db_connection as database:
            try:
                people = database.session.query(PersonTable).all()
                return people
            except NoResultFound:
                return []

    def get_person(self, person_id: int) -> Optional[PersonWithPet]:
        with self.__db_connection as database:
            try:
                person = (
                        database.session.query(
                        PersonTable.first_name,
                        PersonTable.last_name,
                        PetTable.name.label("pet_name"),
                        PetTable.type.label("pet_type"),
                    )
                    .outerjoin(PetTable, PetTable.id == PersonTable.pet_id)
                    .filter(PersonTable.id == person_id)
                    .one()
                )
                return PersonWithPet(
                    first_name=person.first_name,
                    last_name=person.last_name,
                    pet_name=person.pet_name,
                    pet_type=person.pet_type
                )
            except NoResultFound:
                return None

    def delete_person(self, name: str) -> None:
        with self.__db_connection as database:
            try:
                (
                    database.session
                        .query(PersonTable)
                        .filter(PersonTable.name == name)
                        .delete()
                )
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception
