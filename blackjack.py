import enum
import random


#club_image = u"\u2663"
#diamond_image = u"\u2666"
#heart_image = u"\u2665"
#spade_image = u"\u2660"


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



class SuitType(enum.Enum):
    HEART = enum.auto()
    SPADE = enum.auto()
    DIAMOND = enum.auto()
    CLUB = enum.auto()


# card class
class Card():

    __cardValueDict = {CardType.ACE:(11, 'A'),
                       CardType.TWO:(2, '2'),
                       CardType.THREE:(3, '3'),
                       CardType.FOUR:(4, '4'),
                       CardType.FIVE:(5, '5'),
                       CardType.SIX:(6, '6'),
                       CardType.SEVEN:(7, '7'),
                       CardType.EIGHT:(8, '8'),
                       CardType.NINE:(9, '9'),
                       CardType.TEN:(10, '10'),
                       CardType.JACK:(10, 'J'),
                       CardType.QUEEN:(10, 'Q'),
                       CardType.KING:(10, 'K')}

    __suitIconDict = {SuitType.HEART: u"\u2665",
                      SuitType.SPADE:u"\u2660",
                      SuitType.DIAMOND:u"\u2666",
                      SuitType.CLUB:u"\u2663"}



                # default to ace of hearts
        # TOOD:  make sure we are indexing properly to collect all members from the dictionaries
    def __init__(self, type=CardType.ACE, suit=SuitType.HEART):
        self.__type = type
        self.__value = self.__cardValueDict[self.__type][0]
        self.__value_icon = self.__cardValueDict[self.__type][1]
        self.__suit = suit
        self.__suit_icon = self.__suitIconDict[self.__suit]
        self.__face_state = CardFaceState.DOWN

    def set_face_state(self, new_state):
        self.__face_state = new_state

    def get_card_face_state(self):
        return self.__face_state

    def get_card_value(self):
        return self.__value

    def get_card_suit(self):
        return self.__suit

    def get_card_type(self):
        return self.__type

    def draw_card(self):
        print("------------")
        print(f"|{self.__suit_icon}        {self.__suit_icon}|")
        print(f"|          |")
        print(f"|          |")
        print(f"|    {self.__value_icon}     |")
        print(f"|          |")
        print(f"|          |")
        print(f"|{self.__suit_icon}        {self.__suit_icon}|")
        print("------------")

    def get_suit_icon(self):
        return self.__suit_icon


# end of the card class

# deck class
class Deck():


    def __init__(self):
        self.__cards = list()

    # this will populate the set of cards that make up the deck
    def generate_deck_cards(self):
      for this_suit in SuitType:
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


# player class
class Player():
    __hand = list()
    __hand_value=0;

    def __init__(self):
        self.hand.clear()
        self.__hand_value = 0;
        
    # add a card to the players hand,
    def recieve_card(self, new_card):
        self.__hand.append(new_card)
      
         
     # return the value of a player's hand
    def get_hand_value(self):
        return self.__calc_hand_value()
    
    
    # draw a players hand
    def display_hand(self):
        pass;
  
        # print the top line
                 

        #print the second line: | suit icon , spaces, suit icon, |
      
        
        
        
        # print the third and 4th lines :  | , spaces, |


        # print the 5th line:  | , spaces, card type, spaces, |
        
        # print the 6th, 7th lines:  |, spaces, |
        
        #print the 8th line:| suit icon , spaces, suit icon, |
        
        
            
         # print the last line
            


    def __calc_hand_value(self):
        value=0
        aces = list()
        for card in self.__hand:
            value += card.get_value()
            if(CardType.ACE == card.get_card_type()):
                aces.append(card)
              
                
        
        for ace_card in aces:
            # TODO: update this logic to support setting of the ace value to either 1 or 11
            if (value > 21):
                value -= 10
                
            
        self.__hand_value = value 
    
    


# end of player class
empCard = Card(CardType.ACE, SuitType.HEART)
#tempCard = Card(CardType.JACK, SuitType.HEART)
tempCard = Card(CardType.QUEEN, SuitType.HEART)
#tempCard = Card(CardType.KING, SuitType.HEART)
#tempCard = Card(CardType.TEN, SuitType.HEART)
tempCard.draw_card()














