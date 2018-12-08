'''
Created on Dec 7, 2018

@author: senvi
'''
import unittest
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
        pass
    
    def test_Winner_playerBust(self):
        # dealer has lower hand, player busts
        pass
    
    def test_winner_dealerBust(self):
        # player has lower hand, dealer busts
        pass
    
    def test_winner_playerBlackjack(self):
        # player has a blackjack
        pass
    
    def test_winner_dealerBlackJack(self):
        # dealer has blackjack
        pass
    
    def test_winner_player(self):
        #player has better hand < blackJack
        pass
    
    def test_winner_dealer(self):
        #dealer has better hand < blackJack
        pass
    
    
                                
                                    
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()