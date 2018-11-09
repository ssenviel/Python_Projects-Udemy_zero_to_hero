import enum
import random


class CardFaceState(enum.Enum):
    DOWN = 0
    UP = 1


class Value(enum.IntEnum):
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX  = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 10
    QUEEN = 10
    KING = 10


class Suit(enum.Enum):
    HEART = enum.auto
    SPADE = enum.auto
    DIAMOND = enum.auto
    CLUB = enum.auto


# card class
class Card():

                # default to ace of hearts
    def __init__(self, Value=Value.ACE, suit=Suit.HEART):
        self.__value = Value
        self.__suit = suit
        self.__face_state = CardFaceState.DOWN

    def set_face_state(self, new_state):
        self.__face_state = new_state

    def get_card_face_state(self):
        return self.__face_state

    def get_card_value(self):
        return self.__value

    def get_card_suit(self):
        return self.__suit

# end of the card class


