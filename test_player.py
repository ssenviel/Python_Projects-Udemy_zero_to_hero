import unittest
from blackjack import Player, Card, Deck

verbosity_level=2


class TestPlayer(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass


    def test_draw_card(self):
        pass


    def test_hand_value(self):
        pass





suite = unittest.TestLoader().loadTestsFromTestCase(TestPlayer)
unittest.TextTestRunner(verbosity_level).run(suite)
