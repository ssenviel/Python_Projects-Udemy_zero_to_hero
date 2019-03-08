import unittest

from blackjack import Deck, Card


verbosity_level = 2;

class TestDeck(unittest.TestCase):
    expected_deck_size = 52

    def setUp(self):
        self.myTestDeck = Deck()
        self.myTestDeck.generate_deck_cards()

    def tearDown(self):
        del self.myTestDeck;

    def test_deck_Randomness(self):
        tempDeckCards = self.myTestDeck.cards().copy();
        self.myTestDeck.shuffle_cards();
        self.assertNotEqual(tempDeckCards, self.myTestDeck.cards(), "Deck has not been shuffled.")

    def test_deck_size(self):
        self.assertEqual(len(self.myTestDeck.cards()), self.expected_deck_size, "Deck is not the correct size!!")

    def test_deal_card(self):
        tempCard = self.myTestDeck.deal_card()
        self.expected_deck_size -= 1
        self.assertEqual(len(self.myTestDeck.cards()), self.expected_deck_size, "ERROR deck size is not correct")
        self.assertTrue(isinstance(tempCard, Card))






# load the tests
suite_of_tests = unittest.TestLoader().loadTestsFromTestCase(TestDeck)

# run the tests
unittest.TextTestRunner(verbosity=verbosity_level).run(suite_of_tests)
