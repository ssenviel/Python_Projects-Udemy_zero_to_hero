'''
Created on Dec 7, 2018

@author: senvi
'''
import unittest
import blackjack
from blackjack import Player, Dealer, Card, CardFaceState, CardType, SuitType 


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
        self.testPlayer.recieve_card( Card(CardType.ACE, SuitType.CLUB, CardFaceState.UP) )
        self.testPlayer.recieve_card( Card(CardType.JACK, SuitType.HEART, CardFaceState.UP) )
        self.testDealer.recieve_card( Card(CardType.KING, SuitType.DIAMOND, CardFaceState.UP) )
        self.testDealer.recieve_card( Card(CardType.ACE, SuitType.SPADE, CardFaceState.UP ) )
        
        self.winner = blackjack.determine_blackjack_winner(self.testPlayer, self.testDealer)
        self.assertTrue( (self.winner is None), "there should be no winner here")
        
    
    def test_Winner_playerBust(self):
        # dealer has lower hand, player busts
        self.testPlayer.recieve_card( Card(CardType.KING, SuitType.CLUB, CardFaceState.UP))
        self.testPlayer.recieve_card( Card(CardType.JACK, SuitType.HEART, CardFaceState.UP))
        self.testPlayer.recieve_card( Card(CardType.FIVE, SuitType.DIAMOND, CardFaceState.UP))
        
        self.testDealer.recieve_card( Card(CardType.KING, SuitType.DIAMOND, CardFaceState.UP))
        self.testDealer.recieve_card( Card(CardType.ACE, SuitType.SPADE, CardFaceState.UP ))
        
        self.winner = blackjack.determine_blackjack_winner(self.testPlayer, self.testDealer)
        self.assertIsInstance(self.winner, Dealer, "there should be no winner here")
        
        
    
    def test_winner_dealerBust(self):
#         player has lower hand, dealer busts
        self.testPlayer.recieve_card( Card(CardType.SIX, SuitType.CLUB, CardFaceState.UP) )
        self.testPlayer.recieve_card( Card(CardType.JACK, SuitType.HEART, CardFaceState.UP) )
        
        self.testDealer.recieve_card( Card(CardType.KING, SuitType.DIAMOND, CardFaceState.UP))
        self.testDealer.recieve_card( Card(CardType.TEN, SuitType.DIAMOND, CardFaceState.UP))
        self.testDealer.recieve_card( Card(CardType.ACE, SuitType.SPADE, CardFaceState.UP ))
        self.testDealer.recieve_card( Card(CardType.FOUR, SuitType.DIAMOND, CardFaceState.UP))
        
        self.winner = blackjack.determine_blackjack_winner(self.testPlayer, self.testDealer)
        self.assertIsInstance(self.winner, Player, "there should be no winner here")
           
    
    def test_winner_playerBlackjack(self):
        # player has a blackjack
        self.testPlayer.recieve_card( Card(CardType.ACE, SuitType.CLUB, CardFaceState.UP) )
        self.testPlayer.recieve_card( Card(CardType.JACK, SuitType.HEART, CardFaceState.UP) )
        self.testDealer.recieve_card( Card(CardType.KING, SuitType.DIAMOND, CardFaceState.UP))
        self.testDealer.recieve_card( Card(CardType.NINE, SuitType.SPADE, CardFaceState.UP ))
        
        self.winner = blackjack.determine_blackjack_winner(self.testPlayer, self.testDealer)
        self.assertIsInstance(self.winner, Player, "there should be no winner here")
        
        
        
    
    def test_winner_dealerBlackJack(self):
        # dealer has blackjack
        self.testPlayer.recieve_card( Card(CardType.SEVEN, SuitType.CLUB, CardFaceState.UP) )
        self.testPlayer.recieve_card( Card(CardType.JACK, SuitType.HEART, CardFaceState.UP) )
        self.testDealer.recieve_card( Card(CardType.KING, SuitType.DIAMOND, CardFaceState.UP))
        self.testDealer.recieve_card( Card(CardType.ACE, SuitType.SPADE, CardFaceState.UP ))
        
        self.winner = blackjack.determine_blackjack_winner(self.testPlayer, self.testDealer)
        self.assertIsInstance(self.winner, Dealer, "there should be no winner here")
        
        
            
    def test_winner_player(self):
        #player has better hand < blackJack
        #self.testPlayer.recieve_card( Card(CardType.ACE, SuitType.CLUB, CardFaceState.UP) )
        #self.testPlayer.recieve_card( Card(CardType.JACK, SuitType.HEART, CardFaceState.UP) )
        #self.testDealer.recieve_card( Card(CardType.KING, SuitType.DIAMOND, CardFaceState.UP))
        #self.testDealer.recieve_card( Card(CardType.ACE, SuitType.SPADE, CardFaceState.UP ))
        
        #self.winner = determine_blackjack_winner(self.testPlayer, self.testDealer)
        #self.assertIsInstance(self.winner, Player, "there should be no winner here")
        
        pass
    
    def test_winner_dealer(self):
        #dealer has better hand < blackJack
       # self.testPlayer.recieve_card( Card(CardType.ACE, SuitType.CLUB, CardFaceState.UP) )
       # self.testPlayer.recieve_card( Card(CardType.JACK, SuitType.HEART, CardFaceState.UP) )
       # self.testDealer.recieve_card( Card(CardType.KING, SuitType.DIAMOND, CardFaceState.UP))
       # self.testDealer.recieve_card( Card(CardType.ACE, SuitType.SPADE, CardFaceState.UP ))
        
        #self.winner = determine_blackjack_winner(self.testPlayer, self.testDealer)
        #self.assertIsInstance(self.winner, None, "there should be no winner here")
        
        pass
    
     
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()