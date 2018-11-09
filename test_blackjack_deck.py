import unittest
from blackjack import Deck, Card

verbosity_level = 2;

class TestDeck(unittest.TestCase):

    def setUp(self):
        self.myTestDeck = Deck()
        self.myTestDeck.generate_deck_cards()

    def tearDown(self):
        del self.myTestDeck;

    def test_deck_Randomness(self):
        tempDeck = self.myTestDeck
        self.myTestDeck.shuffle_cards();
        self.assertNotEqual(tempDeck, self.myTestDeck, "Deck has not been shuffled.")

    def test_deck_size(self):
        self.assertEqual(len(self.myTestDeck.cards()), 52, "Deck is not the correct size!!")









# load the tests
suite_of_tests = unittest.TestLoader().loadTestsFromTestCase(TestDeck)

# run the tests
unittest.TextTestRunner(verbosity=verbosity_level).run(suite_of_tests)
