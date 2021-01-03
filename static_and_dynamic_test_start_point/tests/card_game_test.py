import unittest

from src.card import Card
from src.card_game import CardGame

class CardGameTest(unittest.TestCase):
    
    def test_checkforace(self):
        self.card = Card('hearts', 1)
        self.card1 = Card('hearts', 2)
        self.card_game = CardGame()
        return_value = self.card_game.checkforace(self.card)
        self.assertEqual(True, return_value)

    def test_highest_card(self):
        self.card1 = Card('hearts', 2)
        self.card2 = Card('spades', 12)
        self.card_game = CardGame() 
        return_value = self.card_game.highest_card(self.card1, self.card2)
        self.assertEqual(self.card2, return_value)

    def test_cards_total(self):
        self.cards = [
            Card('hearts', 2),
            Card('spades', 12),
            Card('diamond', 6),
            Card('clubs', 3)
            ]
        self.card_game = CardGame()
        return_value = self.card_game.cards_total(self.cards)
        self.assertEqual("You have a total of 23", return_value)