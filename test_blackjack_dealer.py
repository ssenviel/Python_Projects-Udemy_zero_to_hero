'''
Created on Nov 27, 2018

@author: senvi
'''
import unittest
from blackjack import Dealer, Card, CardFaceType, SuitType, CardFaceState

class TestDealer(unittest.TestCase):

    def setUp(self):
        self.testDealer = Dealer()
        
    
    def tearDown(self):
        del self.testDealer

 
    def test_hittable_case1(self):
        # draw some cards , face up, value > 13 < 17
        # assert on return of hittable status
        self.testDealer.recieve_card( Card(CardFaceType.KING, SuitType.CLUB) )
        self.testDealer.recieve_card( Card(CardFaceType.FIVE, SuitType.DIAMOND) )
        self.assertTrue(self.testDealer.should_hit(True), "dealer should have hit")
    
    def test_hittable_case2(self):
        # draw some cards , face up, one ace,  value > 13 < 17
        # assert on return of hittable status
        self.testDealer.recieve_card( Card(CardFaceType.ACE, SuitType.CLUB) )
        self.testDealer.recieve_card( Card(CardFaceType.THREE, SuitType.HEART) )
        self.assertTrue(self.testDealer.should_hit(True), "dealer should have hit")
        
    def test_hittable_case3(self):
        # draw some cards, face up with a value greater than 17 
        self.testDealer.recieve_card( Card(CardFaceType.KING, SuitType.CLUB) )
        self.testDealer.recieve_card( Card(CardFaceType.FIVE, SuitType.CLUB) )
        self.testDealer.recieve_card( Card(CardFaceType.FIVE, SuitType.HEART) )
        self.assertFalse(self.testDealer.should_hit(True), "dealer sould have stayed")
    
    def test_hittable_case4(self):
        self.testDealer.recieve_card( Card(CardFaceType.ACE, SuitType.CLUB) )
        self.testDealer.recieve_card( Card(CardFaceType.ACE, SuitType.SPADE) )
        self.testDealer.recieve_card( Card(CardFaceType.SEVEN, SuitType.HEART) )    
        # draw cards, at least 2 aces
        self.assertFalse(self.testDealer.should_hit(True), "dealer should have stayed")
    
    def test_visable_value_case1(self):
        self.testDealer.recieve_card( Card(CardFaceType.EIGHT, SuitType.SPADE) )
        self.testDealer.recieve_card( Card(CardFaceType.JACK, SuitType.HEART, CardFaceState.DOWN ))
        visible_value = self.testDealer.get_visible_hand_value()
        self.assertEqual(visible_value, 8, "error on visible hand value")
        self.testDealer.show_card_faces()
        visible_value = self.testDealer.get_visible_hand_value()
        self.assertEqual(visible_value, 18, "error in visible hand value after turning cards")
        
    def test_visable_value_case2(self):
        self.testDealer.recieve_card( Card(CardFaceType.EIGHT, SuitType.SPADE) )
        self.testDealer.recieve_card( Card(CardFaceType.ACE, SuitType.HEART, CardFaceState.DOWN) )
        visible_value = self.testDealer.get_visible_hand_value()
        self.assertEqual(visible_value, 8, "error on visible hand value")
        self.testDealer.show_card_faces()
        visible_value = self.testDealer.get_visible_hand_value()
        self.assertEqual(visible_value, 19, "error in visible hand value after turning cards")



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()