import unittest
#from blackjack import Card, Suit, Value, CardFaceState
#import blackjack
from blackjack import SuitType, CardType, CardFaceState, Card

verbosity_level=2;

class TestCard(unittest.TestCase):

    def setUp(self):
        print("running setup")
        self.myTestCard = Card(CardType.EIGHT, SuitType.SPADE)

    def tearDown(self):
        print("performing teardown")
        del self.myTestCard


        # check that what was in the setup is still there
    def test_initial_card_state(self):
        self.assertEqual(self.myTestCard.get_card_suit(), SuitType.SPADE, "testing the suit")
        self.assertEqual(self.myTestCard.get_card_value(), 8, "testing the value")
        self.assertEqual(self.myTestCard.get_card_face_state(), CardFaceState.DOWN, "testing the card face state")

    def test_card_state_change(self):
        self.myTestCard.set_face_state(CardFaceState.UP)
        self.assertEqual(self.myTestCard.get_card_face_state(), CardFaceState.UP, "card face state is not as expected")





#if __name__ == '__main__':
#    unittest.main()
suite = unittest.TestLoader().loadTestsFromTestCase(TestCard)
unittest.TextTestRunner(verbosity=verbosity_level).run(suite)