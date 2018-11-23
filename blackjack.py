import enum
import random
import time

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
        # TODO:  refactor references of card "type" to cardFaceType
    def __init__(self, cardFaceType=CardType.ACE, suit=SuitType.HEART, face=CardFaceState.UP):
        self.__type = cardFaceType
        self.__value = self.__cardValueDict[self.__type][0]
        self.__value_icon = self.__cardValueDict[self.__type][1]
        self.__suit = suit
        self.__suit_icon = self.__suitIconDict[self.__suit]
        self.__face_state = face

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
        # TODO: add in logic for if card is face down
        if(CardFaceState.UP == self.__face_state):
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
        return self.__suit_icon

    def get_value_icon(self):
        return self.__value_icon
    
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
    def deal_card(self, face=CardFaceState.UP):
        newCard = self.__cards.pop()
        newCard.set_face_state(face)
              
        return newCard


# end of deck class


# player class
# TODO add docstrings
class Player():
    
    cardStrTopBottom = '------------'  # TODO: refactor to cardVerticalBoundryStr
    cardStrBuffer = '|          |'    # TODO: refactor to cardBufferStr
    multiCardSeperatorStr = '   '      # TODO: refactor to multiCardSeporatorStr
    faceDownCardStr = '|##########|'
    
    def __init__(self):
        self.__hand = list();
        self.__hand_value = 0;
        
    # add a card to the players hand,
    def recieve_card(self, new_card):
        self.__hand.append(new_card)
        
    def get_hand(self):
        return self.__hand
          
     # return the value of a player's hand
    def get_hand_value(self):
        self.__hand_value = self.__calc_hand_value()
        return self.__hand_value

    def __calc_hand_value(self):
        value=0
        aces = list()
        for card in self.__hand:
            value += card.get_card_value()
            if(CardType.ACE == card.get_card_type()):
                aces.append(card)              
   
        for ace_card in aces:
            # TODO: update this logic to support setting of the ace value to either 1 or 11
            if (value > 21):
                value -= 10
                
        return value   
    
    def __draw_hand_vertical_boundry(self, numCards):
        for _ in range(0, numCards-1):
            print(self.cardStrTopBottom, end=self.multiCardSeperatorStr)
                
        print(self.cardStrTopBottom)
         
    def __draw_hand_suit_icon(self, numCards):
         
        for cardIdx in range(0, numCards-1):
                
            if(CardFaceState.UP == self.__hand[cardIdx].get_card_face_state()):
                print(f"|{self.__hand[cardIdx].get_suit_icon()}        {self.__hand[cardIdx].get_suit_icon()}|", end=self.multiCardSeperatorStr)
            else:
                print(self.faceDownCardStr, end=self.multiCardSeperatorStr)
                    
             # print the last card
        if(CardFaceState.UP == self.__hand[numCards-1].get_card_face_state()):        
            print(f"|{self.__hand[numCards-1].get_suit_icon()}        {self.__hand[numCards-1].get_suit_icon()}|")
        else:
            print(self.faceDownCardStr)
              
    
    def __draw_hand_card_buffer_region(self, numCards):
        for _ in range(0,2):
            for cardIdx in range(0, numCards-1):
                if(CardFaceState.UP == self.__hand[cardIdx].get_card_face_state() ):
                    print(self.cardStrBuffer, end=self.multiCardSeperatorStr)
                else:
                    print(self.faceDownCardStr, end=self.multiCardSeperatorStr)
                
                    #last card
            if(CardFaceState.UP == self.__hand[numCards-1].get_card_face_state()):
                print(self.cardStrBuffer)
            else:
                print(self.faceDownCardStr)    
        
    
    # draw a players hand
    def display_hand(self):
        numCards = len(self.__hand)
        
        if(0 == numCards):
            return;
        
        elif (1 == numCards):
            self.__hand[0].draw_card()
        
        else:
        # print the top line
            self.__draw_hand_vertical_boundry(numCards)
       
        #print the second line: | suit icon , spaces, suit icon, |
            self.__draw_hand_suit_icon(numCards)    
       
        # print the 3rd and 4th lines :  | , spaces, |  
            self.__draw_hand_card_buffer_region(numCards)
                        
        # print the 5th line:  | , spaces, card type, spaces, |
            for cardIdx in range(0, numCards-1):
                
                if(CardFaceState.UP == self.__hand[cardIdx].get_card_face_state()):
                    print("|    {:<2}    |".format(self.__hand[cardIdx].get_value_icon()), end=self.multiCardSeperatorStr)
                else:
                    print(self.faceDownCardStr, end=self.multiCardSeperatorStr)
            
             # last card
            if(CardFaceState.UP == self.__hand[numCards-1].get_card_face_state()):
                print("|    {:<2}    |".format(self.__hand[numCards-1].get_value_icon()) )
            else:
                print(self.faceDownCardStr)
                
        # print the 6th, 7th lines:  |, spaces, |
            self.__draw_hand_card_buffer_region(numCards)
            
           #print the 8th line: | suit icon , spaces, suit icon, |
            self.__draw_hand_suit_icon(numCards)
            
         # print the last line
            self.__draw_hand_vertical_boundry(numCards)
     
    def print_hand(self):
        for card in self.__hand:
            print("{} of {}".format(card.get_card_type(), card.get_card_suit()))
     
    def hand_contains_card_type(self, CardValue):
         # return true if the card contains a specific card value type
        for card in self.__hand:
            if(CardValue == card.get_card_type() ):
                return True
        
        return False
    
############## end of player class ###########################

class Dealer(Player):
    
    HARD_STAY=18
    
    def __init__(self):
        Player.__init__(self)
        self.__visible_hand_value = 0

    def __calc_visible_hand_value(self):
        visible_value=0
        aces = list()
        
        for card in self.__hand:
            if(CardFaceState.DOWN == card.get_card_face_state()):
                continue
            else:
                visible_value += card.get_card_value()
                if(CardType.ACE == card.get_card_type()):
                    aces.append(card)  
            
        for ace_card in aces:
            # TODO: update this logic to support setting of the ace value to either 1 or 11
            if (visible_value > 21):
                visible_value -= 10
    
        return visible_value
        
        
    def get_visible_hand_value(self):
        self.__visible_hand_value = self.__calc_visible_hand_value()
        return self.__visible_hand_value
    
    def show_card_faces(self):
        for card in self.__hand:
            card.set_face_state(CardFaceState.UP)
            
    def should_hit(self):
      #conditions for if a dealer should hit
            # 1. hand value is less <= 16
            # 2. if a soft 17 (contains an ace)
        
        if(self.get_hand_value() < 17):
            return True
        elif(self.get_hand_value() == 17 and self.__hand_contains_card_type(CardType.ACE)):
            return True
        else:
            return False
        
            
            
            
#### Dealer class #####
    
#tempCard = Card(CardType.ACE, SuitType.HEART)
#tempCard = Card(CardType.JACK, SuitType.HEART)
#tempCard = Card(CardType.QUEEN, SuitType.HEART)
#tempCard = Card(CardType.KING, SuitType.HEART)
#tempCard = Card(CardType.TEN, SuitType.HEART)
#tempCard.draw_card()





VALID_PLAYER_ACTION = ("stay", "hit")
BLACKJACK_BUST_VALUE=21;

def validPlayerAction(playerInput):
    
    valid = False
    
    for validInput in VALID_PLAYER_ACTION:
        if (playerInput == validInput):
            valid = True
            break
             
    return valid


def playBackJack():
        
    playerActionInput = str()
    
    #  initialize the deck
    gameDeck = Deck()
    gameDeck.generate_deck_cards()
    gameDeck.shuffle_cards()
    
    # create the dealer and the player
    player = Player()
    dealer = Dealer()
    
    # deal two cards the player - face up
    player.recieve_card(gameDeck.deal_card())
    player.recieve_card(gameDeck.deal_card())
    
    # dealer deals two cards, face one face up, face down
    dealer.recieve_card(gameDeck.deal_card())
    dealer.recieve_card(gameDeck.deal_card(CardFaceState.DOWN))
    
    # display the dealer hand and the its visible value
    print("dealer is showing {}".format(dealer.get_visible_hand_value()))
    dealer.display_hand()
    
    # display the player hand and its value
    print("you have {}".format(player.get_hand_value()))
    player.display_hand()
    
     # prompt player to hit UNTIL the player "stays" or is bust.
    
    while(playerActionInput != "stay"):
        
        
        validAction = False
        while( not validAction):
            playerActionInput = input("do you want to hit or stay").lower()
            validAction = validPlayerAction(playerActionInput)
      
        # if player action  = hit --> deal card, print hand and value      
        if(validAction and playerActionInput == "hit"):
            player.deal_card(gameDeck.deal_card())
    
            print("dealer is showing {}".format(dealer.get_visible_hand_value()))
            dealer.display_hand()
            
            print("you have {}".format(player.get_hand_value()))
            player.display_hand()
    
        if(player.get_hand_value() > BLACKJACK_BUST_VALUE):
            print("PLAYER HAS BUSTED -- HOUSE WINS!!")
            exit(0)
                 
       
        
        
        
    # let dealer hit until bust or stay at soft hard 18
    print("showing the dealers' hand")
    dealer.show_card_faces()
    time.sleep(5)
    
    print("dealer is showing {}".format(dealer.get_hand_value()))
    dealer.display_hand()
     
    print("you have {}".format(player.get_hand_value()))
    player.display_hand()
           
    while(dealer.should_hit()):
        dealer.recieve_card(gameDeck.deal_card())
    
    
    print("dealer has {}".format(dealer.get_hand_value()))
    print("plaeyer has {}".format(player.get_hand_value()))
    
    # final game winner logic
    if(dealer.get_hand_value() > BLACKJACK_BUST_VALUE):
        print("DEALER HAS BUSTED -- PLAYER WINS!!".format(dealer.get_hand_value()))
    
    elif(player.get_hand_value() <= dealer.get_hand_value()):
        print("DEALER HAS HIGHER HAND -- HOUSE WINS!!")
    else:
        print("PLAYER HAS HIGHER HAND -- CONGRATULATIONS, PLAYER WINS!!")
        
        
    ### end play black jack function    
        
        
def debug_display_hand():
    deck = Deck()
    deck.generate_deck_cards()
    deck.shuffle_cards()
    
    tempPlayer = Player()
    tempPlayer2 = Player()
    
    tempPlayer.recieve_card(deck.deal_card())
    tempPlayer.recieve_card(deck.deal_card())
    tempPlayer.recieve_card(deck.deal_card())
    tempPlayer.recieve_card(deck.deal_card())
    tempPlayer.recieve_card(deck.deal_card())
    
    tempPlayer2.recieve_card(deck.deal_card())
    tempPlayer2.recieve_card(deck.deal_card(CardFaceState.DOWN))
        
        
    tempPlayer.print_hand()
    tempPlayer.display_hand()
    
    print()
    
    tempPlayer2.print_hand()
    tempPlayer2.display_hand()
    
    
    
    
#### main body ################  
'''
  TOOD 1: refactor  CardType enum to CardFaceType
  TODO 2: debug the logic for the playBlackjack function
  TODO 3:   
     
'''




