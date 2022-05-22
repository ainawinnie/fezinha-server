import uuid
from uuid import UUID

from fezinha_server.entities.exceptions.duplicate_entity_exception import DuplicateEntityException
from fezinha_server.entities.user import User
from fezinha_server.repositories.user_repository import UserRepository
from tests.integ.base_test import BaseTest


class TestUserRepository(BaseTest):

    def setUp(self):
        super().setUp()
        self.user_repository = UserRepository(self.db_connection)

    def test_find_user_by_id(self):
        # when
        user = self.user_repository.find_user_by_id(UUID(self.DEFAULT_ID))
        # then
        self.assertIsNotNone(user)
        self.assertEqual("Test 1", user.name)
        self.assertEqual("test", user.login)

    def test_create_and_find_user(self):
        # given
        user = User(id=uuid.uuid4(), name="New test", login="new_login", password="12345")
        # when
        self.user_repository.create_user(user)
        persisted_user = self.user_repository.find_user_by_id(user.id)
        # then
        self.assertEqual(user, persisted_user)
        self.assertEqual(user.name, persisted_user.name)
        self.assertEqual(user.login, persisted_user.login)
        self.assertEqual(user.password, persisted_user.password)

    def test_update_and_find_user(self):
        # given
        user = User(id=uuid.UUID(self.DEFAULT_ID), name="New test", login="new_login", password="12345")
        # when
        self.user_repository.update_user(user)
        persisted_user = self.user_repository.find_user_by_id(user.id)
        # then
        self.assertEqual(user, persisted_user)
        self.assertEqual(user.name, persisted_user.name)
        self.assertEqual(user.login, persisted_user.login)
        self.assertEqual(user.password, persisted_user.password)

    def test_delete_user(self):
        self.user_repository.delete_user(uuid.UUID(self.DEFAULT_ID))
        user = self.user_repository.find_user_by_id(uuid.UUID(self.DEFAULT_ID))
        self.assertIsNone(user)

    def test_find_by_login(self):
        # when
        user = self.user_repository.find_user_by_login("test")
        # then
        self.assertIsNotNone(user)
        self.assertEqual("Test 1", user.name)

    def test_create_duplicate_user(self):
        # given
        user = User(id=uuid.UUID(self.DEFAULT_ID), name="New test", login="test", password="12345")
        # when
        with self.assertRaises(DuplicateEntityException) as ex:
            self.user_repository.create_user(user)
        self.assertTrue("already persisted" in str(ex.exception))
        self.assertTrue("test" in str(ex.exception))

    def test_update_duplicate_user(self):
        # given
        user = User(id=uuid.uuid4(), name="New test", login="test2", password="12345")
        self.user_repository.create_user(user)
        user.login = "test"
        # when
        with self.assertRaises(DuplicateEntityException) as ex:
            self.user_repository.update_user(user)
        self.assertTrue("already persisted" in str(ex.exception))
