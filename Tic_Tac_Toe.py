'''

 this will implement a 3x3 game of Tic-Tac-Toe

#2 players should be able to play the game (sitting at same computer)
# the board will be printed out every time a player maked a move
# you should be able to accept input of the player position and then place a symbol on the board.
# the game will use the "numpad" to match the numbers to the grid on a tic - tac - toe board.

#- -----------
#| 1 | 2 | 3 |
#-------------
#| 4 | 5 | 6 |
#-------------
#| 7 | 8 | 9 |
#-------------


# program flow:
    # initialize the game
        #  print welcome message to the screen
        #  intitialize the game board data
        # prompt player 1 to get which icon they are going to use

        # ask if they are ready to play

        #while(game in play):
            # prompt player (1 or 2) position of their move
                # should be an integer between 1-9
            # print the board
            # get player move
            # print board
            # check for end game condition
              # see if last player that moved has 3 consecutive positions -- filter + lambda would be good here
                 # player has to have at least 3 moves
                 # check for cross, up/down  diagonal
        # end while loop


#NOTE:  usage of classes was left out in order to force usage of the non OOP aspects of python
#NOTE:  if a player repeats the same move then there move is forfetted.  this consciously done as a penality for stupidity

# learning notes:
    #1.  global variables must be imported into functions using the "global" keyword -- side effect of Dynamically typed language.
    #2. update on 10/31/2018.   logic for verifying a player move was improved.
'''

#TODO:  use this as an example to create a unit test with python.




# define globals
PLAYER1_ICON='';
PLAYER2_ICON='';
playerOneMoves = set();
playerTwoMoves = set();

VALID_PLAYER=('X', 'O')
gameBoard =[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
winningCombos = {1:(1, 2, 3), 2:(4, 5, 6), 3:(7, 8, 9),
                 4:(1, 4, 7), 5:(2,5,8), 6:(3, 6, 9),
                 7:(1, 5, 9), 8:(3, 5, 7) };

# this could have also been implemented to return a tuple
def initialize_board():

    global PLAYER1_ICON;
    global PLAYER2_ICON;


    playerChoice='';
    while(playerChoice not in VALID_PLAYER):
        playerChoice=input("Player 1: do you want to be 'X' or 'O' ? ")

    if(VALID_PLAYER[0] == playerChoice):
        PLAYER1_ICON = 'X';
        PLAYER2_ICON = 'O';
    else:
        PLAYER1_ICON = 'O';
        PLAYER2_ICON = 'X';

    print(f"player 1 is {PLAYER1_ICON}");
    print(f"player 2 is {PLAYER2_ICON}");



def print_board_template():
    print("-------------------");
    print(f"|  1  |  2  |  3  |");
    print("-------------------");
    print(f"|  4  |  5  |  6  |");
    print("-------------------");
    print(f"|  7  |  8  |  9  |");
    print("-------------------");

# TODO:  improve this with formatting
def print_board():
    global gameBoard
    print("-------------------");
    print(f"|  {gameBoard[0]}  |  {gameBoard[1]}  |  {gameBoard[2]}  |");
    print("-------------------");
    print(f"|  {gameBoard[3]}  |  {gameBoard[4]}  |  {gameBoard[5]}  |");
    print("-------------------");
    print(f"|  {gameBoard[6]}  |  {gameBoard[7]}  |  {gameBoard[8]}  |");
    print("-------------------");


def check_for_win(moveNumber):
    # player wins if the moves list contains any one of the winning combos
        # expects that winning combos are exactly 3 entries.
#    print("DEBUG -- checking board status")
    global gameBoard;
    global winningCombos;
    global playerOneMoves;
    global playerTwoMoves;

    activePlayer = 1 if (moveNumber%2==1) else 2;


    if(1 == activePlayer):
        playerMoves = playerOneMoves;
    else:
        playerMoves = playerTwoMoves;

#    print(f"DEBUG -- active Player is {activePlayer}");
#    print(f"DEBUG -- player1Moves = {playerOneMoves}")
#    print(f"DEBUG -- player2Moves = {playerTwoMoves}")
#    print(f"DEBUG -- checking against {playerMoves}");

    if(len(playerMoves) < 3):
        return False;


    for combo in winningCombos.values():
        matchCount=0;
        for move in playerMoves:
            if(move in combo):
                matchCount+=1;

        if(3 == matchCount):
            print(f"player {activePlayer} has a match on {combo}");
            return True;

            break;

    return False;

# active player and position should be integers
def validate_player_move(active_player, player_move):
    global playerOneMoves;
    global playerTwoMoves;

    if(  not player_move.isnumeric() ):
        print("invalid move! please enter the number of a space within the game board -- try again")
        return False;

    newMove = int(player_move);
    if(newMove not in range(1,10)):
        print("invalid move! please select a space within the valid range of moves -- try again")
        return False;

    # make sure that the space input by player 1 is not already occupied by player 2
    if(1 == active_player):
        if(newMove in playerTwoMoves):
            print("Invalid move! player 2 is already occupying this space -- try again.")
            return False;

    # make sure that the space input by player 2 is not already occupied by player 1
    else:
        if(newMove in playerOneMoves):
            print("Invalid move!  player 1 is already occupying this space -- try again.");
            return False;

    return True;



def process_player_move(moveNumber):
    global gameBoard;
    global PLAYER1_ICON;
    global PLAYER2_ICON;

   # print(f"DEBUG -- PLAYER1_ICON = {PLAYER1_ICON}")
   # print(f"DEBUG -- PLAYER2_ICON = {PLAYER2_ICON}")
 #   print(f"moveCntr = {moveNumber}");
    position=-1;
    activePlayer = 1 if (moveNumber % 2==1) else 2;

#    print(f"activePlayer = {activePlayer}");
    legalMove = False;
    while (not legalMove):
        tempInput = input(f"player {(activePlayer)} select your move: ")  # this is to check that the input is sane
        legalMove = validate_player_move(activePlayer, tempInput)
        if(legalMove):
            position = int(tempInput)

    if(1 == activePlayer):
        playerOneMoves.add(position)
        gameBoard[position-1]=PLAYER1_ICON;
    else:
        playerTwoMoves.add(position)
        gameBoard[position-1]=PLAYER2_ICON;




def Tic_Tac_Toe():
    print("Welcome to Tic-Tac-Toe")
    print("here is the game board")
    print_board_template();

    initialize_board();
    print_board();
    moveCntr=1;
    while True:
  #      print(f"\nstart of round  -- movceCntr = {moveCntr} ")
        process_player_move(moveCntr);
        print_board();
        if(True == check_for_win(moveCntr)):
            print(f"PLAYER {1 if (moveCntr%2==1) else 2} HAS WON!!!");  # change to ternary operator
            return;

        moveCntr+=1;
   #     print(f"end  main play loop -- movceCntr = {moveCntr} ")

##### main scripting section

Tic_Tac_Toe();
exit(0);
