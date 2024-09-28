from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.person_repository import PersonRepository
from src.controllers.person_creator_controller import PersonCreatorController
from src.views.person_creator_view import PersonCreatorView

def person_creator_composer():
    model = PersonRepository(db_connection_handler)
    controller = PersonCreatorController(model)
    view = PersonCreatorView(controller)

    return view
