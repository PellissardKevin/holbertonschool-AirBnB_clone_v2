#!/usr/bin/pyhthon3
"""Module for the test of MySQL"""
import MySQLdb
import unittest
from unittest.mock import patch
import io
from console import HBNBCommand
from os import getenv
from models.engine.db_storage import DBStorage
import os


@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', "Not DBStorage")
class TestMySQL(unittest.TestCase):
    """Test for the SQL database"""
    conn = None
    cur = None

    def connection(self):
        """Connect to MySQLdb"""
        storage = DBStorage()
        storage.reload()
        self.conn = MySQLdb.connect(getenv('HBNB_MYSQL_HOST'),
                                    getenv('HBNB_MYSQL_USER'),
                                    getenv('HBNB_MYSQL_PWD'),
                                    getenv('HBNB_MYSQL_DB'))
        self.cur = self.conn.cursor()

    def disconnection(self):
        """Disconnect from MySQLdb"""
        self.cur.close()
        self.conn.close()
        self.conn = None
        self.cur = None

    def test_create_state(self):
        """Test create of a State"""
        self.connection()
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd('create State name="California"')
        self.cur.execute("SELECT COUNT(*) FROM states")
        res = self.cur.fetchone()[0]
        self.assertEqual(res, 1)
        self.disconnection()

    def test_create_city(self):
        """Test create of a City"""
        self.connection()
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd('create State name="California"')
        id = f.getvalue()[:-1]
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd(f'''create City state_id="{id}"
                                 name="San_Francisco"''')
        self.cur.execute("SELECT COUNT(*) FROM cities")
        res = self.cur.fetchone()[0]
        self.assertEqual(res, 1)
        self.disconnection()

    def test_create_user(self):
        """Test create of a User"""
        self.connection()
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd('create User firstname="John"')
        self.cur.execute("SELECT COUNT(*) FROM users")
        res = self.cur.fetchone()[0]
        self.assertEqual(res, 1)
        self.disconnection()

    def test_create_place(self):
        """Test create of a place"""
        self.connection()
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd('create State name="California"')
        id_state = f.getvalue()[:-1]
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd(f'''create City state_id="{id_state}"
                                 name="San_Francisco"''')
        id_city = f.getvalue()[:-1]
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd(f'''create Place city_id="{id_city}"
                                 name="Lovely_place"''')
        self.cur.execute("SELECT COUNT(*) FROM places")
        res = self.cur.fetchone()[0]
        self.assertEqual(res, 1)
        self.disconnection()

    def test_create_review(self):
        """Test create of a Review"""
        self.connection()
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd('create State name="California"')
        id_state = f.getvalue()[:-1]
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd(f'''create City state_id="{id_state}"
                                 name="San_Francisco"''')
        id_city = f.getvalue()[:-1]
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd(f'''create Place city_id="{id_city}"
                                 name="Lovely_place"''')
        id_place = f.getvalue()[:-1]
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd('create User firstname="John"')
        id_user = f.getvalue()[:-1]
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd(f'''create Review place_id="{id_place}"
                                 user_id="{id_user}" text="Charming"''')
        self.cur.execute("SELECT COUNT(*) FROM reviews")
        res = self.cur.fetchone()[0]
        self.assertEqual(res, 1)
        self.disconnection()

    def test_create_amenity(self):
        """Test create of a Amenity"""
        self.connection()
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd('create Amenity name="Wifi"')
        self.cur.execute("SELECT COUNT(*) FROM amenities")
        res = self.cur.fetchone()[0]
        self.assertEqual(res, 1)
        self.disconnection()

if __name__ == '__main__':
    unittest.main()
