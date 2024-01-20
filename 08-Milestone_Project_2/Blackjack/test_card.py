"""
Test for Card class
"""

import unittest
from game_package.game_module import Card

class TestCard(unittest.TestCase):

   def test_card_str(self):
      test_card = Card("Hearts", "Three")
      card_str = test_card.__str__()
      self.assertEqual(card_str, "Three of Hearts")

   def test_card_rep(self):
      test_card = Card('Diamonds', 'Ace')
      card_repr = test_card.__repr__()
      self.assertEqual(card_repr, "Card('Diamonds', 'Ace')")

if __name__=='__main__':
   unittest.main()