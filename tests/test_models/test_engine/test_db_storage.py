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


@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', "Not Database")
class TestDBstorage(unittest.TestCase):
    """Unit test for dbstorage"""

    @classmethod
    def setUpClass(cls):
        """set up for test"""
        cls.user = User()
        cls.user.first_name = "Kev"
        cls.user.last_name = "Yo"
        cls.user.email = "1234@yahoo.com"
        cls.storage = DBStorage()

    @classmethod
    def teardown(cls):
        """at the end of the test this will tear it down"""
        del cls.user

    def test_pep8_DBStorage(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_all(self):
        """tests if all works in DB Storage"""
        storage = DBStorage()
        obj = storage.all()
        self.assertIsNotNone(obj)
        self.assertEqual(type(obj), dict)
        self.assertIs(obj, storage._DBStorage__objects)

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

    def test_doc_console(self):
        """Test for the doc string"""
        self.assertIsNotNone(DBStorage.__doc__)
        self.assertIsNotNone(DBStorage.__init__.__doc__)
        self.assertIsNotNone(DBStorage.all.__doc__)
        self.assertIsNotNone(DBStorage.new.__doc__)
        self.assertIsNotNone(DBStorage.save.__doc__)
        self.assertIsNotNone(DBStorage.delete.__doc__)
        self.assertIsNotNone(DBStorage.reload.__doc__)

    # test 1re tranche
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
        user = User(username="john_doe", email="gui@hbtn.io",
                    password="guipwd")
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

    def test_existence_user(self):
        '''
        Testing if User class is being created properly
        '''
        user = User(email="john@snow.com", password="johnpwd")
        user.save()
        if user.id in models.storage.all('User'):
            self.assertTrue(user.password, "johnpwd")

    def test_existence_amenity(self):
        '''
        Testing if Amenity class is being created properly
        '''
        amenity = Amenity(name="Wifi")
        amenity.save()
        if amenity.id in models.storage.all():
            self.assertTrue(amenity.name, "Wifi")

    def test_existence_state(self):
        '''
        Testing if State class is being created properly
        '''
        state = State(name="Alaska")
        state.save()
        if state.id in models.storage.all():
            self.assertTrue(state.name, "Alaska")

    def test_all_method(self):
        '''
        Testing if all() method returns all instances
        '''
        state = State(name="Cali")
        state.save()
        amenity = Amenity(name="Cable")
        amenity.save()
        user = User(email="john@snow.com", password="johnpwd")
        user.save()
        test_me = str(state.id) + str(amenity.id) + str(user.id)
        if test_me in models.storage.all():
            self.assertTrue(state.name, "Cali")

    def test_delete_method(self):
        '''
            Tests the delete method in db_storage
        '''
        state = State(name="Texas")
        state.save()
        all_stored = models.storage.all()
        models.storage.delete(state)
        self.assertTrue(all_stored["State." + state.id])


if __name__ == "__main__":
    unittest.main()
