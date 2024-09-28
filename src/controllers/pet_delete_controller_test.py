from .pet_delete_controller import PetDeleteController

def test_delete_pet(mocker):
    mock_repository = mocker.Mock()
    controller = PetDeleteController(mock_repository)
    controller.delete("Max")

    mock_repository.delete_pet.assert_called_once_with("Max")
