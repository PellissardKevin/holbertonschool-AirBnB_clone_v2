#!/usr/bin/python3
import unittest
from models.engine.db_storage import DBStorage
from models.user import User
from models.state import State
from models.place import Place


class TestDBstorage(unittest.TestCase):
    """Unit test for dbstorage"""
    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db')
    @classmethod
    def setUpClass(cls):
        cls.user = User()
        cls.user.first_name = "Kev"
        cls.user.last_name = "Yo"
        cls.user.email = "1234@yahoo.com"
        cls.storage = DBStorage()

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db')
    @classmethod
    def teardown(cls):
        del cls.user

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db')
    def test_all(self):
        storage = DBStorage()
        obj = storage.all()
        self.assertIsNotNone(obj)
        self.assertEqual(type(obj), dict)
        self.assertIs(obj, storage._DBStorage__objects)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db')
    def test_new(self):
        storage = DBStorage()
        obj = storage.all()
        user = User()
        user.id = 123455
        user.name = "Kevin"
        storage.new(user)
        key = user.__class__.__name__ + "." + str(user.id)
        self.assertIsNotNone(obj[key])

    def test_doc_console(self):
        self.assertIsNotNone(DBStorage.__doc__)
        self.assertIsNotNone(DBStorage.__init__.__doc__)
        self.assertIsNotNone(DBStorage.all.__doc__)
        self.assertIsNotNone(DBStorage.new.__doc__)
        self.assertIsNotNone(DBStorage.save.__doc__)
        self.assertIsNotNone(DBStorage.delete.__doc__)
        self.assertIsNotNone(DBStorage.reload.__doc__)

    def testPycodeStyle(self):
        style = pycodestyle.StyleGuide(quiet=True)
        p = style.check_files(['models/engin/db_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def setUp(self):
        self.storage = DBStorage()
        self.storage.reload()

    def tearDown(self):
        self.storage.close()

    def test_all_method_returns_dict(self):
        result = self.storage.all()
        self.assertIsInstance(result, dict)

    def test_all_method_returns_correct_dict_for_state(self):
        state = State(name="California")
        self.storage.new(state)
        self.storage.save()
        result = self.storage.all(State)
        self.assertEqual(len(result), 1)
        key = 'State.' + str(state.id)
        self.assertIn(key, result)

    def test_all_method_returns_correct_dict_for_user(self):
        user = User(username="john_doe")
        self.storage.new(user)
        self.storage.save()
        result = self.storage.all(User)
        self.assertEqual(len(result), 1)
        key = 'User.' + str(user.id)
        self.assertIn(key, result)

    def test_new_method_adds_object_to_session(self):
        state = State(name="New York")
        self.storage.new(state)
        self.assertIn(state, self.storage._DBStorage__session.new)

    def test_save_method_commits_changes(self):
        state = State(name="Texas")
        self.storage.new(state)
        self.storage.save()
        self.assertIn(state, self.storage.all(State).values())

    def test_delete_method_removes_object_from_session(self):
        state = State(name="Florida")
        self.storage.new(state)
        self.storage.delete(state)
        self.assertNotIn(state, self.storage._DBStorage__session)

    def test_reload_method_creates_session(self):
        self.storage.reload()
        self.assertIsNotNone(self.storage._DBStorage__session)


if __name__ == "__main__":
    unittest.main()
