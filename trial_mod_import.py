'''
Created on Mar 7, 2019

@author: senvi
'''


from Card import Card, CardFaceState, CardFaceType, SuitType


if __name__ == '__main__':
    myCard = Card(cardFaceType=CardFaceType.ACE, suit=SuitType.HEART, face=CardFaceState.UP)
    myCard.draw_card()
    
    