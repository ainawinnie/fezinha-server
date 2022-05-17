from flask import Blueprint

from fezinha_server import log
from fezinha_server.entities.exceptions.duplicate_entity_exception import DuplicateEntityException
from fezinha_server.entities.exceptions.entity_not_found_exception import EntityNotFoundException
from fezinha_server.entities.exceptions.invalid_credentials_exception import InvalidCredentialsException
from fezinha_server.entities.exceptions.invalid_parameter_exception import InvalidParameterException

logger = log.get_logger(__name__)


def fill_error_handlers_to_controller(controller: Blueprint):

    @controller.errorhandler(EntityNotFoundException)
    def entity_not_found_exception(exception: EntityNotFoundException):
        logger.exception(exception)
        return str(exception), 404

    @controller.errorhandler(InvalidCredentialsException)
    def entity_not_found_exception(exception: InvalidCredentialsException):
        logger.exception(exception)
        return str(exception), 403

    @controller.errorhandler(InvalidParameterException)
    def invalid_entity_exception(exception: InvalidParameterException):
        logger.exception(exception)
        return str(exception), 400

    @controller.errorhandler(DuplicateEntityException)
    def duplicate_entity_exception(exception: InvalidParameterException):
        logger.exception(exception)
        return str(exception), 409

    @controller.errorhandler(Exception)
    def generic_exception(exception: Exception):
        logger.exception(exception)
        return "A generic exception occurred. Ask admin for help.", 500
