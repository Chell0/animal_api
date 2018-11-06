"""Import libraries."""
import unittest
import json

from app import app

class TestAnimalApi(unittest.TestCase):
    """Testing our api."""

    def setUp(self):
        """Our setup."""
        self.app = app
        self.client = self.app.test_client()
        self.animals = {'name': 'Goat'}


    def test_homePage(self):
        """Test if we can get our home page respinse."""
        res = self.client.get('/', content_type="application/json")
        self.assertEqual(res.status_code, 200)

    def test_returnAll(self):
        """Test if our api can fetch all animals."""
        res = self.client.get('/animals', content_type="application/json")
        self.assertEqual(res.status_code, 200)


if __name__ == '__main__':
    unittest.main()
