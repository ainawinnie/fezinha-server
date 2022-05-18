import unittest
import uuid
from unittest.mock import Mock

from fezinha_server.entities.exceptions.invalid_parameter_exception import InvalidParameterException
from fezinha_server.entities.user import User
from fezinha_server.services.user_service import UserService
from fezinha_server.utils import bcrypt_utils


class TestUserService(unittest.TestCase):

    def setUp(self):
        self.repository = Mock()
        self.service = UserService(self.repository)
        self.user1 = User(id=None, name="User 1", login="login", password="password")

    def test_create_user_success(self):
        # given
        self.repository.create_user.return_value = self.user1
        # when
        self.service.create_user(self.user1)
        # then
        self.assertIsNotNone(self.user1.id)
        self.assertTrue(bcrypt_utils.check_encrypted_password("password", self.user1.password))

    def test_create_user_without_name_and_login(self):
        # given
        self.user1.name = ""
        self.user1.login = ""
        self.repository.create_user.return_value = self.user1
        # when
        with self.assertRaises(InvalidParameterException) as ex:
            self.service.create_user(self.user1)
        # then
        self.assertTrue("name" in str(ex.exception))
        self.assertTrue("login" in str(ex.exception))

    def test_create_user_without_password(self):
        # given
        self.user1.password = ""
        self.repository.create_user.return_value = self.user1
        # when
        with self.assertRaises(InvalidParameterException) as ex:
            self.service.create_user(self.user1)
        # then
        self.assertTrue("password" in str(ex.exception))
