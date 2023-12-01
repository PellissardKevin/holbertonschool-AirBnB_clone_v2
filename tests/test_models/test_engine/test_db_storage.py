#!/usr/bin/python3
import unittest
from models.engine.db_storage import DBStorage
import pycodestyle


class TestDBstorage(unittest.TestCase):
    """Unit test for dbstorage"""

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db')
    @classmethod
    def setUpClass(cls):
        """set up for test"""
        cls.user = User()
        cls.user.first_name = "Kev"
        cls.user.last_name = "Yo"
        cls.user.email = "1234@yahoo.com"
        cls.storage = DBStorage()

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db')
    @classmethod
    def teardown(cls):
        """at the end of the test this will tear it down"""
        del cls.user

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db')
    def test_pep8_DBStorage(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db')
    def test_all(self):
        """tests if all works in DB Storage"""
        storage = DBStorage()
        obj = storage.all()
        self.assertIsNotNone(obj)
        self.assertEqual(type(obj), dict)
        self.assertIs(obj, storage._DBStorage__objects)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db')
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

    def testPycodeStyle(self):
        """Test pycodestyle for console"""
        style = pycodestyle.StyleGuide(quiet=True)
        p = style.check_files(['models/engin/db_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")


if __name__ == "__main__":
    unittest.main()
