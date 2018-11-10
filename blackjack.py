import enum
import random


class CardFaceState(enum.Enum):
    DOWN = 0
    UP = 1



class CardType(enum.Enum):
    ACE = enum.auto()
    TWO = enum.auto()
    THREE = enum.auto()
    FOUR =  enum.auto()
    FIVE =  enum.auto()
    SIX  =  enum.auto()
    SEVEN =  enum.auto()
    EIGHT =  enum.auto()
    NINE =  enum.auto()
    TEN =  enum.auto()
    JACK =  enum.auto()
    QUEEN =  enum.auto()
    KING =  enum.auto()



class Suit(enum.Enum):
    HEART = enum.auto()
    SPADE = enum.auto()
    DIAMOND = enum.auto()
    CLUB = enum.auto()


# card class
class Card():

    ValueDict = {CardType.ACE:1,
                 CardType.TWO:2,
                 CardType.THREE:3,
                 CardType.FOUR:4,
                 CardType.FIVE:5,
                 CardType.SIX:6,
                 CardType.SEVEN:7,
                 CardType.EIGHT:8,
                 CardType.NINE:9,
                 CardType.TEN:10,
                 CardType.JACK:10,
                 CardType.QUEEN:10,
                 CardType.KING:10}

                # default to ace of hearts
    def __init__(self, type=CardType.ACE, suit=Suit.HEART):
        self.__type = type
        self.__value = self.ValueDict[self.__type]
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

# deck class
class Deck():


    def __init__(self):
        self.__cards = list()

    # this will populate the set of cards that make up the deck
    def generate_deck_cards(self):
      for this_suit in Suit:
          for this_value in CardType:
             # print(f"{this_suit} of {this_value}")
              tempCard = Card(this_value, this_suit)
              self.__cards.append(tempCard)

      # this will shuffle the cards that make up the deck
    def shuffle_cards(self):
        random.shuffle(self.__cards)

    # return the list of cards
    def cards(self):
        return self.__cards

    # pops a card off the deck and returns the card
    def deal_card(self):
        return self.__cards.pop()


# end of deck class


