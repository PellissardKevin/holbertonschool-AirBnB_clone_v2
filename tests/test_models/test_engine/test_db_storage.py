#!/usr/bin/python3
import unittest
from models.engine.db_storage import DBStorage
import pycodestyle


class TestDBstorage(unittest.TestCase):
    """Unit test for dbstorage"""

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
