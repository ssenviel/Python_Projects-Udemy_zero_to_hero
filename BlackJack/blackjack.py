"""
this module implements a command line version of blackjack.
this was the solution to milestone 2 project from the Python Zero To Hero Udemy course
"""

import os
import random
import time
from Card import Card, CardFaceState, CardFaceType, SuitType


VALID_PLAYER_ACTION = ("stay", "hit")
BLACKJACK_VALUE = 21
SCREEN_CLEAR = '\n'*30
STARTING_DEFAULT_HOLDINGS = 100


# deck class
class BlackJackDeck():
    """
    this class implements the Deck class
    Members:
        __cards -- a list of Card objects
    """

    def __init__(self):
        self.__cards = list()

# this will populate the set of cards that make up the deck
    def generate_deck_cards(self):
        """
        allocate all the cards to be contained in the deck
        after this function the Cards list will of the deck object
        will contain cards.
        """
        for this_suit in SuitType:
            for this_value in CardFaceType:
# print(f"{this_suit} of {this_value}")
                self.__cards.append(Card(this_value, this_suit))

# this will shuffle the cards that make up the deck
    def shuffle_cards(self):
        """ shuffle the card object in the cards list """
        random.shuffle(self.__cards)

    # return the list of cards
    def cards(self):
        """ get return a copy of the cards in the deck """
        return self.__cards

    # pops a card off the deck and returns the card
    def deal_card(self, face=CardFaceState.UP):
        """ remove a card from the deck
            parameters:
                face == CardFaceState enum type that will determine if
                        the card is dealt face up or face down
        """
        new_card = self.__cards.pop()
        new_card.set_face_state(face)
        return new_card

# end of deck class

# player class
class Player():
    """
    this class implement a player class. this abstracts the operations a player takes during the
    course of a game of blackjack
    members:
        __hand :  list of cards
        __hand_value :  value of the hand
    """
    cardVerticalBoundryStr = '------------'
    cardBufferStr = '|          |'
    multiCardSeperatorStr = '   '
    faceDownCardStr = '|##########|'

    def __init__(self):
        self.__hand = list()
        self.__hand_value = 0
    
    def clear_hand(self):
        """
            empty the hand of a player
        """
        self.__hand.clear();

    def recieve_card(self, new_card):
        """ add a card to the players hand """
        self.__hand.append(new_card)

    def get_hand(self):
        """ return the players list of cards """
        return self.__hand

# return the value of a player's hand
    def get_hand_value(self):
        """ update and return the value of the players hand """
        self.__hand_value = self.__calc_hand_value()
        return self.__hand_value

    def __calc_hand_value(self):
        """ calculate the current value of the hand of cards """
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

    def __draw_hand_vertical_boundry(self, num_cards):
        """ draw the verical boundary for  a card """
        for _ in range(0, num_cards-1):
            print(self.cardVerticalBoundryStr, end=self.multiCardSeperatorStr)
        print(self.cardVerticalBoundryStr)

    def __draw_hand_suit_icon(self, num_cards):
        """draw the line of a card that contains the suit icon """
        for card_idx in range(0, num_cards-1):
            if CardFaceState.UP == self.__hand[card_idx].get_card_face_state():
                print(f"|{self.__hand[card_idx].get_suit_icon()}        {self.__hand[card_idx].get_suit_icon()}|", end=self.multiCardSeperatorStr)
            else:
                print(self.faceDownCardStr, end=self.multiCardSeperatorStr)

# print the last card
        if CardFaceState.UP == self.__hand[num_cards-1].get_card_face_state():
            print(f"|{self.__hand[num_cards-1].get_suit_icon()}        {self.__hand[num_cards-1].get_suit_icon()}|")
        else:
            print(self.faceDownCardStr)

    def __draw_hand_card_buffer_region(self, num_cards):
        for _ in range(0, 2):
            for card_idx in range(0, num_cards-1):
                if CardFaceState.UP == self.__hand[card_idx].get_card_face_state():
                    print(self.cardBufferStr, end=self.multiCardSeperatorStr)
                else:
                    print(self.faceDownCardStr, end=self.multiCardSeperatorStr)
#last card
            if CardFaceState.UP == self.__hand[num_cards-1].get_card_face_state():
                print(self.cardBufferStr)
            else:
                print(self.faceDownCardStr)
    # draw a players hand
    def display_hand(self):
        """
          draw a players hand on the console
        """
        num_cards = len(self.__hand)
        if 0 == num_cards:
            return

        if 1 == num_cards:
            self.__hand[0].draw_card()
        else:
# print the top line
            self.__draw_hand_vertical_boundry(num_cards)
#print the second line: | suit icon , spaces, suit icon, |
            self.__draw_hand_suit_icon(num_cards)
# print the 3rd and 4th lines :  | , spaces, |
            self.__draw_hand_card_buffer_region(num_cards)
# print the 5th line:  | , spaces, card type, spaces, |
            for card_idx in range(0, num_cards-1):
                if CardFaceState.UP == self.__hand[card_idx].get_card_face_state():
                    print("|    {:<2}    |".format(self.__hand[card_idx].get_value_icon()), end=self.multiCardSeperatorStr)
                else:
                    print(self.faceDownCardStr, end=self.multiCardSeperatorStr)
                        # last card
            if CardFaceState.UP == self.__hand[num_cards-1].get_card_face_state():
                print("|    {:<2}    |".format(self.__hand[num_cards-1].get_value_icon()))
            else:
                print(self.faceDownCardStr)
# print the 6th, 7th lines:  |, spaces, |
            self.__draw_hand_card_buffer_region(num_cards)
# print the 8th line: | suit icon , spaces, suit icon, |
            self.__draw_hand_suit_icon(num_cards)
# print the last line
            self.__draw_hand_vertical_boundry(num_cards)

    def hand_contains_card_type(self, card_value):
        """
            return true if the hand contains a card of a certain type
            Args:
                card_value -- cardFaceType enum object being searched for
        """
# return true if the card contains a specific card value type
        for card in self.__hand:
            if card_value == card.get_card_type():
                return True
        return False
############## end of player class ###########################
class Dealer(Player):
    """
    this class implements the logic for the blackjack blackjack_game_dealer.
    it is a subclass of player
    """
    HARD_STAY = 18
    def __init__(self):
        Player.__init__(self)
        self.__visible_hand_value = 0

    def __calc_visible_hand_value(self):
        visible_value = 0
        aces = list()
        for card in self._Player__hand:
            if CardFaceState.DOWN == card.get_card_face_state():
                continue
            else:
                visible_value += card.get_card_value()
                if CardFaceType.ACE == card.get_card_type():
                    aces.append(card)

        for ace_card in aces:
            if visible_value > 21:
                visible_value -= 10

        return visible_value

    def get_visible_hand_value(self):
        """
        return the value of the cards that are face up
        """
        self.__visible_hand_value = self.__calc_visible_hand_value()
        return self.__visible_hand_value
    def show_card_faces(self):
        """ set all the cards in the hand to face up"""
        for card in self._Player__hand:
            card.set_face_state(CardFaceState.UP)
    def should_hit(self, debug=False):
        """
            return true if the blackjack_game_dealer should hit based on the current hand
            conditions for if a blackjack_game_dealer should hit
            # 1. hand value is less <= 16
            # 2. if a soft 17 (contains an ace)

            Args:
                debug --  debug log flag. will output additional info
        """

        value = self.get_hand_value()
        if debug:
            print("DEBUG -- blackjack_game_dealer hand value is {}".format(value))
        if (value < self.HARD_STAY-1) or (value == self.HARD_STAY-1 and self.hand_contains_card_type(CardFaceType.ACE)):
            return True
        else:
            return False

class UserPlayer(Player):
    """
        this is a class that implements the user player. 
        TODO:  refactor "holdings" --> "funds"
    """
    def __init__(self, holdings=0):

        Player.__init__(self)
        self.__funds = holdings

    
    def add_winnings(self, winnings):
        self.__funds += winnings
    
    def get_funds(self):
        return self.__funds
    
    def subtract_losses(self, loss):
        self.__funds -= loss
        
    

#### end UserPlayerClass #####

class GameInfo():
    
    def set_wager_amount(self, wager=1):
        self.__wager_amount = wager

    def get_wager_amount(self):
        return self.__wager_amount

##### GameInfo class 

def valid_player_action(player_input):
    """
    return true if the player input is valid
    Args:
        player_input -- string input by the player
    """
    valid = False
    for valid_input in VALID_PLAYER_ACTION:
        if player_input == valid_input:
            valid = True
            break
    return valid

def play_back_jack(blackjack_player, blackjack_dealer, player_wager=1):
    """ 
       main logic for a game of blackjack
       blackjack_player = object of UserPlayer class
       blackjack_dealer = object of the blackjack_dealer class
       player_wager = amount in dollars to bet
     
    """
    player_action_input = str()

#  initialize the deck
    game_deck = BlackJackDeck()
    game_deck.generate_deck_cards()
    game_deck.shuffle_cards()

# clear the hand of the blackjack_dealer and the blackjack_player
    blackjack_player.clear_hand()
    blackjack_dealer.clear_hand()
    
# deal two cards the blackjack_player - face up
    blackjack_player.recieve_card(game_deck.deal_card())
    blackjack_player.recieve_card(game_deck.deal_card())

# blackjack_dealer deals two cards, face one face up, face down
    blackjack_dealer.recieve_card(game_deck.deal_card())
    blackjack_dealer.recieve_card(game_deck.deal_card(CardFaceState.DOWN))
# display the blackjack_dealer hand and the its visible value
    print("blackjack_dealer is showing {}".format(blackjack_dealer.get_visible_hand_value()))
    blackjack_dealer.display_hand()
    print()
# display the blackjack_player hand and its value
    print("you have {}".format(blackjack_player.get_hand_value()))
    blackjack_player.display_hand()
# prompt blackjack_player to hit UNTIL the blackjack_player "stays" or is bust.
# if the blackjack_player has blackjack then skip this part
    while player_action_input != "stay":
        valid_action = False
        while not valid_action:
            player_action_input = input("do you want to hit or stay?\n").lower()
            valid_action = valid_player_action(player_action_input)
# if blackjack_player action  = hit --> deal card, print hand and value
        if(valid_action and player_action_input == "hit"):
            blackjack_player.recieve_card(game_deck.deal_card())
            clear_screen()
            print("blackjack_dealer is showing {}".format(blackjack_dealer.get_visible_hand_value()))
            blackjack_dealer.display_hand()
            print()
            print("you have {}".format(blackjack_player.get_hand_value()))
            blackjack_player.display_hand()
            print()
        if blackjack_player.get_hand_value() > BLACKJACK_VALUE:
            print("PLAYER HAS BUSTED -- HOUSE WINS!!")
            exit(0)
    # let blackjack_dealer hit until bust or stay at soft hard 18
    clear_screen()
    print("showing the dealers' hand\n")
    blackjack_dealer.show_card_faces()
    print("blackjack_dealer is showing {}".format(blackjack_dealer.get_hand_value()))
    blackjack_dealer.display_hand()
    print()
    print("you have {}".format(blackjack_player.get_hand_value()))
    blackjack_player.display_hand()
    print()
    time.sleep(4)
    while blackjack_dealer.should_hit():
        clear_screen()
        print("blackjack_dealer is drawing a card")
        time.sleep(2)
        blackjack_dealer.recieve_card(game_deck.deal_card())
        blackjack_dealer.display_hand()
        print()
        blackjack_player.display_hand()
# final game winner logic
    game_winner = determine_blackjack_winner(blackjack_player, blackjack_dealer)
    
    if game_winner is blackjack_player:
        blackjack_player.add_winnings(player_wager)
    elif game_winner is blackjack_dealer:
        blackjack_player.subtract_losses(player_wager)
    else:
    	pass
    
### end play black jack function

def determine_blackjack_winner(player, dealer):
    """
    determine the winner of the blackjack game
    parameters:
        player -- object of the Player class
        dealer -- object of the Dealer class

        returns:
            object that has the better or winning hound or none if a push
    """
    player_value = player.get_hand_value()
    dealer_value = dealer.get_hand_value()
    print("\ndealer has {}".format(dealer_value))
    print("player has {}".format(player_value))
    if dealer_value == player_value:
        winner = None
        print("PUSH -- no one wins")
    elif player_value > BLACKJACK_VALUE:
        winner = dealer
        print("PLAYER has BUSTED -- DEALER WINS!!")
    elif dealer_value > BLACKJACK_VALUE:
        winner = player
        print("DEALER HAS BUSTED -- PLAYER WINS!!")
    elif player_value <= dealer_value:
        winner = dealer
        print("DEALER HAS HIGHER HAND -- HOUSE WINS!!")
    else:
        winner = player
        print("PLAYER HAS HIGHER HAND -- CONGRATULATIONS, PLAYER WINS!!")
    return winner

def clear_screen():
    """ clear the screen: uses OS system call """
#     print(SCREEN_CLEAR)

    if os.name == 'nt':
#         print("\nWindows\n\n")
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def collect_player_wager(game_player):
  
    valid_bet = False
    
    while not valid_bet:
        bet = input("how much would you like to like to bet? ")
     
        if(int(bet) > game_player.get_funds() or not bet.isnumeric() ):
            print("invalid bet amount, try again muthafucka")
        else:
            valid_bet = True
    return int(bet)


def blackjack_game():
	blackjack_game_player = UserPlayer(holdings=STARTING_DEFAULT_HOLDINGS)
	blackjack_game_dealer = Dealer()
	replayGame = True
	
	print("welcome to CLI black jack, you have ${} to play with. ".format(blackjack_game_player.get_funds()))
	game_wager = collect_player_wager(blackjack_game_player)
	play_back_jack(blackjack_player = blackjack_game_player, blackjack_dealer = blackjack_game_dealer, player_wager = game_wager)
	
	playerFunds = blackjack_game_player.get_funds()
	
	if playerFunds <= 0:
		print("you are broke!! goodbye broke nigga  :)")
		replayGame = False
	    
	while replayGame:
		if playerFunds > 0:
			replay = input("you have ${} remaining. would you like to play again? (yes/no)".format(blackjack_game_player.get_funds()))
			if("yes" == replay ):
				play_back_jack(blackjack_game_player, blackjack_game_dealer, collect_player_wager(blackjack_game_player))
			else:
				print("good-bye")
				replayGame = False
		else:
			print("you have no more money. Get cho biatch ass away from the table!")
			replayGame = False	


#### main body ####
if __name__ == '__main__':
	blackjack_game()
	exit(0)
	
	
	


    
# TODO: create logic to update player winnings  and ask to play gain
# TODO:  add the main-program definition

