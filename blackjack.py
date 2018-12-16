import enum
import os
import random
import time


#club_image = u"\u2663"
#diamond_image = u"\u2666"
#heart_image = u"\u2665"
#spade_image = u"\u2660"
class CardFaceState(enum.Enum):
    DOWN = 0
    UP = 1



class CardFaceType(enum.Enum):
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
    HEART = enum.auto()
    SPADE = enum.auto()
    DIAMOND = enum.auto()
    CLUB = enum.auto()


# card class
class Card():

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
        return self.__suit_icon

    def get_value_icon(self):
        return self.__value_icon

# deck class
class Deck():


    def __init__(self):
        self.__cards = list()

    # this will populate the set of cards that make up the deck
    def generate_deck_cards(self):
        for this_suit in SuitType:
            for this_value in CardFaceType:
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

class Player():
    """
    this class implement a player class. this abstracts the operations a player takes during the
    course of a game of blackjack
    """
    cardVerticalBoundryStr = '------------'
    cardBufferStr = '|          |'
    multiCardSeperatorStr = '   '
    faceDownCardStr = '|##########|'

    def __init__(self):
        self.__hand = list()
        self.__hand_value = 0

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
        value = 0
        aces = list()
        for card in self.__hand:
            value += card.get_card_value()
            if CardFaceType.ACE == card.get_card_type():
                aces.append(card)

        for ace_card in aces:

            if value > 21:
                value -= 10
        return value

    def __draw_hand_vertical_boundry(self, numCards):
        for _ in range(0, numCards-1):
            print(self.cardVerticalBoundryStr, end=self.multiCardSeperatorStr)
        print(self.cardVerticalBoundryStr)

    def __draw_hand_suit_icon(self, numCards):
        for cardIdx in range(0, numCards-1):
            if CardFaceState.UP == self.__hand[cardIdx].get_card_face_state():
                print(f"|{self.__hand[cardIdx].get_suit_icon()}        {self.__hand[cardIdx].get_suit_icon()}|", end=self.multiCardSeperatorStr)
            else:
                print(self.faceDownCardStr, end=self.multiCardSeperatorStr)

             # print the last card
        if CardFaceState.UP == self.__hand[numCards-1].get_card_face_state():
            print(f"|{self.__hand[numCards-1].get_suit_icon()}        {self.__hand[numCards-1].get_suit_icon()}|")
        else:
            print(self.faceDownCardStr)

    def __draw_hand_card_buffer_region(self, numCards):
        for _ in range(0, 2):
            for cardIdx in range(0, numCards-1):
                if CardFaceState.UP == self.__hand[cardIdx].get_card_face_state():
                    print(self.cardBufferStr, end=self.multiCardSeperatorStr)
                else:
                    print(self.faceDownCardStr, end=self.multiCardSeperatorStr)
                
                    #last card
            if(CardFaceState.UP == self.__hand[numCards-1].get_card_face_state()):
                print(self.cardBufferStr)
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
        
        for card in self._Player__hand:
            if(CardFaceState.DOWN == card.get_card_face_state()):
                continue
            else:
                visible_value += card.get_card_value()
                if(CardFaceType.ACE == card.get_card_type()):
                    aces.append(card)  
            
        for ace_card in aces:
             if (visible_value > 21):
                visible_value -= 10
    
        return visible_value
        
        
    def get_visible_hand_value(self):
        self.__visible_hand_value = self.__calc_visible_hand_value()
        return self.__visible_hand_value
    
    def show_card_faces(self):
        for card in self._Player__hand:
            card.set_face_state(CardFaceState.UP)
            
    def should_hit(self, debug=False):
      #conditions for if a dealer should hit
            # 1. hand value is less <= 16
            # 2. if a soft 17 (contains an ace)
        value = self.get_hand_value()
        if(debug):
            print("DEBUG -- dealer hand value is {}".format(value))
        
        if(value < self.HARD_STAY-1):
            return True
        elif(value == self.HARD_STAY-1 and self.hand_contains_card_type(CardFaceType.ACE)):
            return True
        else:
            return False
        
            
            
            
#### Dealer class #####
    
#tempCard = Card(CardFaceType.ACE, SuitType.HEART)
#tempCard = Card(CardFaceType.JACK, SuitType.HEART)
#tempCard = Card(CardFaceType.QUEEN, SuitType.HEART)
#tempCard = Card(CardFaceType.KING, SuitType.HEART)
#tempCard = Card(CardFaceType.TEN, SuitType.HEART)
#tempCard.draw_card()





VALID_PLAYER_ACTION = ("stay", "hit")
BLACKJACK_VALUE=21;
SCREEN_CLEAR = '\n'*30

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
    print()
    
    # display the player hand and its value
    print("you have {}".format(player.get_hand_value()))
    player.display_hand()
    
    # prompt player to hit UNTIL the player "stays" or is bust.
    # if the player has blackjack then skip this part
    
    while(playerActionInput != "stay"):
        
        
        validAction = False
        while( not validAction):
            playerActionInput = input("do you want to hit or stay?\n").lower()
            validAction = validPlayerAction(playerActionInput)
      
        # if player action  = hit --> deal card, print hand and value      
        if(validAction and playerActionInput == "hit"):
            player.recieve_card( gameDeck.deal_card() )
    
            clear_screen()
            
            print("dealer is showing {}".format(dealer.get_visible_hand_value()))
            dealer.display_hand()
            print()
            
            print("you have {}".format(player.get_hand_value()))
            player.display_hand()
            print()
    
        if(player.get_hand_value() > BLACKJACK_VALUE):
            print("PLAYER HAS BUSTED -- HOUSE WINS!!")
            exit(0)
                 
       
        
        
        
    # let dealer hit until bust or stay at soft hard 18
    clear_screen()
    print("showing the dealers' hand\n")
    dealer.show_card_faces()
    
    print("dealer is showing {}".format(dealer.get_hand_value()))
    dealer.display_hand()
    print()
    
    print("you have {}".format(player.get_hand_value()))
    player.display_hand()
    print()
    time.sleep(4)
           
    while(dealer.should_hit()):
        clear_screen()
        print("dealer is drawing a card")
        time.sleep(2)
        dealer.recieve_card(gameDeck.deal_card())
                
        dealer.display_hand()
        print()
        player.display_hand()
   
    # final game winner logic
    game_winner = determine_blackjack_winner(player, dealer)
        
        
    ### end play black jack function    

def determine_blackjack_winner(player, dealer):
    playerValue = player.get_hand_value()
    dealerValue = dealer.get_hand_value()
    print("\ndealer has {}".format(dealerValue))
    print("player has {}".format(playerValue))
    
    if(dealerValue == playerValue ):
        winner  = None
        print("PUSH -- no one wins")
    elif(playerValue > BLACKJACK_VALUE):
        winner = dealer
        print("PLAYER has BUSTED -- DEALER WINS!!")    
    elif(dealerValue > BLACKJACK_VALUE):
        winner  = player
        print("DEALER HAS BUSTED -- PLAYER WINS!!")
    elif(playerValue <= dealerValue):
        winner = dealer
        print("DEALER HAS HIGHER HAND -- HOUSE WINS!!")
    else:
        winner = player
        print("PLAYER HAS HIGHER HAND -- CONGRATULATIONS, PLAYER WINS!!")
    
    return winner    

def clear_screen():
#     print(SCREEN_CLEAR)

    if os.name == 'nt':
#         print("\nWindows\n\n")
        _= os.system('cls')
    else:
        _= os.system('clear')
    
    
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
  
  
  TODO 3: fine tune the console output
     
  TODO 4: run pyLint
  TODO 5: doc string every class and method
     
'''
playBackJack()
exit(0)



