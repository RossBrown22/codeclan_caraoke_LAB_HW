import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song


class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room_1 = Room("Singing Room 1", 2)
        self.room_2 = Room("Singing Room 2", 2)
        self.room_3 = Room("Singing Room 3", 3)
        self.guest_1 = Guest("Ross", 50, "Crazy Train")
        self.guest_2 = Guest("Alex", 30, "Future Days")
        self.guest_3 = Guest("Chandler", 3, "Country Road")
        self.song_1 = Song("Crazy Train", "Ozzy Osbourne", 4)
        self.song_2 = Song("Future Days", "Pearl Jam", 4)
        self.song_3 = Song("Creep", "Radiohead", 4)
        

    def test_room_has_name(self):
        expected = "Singing Room 1"
        actual = self.room_1.name
        self.assertEqual(expected, actual)

    def test_amount_of_guests(self):
        expected = 0
        actual = self.room_1.amount_of_guests()
        self.assertEqual(expected, actual)
    
    def test_check_in_guest(self):
        self.room_1.check_in_guest(self.guest_1)
        self.assertIn(self.guest_1, self.room_1.guest_list)

    def test_check_out_guest(self):
        self.room_1.check_in_guest(self.guest_1)
        self.room_1.check_out_guest(self.guest_1)
        self.assertNotIn(self.guest_1, self.room_1.guest_list)

    def test_amount_of_songs(self):
        expected = 0
        actual = self.room_1.amount_of_songs()
        self.assertEqual(expected, actual)

    def test_add_song(self):
        self.room_1.add_song(self.song_1)
        self.assertIn(self.song_1, self.room_1.song_list)
    
    def test_remove_song(self):
        self.room_1.add_song(self.song_1)
        self.room_1.remove_song(self.song_1)
        self.assertNotIn(self.song_1, self.room_1.song_list)
    
    def test_is_there_room_available__yes(self):
        self.room_1.check_in_guest(self.guest_1)
        self.assertEqual(True, self.room_1.is_there_room_available())

    def test_is_there_room_available__no(self):
        self.room_1.check_in_guest(self.guest_1)
        self.room_1.check_in_guest(self.guest_2)
        self.room_1.check_in_guest(self.guest_3)
        self.assertEqual(False, self.room_1.is_there_room_available())  

    def test_can_guest_pay_entry_fee__yes(self):
        has_money = self.room_1.guest_pays_entry_fee(self.guest_1)
        self.assertEqual(True, has_money)

    def test_can_guest_pay_entry_fee__no(self):
        has_money = self.room_1.guest_pays_entry_fee(self.guest_3)
        self.assertEqual(False, has_money)

    def test_play_my_favourite_song__yes(self):
        self.room_1.check_in_guest(self.guest_1)
        self.room_1.add_song(self.song_1)
        favourite = self.room_1.play_my_favourite_song(self.guest_1)
        self.assertEqual("Whoo!", favourite)

    def test_play_my_favourite_song__no(self):
        self.room_1.check_in_guest(self.guest_1)
        self.room_1.add_song(self.song_2)
        favourite = self.room_1.play_my_favourite_song(self.guest_1)
        self.assertEqual("That's not my jam!", favourite)

# ........


  