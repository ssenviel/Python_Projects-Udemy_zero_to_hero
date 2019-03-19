'''
Created on Mar 7, 2019

@author: senvi
'''
import enum


#club_image = u"\u2663"
#diamond_image = u"\u2666"
#heart_image = u"\u2665"
#spade_image = u"\u2660"
class CardFaceState(enum.Enum):
    """enum type for the state of a card faceS"""
    DOWN = 0
    UP = 1



class CardFaceType(enum.Enum):
    """enum type for the types of card faces. ACE thru KING """
    ACE = enum.auto()
    TWO = enum.auto()
    THREE = enum.auto()
    FOUR = enum.auto()
    FIVE = enum.auto()
    SIX = enum.auto()
    SEVEN = enum.auto()
    EIGHT = enum.auto()
    NINE = enum.auto()
    TEN = enum.auto()
    JACK = enum.auto()
    QUEEN = enum.auto()
    KING = enum.auto()



class SuitType(enum.Enum):
    """ enum type for the suits of a card deck """
    HEART = enum.auto()
    SPADE = enum.auto()
    DIAMOND = enum.auto()
    CLUB = enum.auto()






# card class
class Card():
    """
    class for the Card of a Deck.
    contains a value dictionary and
    Suit icon dictionary for the use of handling displaying card information
    """
    __cardValueDict = {CardFaceType.ACE:(11, 'A'),
                       CardFaceType.TWO:(2, '2'),
                       CardFaceType.THREE:(3, '3'),
                       CardFaceType.FOUR:(4, '4'),
                       CardFaceType.FIVE:(5, '5'),
                       CardFaceType.SIX:(6, '6'),
                       CardFaceType.SEVEN:(7, '7'),
                       CardFaceType.EIGHT:(8, '8'),
                       CardFaceType.NINE:(9, '9'),
                       CardFaceType.TEN:(10, '10'),
                       CardFaceType.JACK:(10, 'J'),
                       CardFaceType.QUEEN:(10, 'Q'),
                       CardFaceType.KING:(10, 'K')}

    __suitIconDict = {SuitType.HEART: u"\u2665",
                      SuitType.SPADE:u"\u2660",
                      SuitType.DIAMOND:u"\u2666",
                      SuitType.CLUB:u"\u2663"}


    def __init__(self, cardFaceType=CardFaceType.ACE, suit=SuitType.HEART, face=CardFaceState.UP):
        self.__type = cardFaceType
        self.__value = self.__cardValueDict[self.__type][0]
        self.__value_icon = self.__cardValueDict[self.__type][1]
        self.__suit = suit
        self.__suit_icon = self.__suitIconDict[self.__suit]
        self.__face_state = face

    def set_face_state(self, new_state):
        """
        set the face state of a card. takes a CardFaceStateEnum
        """
        self.__face_state = new_state

    def get_card_face_state(self):
        """ returns the cards face state of a card in the form of a CardsFaceStateEnum object"""
        return self.__face_state

    def get_card_value(self):
        """ get the numerical value of a card """
        return self.__value

    def get_card_suit(self):
        """ get the card suit in the form of a SuitType enum type"""
        return self.__suit

    def get_card_type(self):
        """get the card type in the form of a CardFaceType enum"""
        return self.__type

    def draw_card(self):
        """ draw a card on the console """
        if CardFaceState.UP == self.__face_state:
            print("------------")
            print(f"|{self.__suit_icon}        {self.__suit_icon}|")
            print(f"|          |")
            print(f"|          |")
            print(f"|    {self.__value_icon}     |")
            print(f"|          |")
            print(f"|          |")
            print(f"|{self.__suit_icon}        {self.__suit_icon}|")
            print("------------")
        else:
            print("------------")
            print("|##########|")
            print("|##########|")
            print("|##########|")
            print("|##########|")
            print("|##########|")
            print("|##########|")
            print("|##########|")
            print("------------")

    def get_suit_icon(self):
        """ return the suit icon """
        return self.__suit_icon

    def get_value_icon(self):
        """ return the icon for the value of a card """
        return self.__value_icon





