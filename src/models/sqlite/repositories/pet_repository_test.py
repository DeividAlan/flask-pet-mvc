from unittest import mock
import pytest
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.pet import PetTable
from .pet_repository import PetRepository

class MockConnection:
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock(
            data=[
                (
                    [mock.call.query(PetTable)],
                    [
                        PetTable(name="dog", type="dog"),
                        PetTable(name="cat", type="cat")
                    ]
                )
            ]
        )
    def __enter__(self): return self
    def __exit__(self, exc_type, exc_val, exc_tb): pass

class MockConnectionNoResult:
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock()
        self.session.query.side_effect = self.__rase_no_result_found

    def __rase_no_result_found(self, *args, **kwargs):
        raise NoResultFound("No result found")

    def __enter__(self): return self
    def __exit__(self, exc_type, exc_val, exc_tb): pass

def test_list_pets():
    mock_connection = MockConnection()
    repo = PetRepository(mock_connection)
    response = repo.list_pets()

    mock_connection.session.query.assert_called_once_with(PetTable)
    mock_connection.session.all.assert_called_once()
    mock_connection.session.filter.assert_not_called()

    assert response[0].name == "dog"

def test_delete_pet():
    mock_connection = MockConnection()
    repo = PetRepository(mock_connection)
    repo.delete_pet(name="petName")

    mock_connection.session.query.assert_called_once_with(PetTable)
    mock_connection.session.filter.assert_called_once_with(PetTable.name == "petName")
    mock_connection.session.delete.assert_called_once()

def test_list_pets_no_result():
    mock_connection = MockConnectionNoResult()
    repo = PetRepository(mock_connection)
    response = repo.list_pets()

    mock_connection.session.query.assert_called_once_with(PetTable)
    mock_connection.session.all.assert_not_called()
    mock_connection.session.filter.assert_not_called()

    assert response == []

def test_delete_pet_error():
    mock_connection = MockConnectionNoResult()
    repo = PetRepository(mock_connection)

    with pytest.raises(Exception):
        repo.delete_pet(name="petName")

    mock_connection.session.rollback.assert_called_once()
