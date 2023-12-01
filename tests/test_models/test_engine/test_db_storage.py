#!/usr/bin/python3
from unittest import skipIf, TestCase
import unittest 
from models.engine.db_storage import DBStorage
from models.user import User
from models.state import State
from unittest.mock import patch
from models import storage
import os
import pycodestyle


<<<<<<< HEAD
class TestDBstorage(TestCase):
    """Unit test for dbstorage"""

    # k test

    skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db')
=======
class TestDBstorage(unittest.TestCase):
    """Unit test for dbstorage"""
    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db')
>>>>>>> 6cdd1eeeb0a399766fc2de833616a3a3beb6ed3d
    @classmethod
    def setUpClass(cls):
        """set up for test"""
        cls.user = User()
        cls.user.first_name = "Kev"
        cls.user.last_name = "Yo"
        cls.user.email = "1234@yahoo.com"
        cls.storage = DBStorage()

    skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db')
    @classmethod
    def teardown(cls):
        """at the end of the test this will tear it down"""
        del cls.user

    skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db')
    def test_pep8_DBStorage(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db')
    def test_all(self):
        """tests if all works in DB Storage"""
        storage = DBStorage()
        obj = storage.all()
        self.assertIsNotNone(obj)
        self.assertEqual(type(obj), dict)
        self.assertIs(obj, storage._DBStorage__objects)

    skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db')
    def test_new(self):
        """test when new is created"""
        storage = DBStorage()
        obj = storage.all()
        user = User()
        user.id = 123455
        user.name = "Kevin"
        storage.new(user)
        key = user.__class__.__name__ + "." + str(user.id)
        self.assertIsNotNone(obj[key])

    skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db')
    def test_doc_console(self):
        """Test for the doc string"""
        self.assertIsNotNone(DBStorage.__doc__)
        self.assertIsNotNone(DBStorage.__init__.__doc__)
        self.assertIsNotNone(DBStorage.all.__doc__)
        self.assertIsNotNone(DBStorage.new.__doc__)
        self.assertIsNotNone(DBStorage.save.__doc__)
        self.assertIsNotNone(DBStorage.delete.__doc__)
        self.assertIsNotNone(DBStorage.reload.__doc__)

    skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db')
    def testPycodeStyle(self):
<<<<<<< HEAD
        """Test pycodestyle for console"""
        style = pycodestyle.StyleGuide(quiet=True)
        p = style.check_files(['models/engin/db_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")
=======
        style = pycodestyle.StyleGuide(quiet=True)
        p = style.check_files(['models/engin/db_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def setUp(self):
        self.storage = DBStorage()
        self.storage.reload()

    def tearDown(self):
        self.storage.close()
>>>>>>> 6cdd1eeeb0a399766fc2de833616a3a3beb6ed3d

    # test 1re tranche
    skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db')
    def test_all_method_returns_dict(self):
        result = self.storage.all()
        self.assertIsInstance(result, dict)

    skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db')
    def test_all_method_returns_correct_dict_for_state(self):
        state = State(name="California")
        self.storage.new(state)
        self.storage.save()
        result = self.storage.all(State)
        self.assertEqual(len(result), 1)
        key = 'State.' + str(state.id)
        self.assertIn(key, result)

    skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db')
    def test_all_method_returns_correct_dict_for_user(self):
        user = User(username="john_doe", email="gui@hbtn.io", password="guipwd")
        self.storage.new(user)
        self.storage.save()
        result = self.storage.all(User)
        self.assertEqual(len(result), 1)
        key = 'User.' + str(user.id)
        self.assertIn(key, result)

    skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db')
    def test_new_method_adds_object_to_session(self):
        state = State(name="New York")
        self.storage.new(state)
        self.assertIn(state, self.storage._DBStorage__session.new)

    skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db')
    def test_save_method_commits_changes(self):
        state = State(name="Texas")
        self.storage.new(state)
        self.storage.save()
        self.assertIn(state, self.storage.all(State).values())

    skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db')
    def test_delete_method_removes_object_from_session(self):
        state = State(name="Florida")
        self.storage.new(state)
        self.storage.delete(state)
        self.assertNotIn(state, self.storage._DBStorage__session)

    skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db')
    def test_reload_method_creates_session(self):
        self.storage.reload()
        self.assertIsNotNone(self.storage._DBStorage__session)

    @skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db')
    def test_delete_method_removes_object_from_session_and_database(self):
        state = State(name="Florida")
        self.storage.new(state)
        self.storage.save()
        
        # Vérifie que l'objet est initialement dans la session
        self.assertIn(state, self.storage._DBStorage__session)
        
        # Supprime l'objet et sauvegarde les modifications
        self.storage.delete(state)
        self.storage.save()
        
        # Vérifie que l'objet n'est plus dans la session
        self.assertNotIn(state, self.storage._DBStorage__session)

        # Vérifie que l'objet n'est plus dans la base de données
        result = self.storage.all(State)
        self.assertNotIn(state, result.values())

    @skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db')
    def test_reload_method_rolls_back_session(self):
        state = State(name="Texas")
        self.storage.new(state)
        self.storage.save()
        
        # Modifie l'objet dans la session sans sauvegarder
        state.name = "New Texas"
        
        # Appelle reload pour réinitialiser la session
        self.storage.reload()
        
        # Vérifie que les modifications n'ont pas été sauvegardées
        result = self.storage.all(State)
        self.assertNotEqual(result[state.id].name, "New Texas")

if __name__ == "__main__":
    unittest.main()
