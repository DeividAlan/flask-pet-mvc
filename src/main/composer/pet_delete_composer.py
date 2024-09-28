from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.pet_repository import PetRepository
from src.controllers.pet_delete_controller import PetDeleteController
from src.views.pet_delete_view import PetDeleteView

def pet_delete_composer():
    model = PetRepository(db_connection_handler)
    controller = PetDeleteController(model)
    view = PetDeleteView(controller)

    return view
