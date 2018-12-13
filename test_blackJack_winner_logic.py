'''
Created on Dec 7, 2018

@author: senvi
'''
import unittest
import blackjack
from blackjack import Player, Dealer, Card, CardFaceState, CardFaceType, SuitType 


class TestBlackWinnerLogic(unittest.TestCase):


    def setUp(self):
        self.testPlayer = Player()
        self.testDealer = Dealer()
        self.winner = None

    def tearDown(self):
        del self.testPlayer
        del self.testDealer

    def test_Winnner_push(self):
        #  both player and dealer have Ace and Face card
        self.testPlayer.recieve_card( Card(CardFaceType.ACE, SuitType.CLUB, CardFaceState.UP) )
        self.testPlayer.recieve_card( Card(CardFaceType.JACK, SuitType.HEART, CardFaceState.UP) )
        self.testDealer.recieve_card( Card(CardFaceType.KING, SuitType.DIAMOND, CardFaceState.UP) )
        self.testDealer.recieve_card( Card(CardFaceType.ACE, SuitType.SPADE, CardFaceState.UP ) )
        
        self.winner = blackjack.determine_blackjack_winner(self.testPlayer, self.testDealer)
        self.assertTrue( (self.winner is None), "there should be no winner here")
        
    
    def test_Winner_playerBust(self):
        # dealer has lower hand, player busts
        self.testPlayer.recieve_card( Card(CardFaceType.KING, SuitType.CLUB, CardFaceState.UP))
        self.testPlayer.recieve_card( Card(CardFaceType.JACK, SuitType.HEART, CardFaceState.UP))
        self.testPlayer.recieve_card( Card(CardFaceType.FIVE, SuitType.DIAMOND, CardFaceState.UP))
        
        self.testDealer.recieve_card( Card(CardFaceType.KING, SuitType.DIAMOND, CardFaceState.UP))
        self.testDealer.recieve_card( Card(CardFaceType.ACE, SuitType.SPADE, CardFaceState.UP ))
        
        self.winner = blackjack.determine_blackjack_winner(self.testPlayer, self.testDealer)
        self.assertIsInstance(self.winner, Dealer, "Dealer should have won")
        
        
    
    def test_winner_dealerBust(self):
#         player has lower hand, dealer busts
        self.testPlayer.recieve_card( Card(CardFaceType.SIX, SuitType.CLUB, CardFaceState.UP) )
        self.testPlayer.recieve_card( Card(CardFaceType.JACK, SuitType.HEART, CardFaceState.UP) )
        
        self.testDealer.recieve_card( Card(CardFaceType.KING, SuitType.DIAMOND, CardFaceState.UP))
        self.testDealer.recieve_card( Card(CardFaceType.TEN, SuitType.DIAMOND, CardFaceState.UP))
        self.testDealer.recieve_card( Card(CardFaceType.ACE, SuitType.SPADE, CardFaceState.UP ))
        self.testDealer.recieve_card( Card(CardFaceType.FOUR, SuitType.DIAMOND, CardFaceState.UP))
        
        self.winner = blackjack.determine_blackjack_winner(self.testPlayer, self.testDealer)
        self.assertIsInstance(self.winner, Player, "Player should have won")
           
    
    def test_winner_playerBlackjack(self):
        # player has a blackjack
        self.testPlayer.recieve_card( Card(CardFaceType.ACE, SuitType.CLUB, CardFaceState.UP) )
        self.testPlayer.recieve_card( Card(CardFaceType.JACK, SuitType.HEART, CardFaceState.UP) )
        self.testDealer.recieve_card( Card(CardFaceType.KING, SuitType.DIAMOND, CardFaceState.UP))
        self.testDealer.recieve_card( Card(CardFaceType.NINE, SuitType.SPADE, CardFaceState.UP ))
        
        self.winner = blackjack.determine_blackjack_winner(self.testPlayer, self.testDealer)
        self.assertIsInstance(self.winner, Player, "Player Should have won")
        
        
        
    
    def test_winner_dealerBlackJack(self):
        # dealer has blackjack
        self.testPlayer.recieve_card( Card(CardFaceType.SEVEN, SuitType.CLUB, CardFaceState.UP) )
        self.testPlayer.recieve_card( Card(CardFaceType.JACK, SuitType.HEART, CardFaceState.UP) )
        self.testDealer.recieve_card( Card(CardFaceType.KING, SuitType.DIAMOND, CardFaceState.UP))
        self.testDealer.recieve_card( Card(CardFaceType.ACE, SuitType.SPADE, CardFaceState.UP ))
        
        self.winner = blackjack.determine_blackjack_winner(self.testPlayer, self.testDealer)
        self.assertIsInstance(self.winner, Dealer, "Dealer should have won")
        
        
            
    def test_winner_player(self):
        #player has better hand < blackJack
        self.testPlayer.recieve_card( Card(CardFaceType.NINE, SuitType.CLUB, CardFaceState.UP) )
        self.testPlayer.recieve_card( Card(CardFaceType.EIGHT, SuitType.HEART, CardFaceState.UP) )
        self.testDealer.recieve_card( Card(CardFaceType.KING, SuitType.DIAMOND, CardFaceState.UP))
        self.testDealer.recieve_card( Card(CardFaceType.THREE, SuitType.SPADE, CardFaceState.UP ))
        
        self.winner = blackjack.determine_blackjack_winner(self.testPlayer, self.testDealer)
        self.assertIsInstance(self.winner, Player, "Player should have won")
        
        
    
    def test_winner_dealer(self):
        #dealer has better hand < blackJack
        self.testPlayer.recieve_card( Card(CardFaceType.TWO, SuitType.CLUB, CardFaceState.UP) )
        self.testPlayer.recieve_card( Card(CardFaceType.NINE, SuitType.HEART, CardFaceState.UP) )
        self.testDealer.recieve_card( Card(CardFaceType.KING, SuitType.DIAMOND, CardFaceState.UP))
        self.testDealer.recieve_card( Card(CardFaceType.SIX, SuitType.SPADE, CardFaceState.UP ))
        
        self.winner = blackjack.determine_blackjack_winner(self.testPlayer, self.testDealer)
        self.assertIsInstance(self.winner, Dealer, "Dealer should have won")
             
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()