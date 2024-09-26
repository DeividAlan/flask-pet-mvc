from unittest import mock
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
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

    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

def test_list_pets():
    mock_connection = MockConnection()
    repo = PetRepository(mock_connection)
    response = repo.list_pets()

    mock_connection.session.query.assert_called_once_with(PetTable)
    mock_connection.session.all.assert_called_once()
    mock_connection.session.filter.assert_not_called()

    assert response[0].name == "dog"
