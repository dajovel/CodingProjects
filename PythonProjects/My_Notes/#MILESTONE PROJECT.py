#MILESTONE PROJECT
#TICTACTOE FOR 2 PLAYERS
#Board should be printed out everytime a player makes a move
#idea of a number pad to match numbers to grid on tic tac toe board:
#7,8,9
#4,5,6
#1,2,3
#Welcome to Tic tac tpe
#player 1 do you want to be X or O?
#PLAYER 1 WILL GO FIRST.
#ARE YOU READY TO PLAY?
# test_board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']

# def display_board(board):
#     #clear_output()
#     print('n'*100)
#     print(board[7]+'|'+board[8]+'|'+board[9])
#     print('- - -')
#     print(board[4]+'|'+board[5]+'|'+board[6])
#     print('- - -')
#     print(board[1]+'|'+board[2]+'|'+board[3])
    
# display_board(test_board)

#write a function that can take in player input and assign ther marker as "X" or "O". Think about using while loops to contunually ask until you get a correct answer
# def player_input():
#     marker = ''
#     #KEEP ASKING PAYER 1 TO CHOOSE X OR O
#     while marker != 'X' and marker != 'O':
#         marker = input("Player 1, choose X or O: ")

#     #ASSIGN PLAYER 2, THE OPPOSITE MARKER
#     player1 = marker

#     if player1 == 'X':
#         player2 = 'O'
#     else:
#         player2 = 'X'
#     return (player1,player2)

# player_input()

#player1_marker , player2_marker = player_input()



# We need to print a board. √ option + "v" 
# Take in player input. √
# Place their input on the board.
# Check if the game is won,tied, lost, or ongoing.
# Repeat c and d until the game has been won or tied.
# Ask if players want to play again.

# players_list = [1,2,3,4,5,6,7,8,9]

# #board will keep track of players markers,
# board = []

# board_position = input("Please enter a number for the board position choice: ")

#position = int(input('Please enter a number'))

def display_board(board):
    print('n'*100)
    print(' | |')
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(' | |')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(' | |')
    print(board[1]+'|'+board[2]+'|'+board[3])
#Display_board(test_board)


#write a function that can take in player input and assign ther marker as "X" or "O". Think about using while loops to contunually ask until you get a correct answer
def player_input():
    """
    write a function that can take in player input 
    and assign ther marker as "X" or "O". 
    Think about using while loops to contunually 
    ask until you get a correct answer
    OUTPUT = (Player 1 marker. Player 2 marker )
    """

    marker = ''
    #KEEP ASKING PAYER 1 TO CHOOSE X OR O
    while marker != 'X' and marker != 'O':
        marker = input("Player 1, choose X or O: ").upper()
    
    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')

#player_input()

def place_marker(board, marker, position):
    
    board[position] = marker

def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

import random

def choose_first():
    flip = random.randint(0,1)
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
            #If i have a space that means my board is full
    
    return True

def player_choice(board):
    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input("Choose a position (1-9) "))
    
    return position


def replay():
    return input("Play again? Enter Yes or No: ").lower().startswith('y')

#while loop to keep runnning the game
print("Welcome to TicTacToe!")
while True:
    #PLAY THE GAME
    #SET EVERYTHING UP (BOARD, WHOS FIRST, CHOOSE MARKERS X,O)
    the_board = [' ']*10
    player1_marker, player2_marker = player_input() 

    turn = choose_first()
    print(turn + 'will go first')
    play_game = input("Ready to play? y  or n: ")
    if play_game.lower() == 'y':
        game_on = True
    else:
        game_on = False

    #GAME PLAY
    while game_on:
        if turn == 'Player 1':
            #show the board
            display_board(the_board)
            #choose a position
            position = player_choice(the_board)
            #Place marker on position
            place_marker(the_board, player1_marker, position)
            #check if they won

            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('PLAYER 1 HAS WON!!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("Tie GAME!")
                    game_on = False
                else:
                    turn = 'Player 2'

        else:
            #show the board
            display_board(the_board)
            #choose a position
            position = player_choice(the_board)
            #Place marker on position
            place_marker(the_board, player2_marker, position)
            #check if they won
            if win_check(the_board,player2_marker):
                display_board(the_board)
                print('PLAYER 2 HAS WON!!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("Tie GAME!")
                    game_on = False
                else:
                    turn = 'Player 1'            # #
    if not replay():
        break
#break out of whole loop on replay()