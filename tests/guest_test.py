import unittest
from classes.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest_1 = Guest("Ross", 50, "Crazy Train")
        

    def test_guest_name(self):
        self.assertEqual("Ross", self.guest_1.name)