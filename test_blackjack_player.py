import unittest
from blackjack import Player, Card, CardType, SuitType

verbosity_level=2


class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.testPlayer = Player()
               

    def tearDown(self):
        del self.testPlayer       

    
    def test_card_draw(self):
       # print("testing card draw")
        self.testPlayer.recieve_card( Card(CardType.ACE, SuitType.CLUB) )
        self.testPlayer.recieve_card( Card(CardType.ACE, SuitType.HEART) )
        testHand = self.testPlayer.get_hand()
        self.assertEqual(len(testHand), 2, "expected different number of cards")
        

    def test_hand_value_all_aces(self):
        self.testPlayer.recieve_card( Card(CardType.ACE, SuitType.CLUB) )
        self.testPlayer.recieve_card( Card(CardType.ACE, SuitType.HEART) )
        self.testPlayer.recieve_card( Card(CardType.ACE, SuitType.SPADE) )
        self.testPlayer.recieve_card( Card(CardType.ACE, SuitType.CLUB) )
     
        
        self.assertEqual(self.testPlayer.get_hand_value(), 14, "failed case 1")

    def test_hand_value_aces_and_twos(self):
        # this will test against having all aces and all twos
        self.testPlayer.recieve_card( Card(CardType.ACE, SuitType.CLUB) )
        self.testPlayer.recieve_card( Card(CardType.ACE, SuitType.HEART) )
        self.testPlayer.recieve_card( Card(CardType.ACE, SuitType.SPADE) )
        self.testPlayer.recieve_card( Card(CardType.ACE, SuitType.CLUB) )
     
        
        self.testPlayer.recieve_card( Card(CardType.TWO, SuitType.CLUB) )
        self.testPlayer.recieve_card( Card(CardType.TWO, SuitType.HEART) )
        self.testPlayer.recieve_card( Card(CardType.TWO, SuitType.SPADE) )
        self.testPlayer.recieve_card( Card(CardType.TWO, SuitType.CLUB) )
     
        self.assertEqual( len(self.testPlayer.get_hand() ) , 8, "incorrect number of cards")
     
        self.assertEqual(self.testPlayer.get_hand_value(), 12, "failed case2 -- all twos and aces")

suite = unittest.TestLoader().loadTestsFromTestCase(TestPlayer)
unittest.TextTestRunner(verbosity=verbosity_level).run(suite)
