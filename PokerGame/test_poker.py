import unittest
from main import royalflush, straight_flush, flush, straight, has_pair

class TestPokerHandEvaluation(unittest.TestCase):

    def test_royalflush(self):
        # Royal Flush
        cards = [36, 12, 8, 48, 24]
        self.assertTrue(royalflush(cards))

        # Nicht Royal Flush
        cards = [36, 12, 8, 48, 25]
        self.assertFalse(royalflush(cards))

    def test_straight_flush(self):
        # Straight Flush
        cards = [11, 23, 7, 47, 35]
        self.assertTrue(straight_flush(cards))

        # Nicht Straight Flush
        cards = [11, 23, 7, 47, 45]
        self.assertFalse(straight_flush(cards))

    def test_flush(self):
        # Flush
        cards = [30, 2, 18, 42, 10]
        self.assertTrue(flush(cards))

        # Nicht Flush
        cards = [30, 2, 18, 42, 11]
        self.assertFalse(flush(cards))

    def test_straight(self):
        # Straight
        cards = [9, 6, 10, 7, 21]
        self.assertTrue(straight(cards))

        # Nicht Straight
        cards = [9, 6, 10, 7, 31]
        self.assertFalse(straight(cards))

    def test_four_of_a_kind(self):
        # Vier Gleiche
        cards = [1, 14, 27, 40, 7]  # Vier Karten mit gleichem Wert
        self.assertEqual(has_pair(cards), "four")

        # Nicht Vier Gleiche
        cards = [1, 14, 7, 40, 37]
        self.assertNotEqual(has_pair(cards), "four")

    def test_full_house(self):
        # Full House
        cards = [24, 47, 11, 34, 37]  # Beispiel: 3 Damen, 2 Könige
        self.assertEqual(has_pair(cards), "fullHouse")

        # Nicht Full House
        cards = [24, 47, 37, 34, 12]
        self.assertNotEqual(has_pair(cards), "fullHouse")

    def test_three_of_a_kind(self):
        # Drei Gleiche
        cards = [29, 42, 3, 21, 19]
        self.assertEqual(has_pair(cards), "three")

        # Nicht Drei Gleiche
        cards = [29, 49, 19, 3, 9]
        self.assertNotEqual(has_pair(cards), "three")

    def test_two_pair(self):
        # Zwei Paare
        cards = [39, 7, 46, 0, 12]
        self.assertEqual(has_pair(cards), "twoPair")

        # Nicht Zwei Paare
        cards = [39, 7, 46, 31, 12]
        self.assertNotEqual(has_pair(cards), "twoPair")

    def test_pair(self):
        # Ein Paar
        cards = [46, 37, 33, 49, 40]
        self.assertEqual(has_pair(cards), "pair")

        # Kein Paar
        cards = [46, 37, 29, 49, 40]
        self.assertNotEqual(has_pair(cards), "pair")


if __name__ == '__main__':
    unittest.main()
