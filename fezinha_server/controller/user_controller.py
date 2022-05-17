from flask import Blueprint, request
from flask_jwt import jwt_required

from fezinha_server.controller import errors_handler
from fezinha_server.controller.mappers.user_mapper import UserMapper
from fezinha_server.services.user_service import UserService

controller = Blueprint("user_controller", __name__, url_prefix="/api/user")
errors_handler.fill_error_handlers_to_controller(controller)


@controller.route("/", methods=["POST"])
def create_user(user_service: UserService):
    user_dto = request.json
    user = UserMapper.to_entity(user_dto)
    user_service.create_user(user)
    return user_dto, 200

