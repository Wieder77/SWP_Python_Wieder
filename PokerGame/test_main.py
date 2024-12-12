import unittest
from main import *

class PokerUnittest(unittest.TestCase):
    def test_royalflush(self):
        cards = [36, 12, 8, 48, 24]
        self.assertTrue(royalflush(cards))
        cards = [36, 12, 8, 48, 25]
        self.assertFalse(royalflush(cards))

    def test_straight_flush(self):
        cards = [11, 23, 7, 47, 35]
        self.assertTrue(straight_flush(cards))
        cards = [11, 23, 7, 47, 45]
        self.assertFalse(straight_flush(cards))
if __name__ == '__main__':
    unittest.main()
