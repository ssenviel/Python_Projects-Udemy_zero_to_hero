import unittest
#from blackjack import Card, Suit, Value, CardFaceState
#import blackjack
from blackjack import Suit, Value, CardFaceState, Card

class TestCard(unittest.TestCase):

    def setUp(self):
        self.myTestCard = Card(Value.EIGHT, Suit.SPADE)

    def tearDown(self):
        del self.myTestCard

        # check that what was in the setup is still there
    def test_initial_card_state(self):
        self.assertEqual(self.myTestCard.get_card_suit(), Suit.SPADE, "testing the suit")
        self.assertEqual(self.myTestCard.get_card_value(), Value.NINE, "testing the value")
        self.assertEqual(self.myTestCard.get_card_face_state(), CardFaceState.DOWN, "testing the card face state")




if __name__ == '__main__':
    unittest.main()
