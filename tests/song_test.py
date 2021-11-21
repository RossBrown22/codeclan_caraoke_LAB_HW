import unittest
from classes.song import Song

class TestSong (unittest.TestCase):
    def setUp(self):
        self.song_1 = Song("Crazy Train", "Ozzy Osbourne", 3)
        self.song_2 = Song("Future Days", "Pearl Jam", 4)
        self.song_3 = Song("Creep", "Radiohead", 4)
