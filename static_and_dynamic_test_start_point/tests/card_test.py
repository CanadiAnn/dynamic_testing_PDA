import unittest
from src.card import Card


class CardTest(unittest.TestCase):
    
    def setUp(self):
        self.card1 = Card('hearts', 1)
        self.card2 = Card('spades', 14)
        self.card3 = Card('diamond', 6)
        self.card4 = Card('clubs', 3)
    
    # def test_card_has_suit(self):
    #     self.assertEqual('hearts', self.card1.suit)
    #     self.assertEqual('spades', self.card2.suit)

    # def test_card_has_value(self):
    #     self.assertEqual(1, self.card1.value)
    #     self.assertEqual(14, self.card2.value)