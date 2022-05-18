import unittest
import uuid
from unittest.mock import Mock

from fezinha_server.entities.exceptions.entity_not_found_exception import EntityNotFoundException
from fezinha_server.entities.exceptions.invalid_credentials_exception import InvalidCredentialsException
from fezinha_server.entities.exceptions.invalid_parameter_exception import InvalidParameterException
from fezinha_server.entities.user import User
from fezinha_server.services.authentication_service import AuthenticationService
from fezinha_server.utils import bcrypt_utils


class TestAuthenticationService(unittest.TestCase):

    def setUp(self):
        self.repository = Mock()
        self.service = AuthenticationService(self.repository)
        self.password1 = "12345"
        self.user1 = User(id=uuid.uuid4(), name="User 1", login="login",
                          password=bcrypt_utils.encrypt_password(self.password1))

    def test_authenticate_with_success(self):
        # given
        self.repository.find_user_by_login.return_value = self.user1
        # when
        user = self.service.authenticate(self.user1.login, self.password1)
        # then
        self.assertEqual(self.user1, user)

    def test_authenticate_with_wrong_pass(self):
        # given
        self.repository.find_user_by_login.return_value = self.user1
        # when
        with self.assertRaises(InvalidCredentialsException) as ex:
            self.service.authenticate(self.user1.login, "wrong_password")
        # then
        self.assertTrue(self.user1.login in str(ex.exception))

    def test_authenticate_with_wrong_login(self):
        # given
        self.repository.find_user_by_login.return_value = None
        # when
        with self.assertRaises(EntityNotFoundException) as ex:
            self.service.authenticate("wrong_login", "wrong_password")
        # then
        self.assertTrue("wrong_login" in str(ex.exception))

    def teste_authenticate_without_pass(self):
        # when
        with self.assertRaises(InvalidParameterException) as ex:
            self.service.authenticate("wrong_login", None)
        # then
        self.assertTrue("authenticate" in str(ex.exception))
