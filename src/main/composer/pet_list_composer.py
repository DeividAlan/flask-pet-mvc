from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.pet_repository import PetRepository
from src.controllers.pet_list_controller import PetListController
from src.views.pet_list_view import PetListView

def pet_list_composer():
    model = PetRepository(db_connection_handler)
    controller = PetListController(model)
    view = PetListView(controller)

    return view
