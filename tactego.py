import random

"""
File:    tactego.py
Author:  Timothy Rauck
Date:    11/15/2023
Section: 52
E-mail:  trauck1@umbc.edu
Description: This program is a two player game called tactego, 
where both teams are trying to capture the other teams flag.
"""

# the tactego function runs the whole game using the other functions
def tactego():
    board = []
    game_list = []
    board = build_empty_board()
    game_list = get_file()
    print_first_board(board, game_list)
    play_game(board, game_list)


# this function gets the files and adds the pieces to the game_list, dividing them into the red and blue list
def get_file():
    file = open(file_name, "r")
    file_list = []
    for i in file:
        i = i.strip()
        file_list.append(i)
    piece_list = []
    blue_list = []
    red_list = []
    for i in range(len(file_list)):
        piece = file_list[i].split()
        for j in range(int(piece[1])):
            piece_list.append(piece[0])
    for x in range(len(piece_list)):
        red_list.append(f"R{piece_list[x]}")
        blue_list.append(f"B{piece_list[x]}")
    random.shuffle(red_list)
    random.shuffle(blue_list)
    game_list = [red_list, blue_list]
    return game_list


# this function builds the empty board
def build_empty_board():
    array = [[" " for w in range(width)] for l in range(length)]
    return array


# this function prints the original board at the beginning using the game_list
def print_first_board(board, game_list):
    row = 0
    col = 0
    for i in range(len(game_list[0])):
        board[row][col] = game_list[0][i]
        col += 1
        if col >= width:
            row += 1
            col = 0
    col = 0
    row = length - 1
    for i in range(len(game_list[1])):
        board[row][col] = game_list[1][i]
        col += 1
        if col >= width:
            row -= 1
            col = 0
    print(" " * 2, end="")
    for x in range(len(board[0])):
        print(f"  {x}  ", end="")
    print()
    for row in range(length):
        print(row, end="   ")
        for col in range(width):
            print(board[row][col], end="   ")
        print()


# this function prints the board with the changes given from the play_game function
def print_board(board, game_list):
    print(" " * 2, end="")
    for x in range(len(board[0])):
        print(f"  {x}  ", end="")
    print()
    for row in range(length):
        print(row, end="   ")
        for col in range(width):
            print(board[row][col], end="   ")
        print()


# In the function the players are taking turns moving their pieces either moving to a blank space or attacking
def play_game(board, game_list):
    game_over = False
    valid_turn = False
    turn_counter = 0
    # this for loop makes the length of the blank spaces two, so they line up with the pieces
    for i in range(len(board)):
        for j in range(len(board[i])):
            if len(board[i][j]) == 1:
                board[i][j] = "  "
    original_position = input("Blue Player, Select Piece to Move by Position >> ")
    next_position = input("Blue Player, Select Position to move Piece >> ")
    while game_over is False:
        original_position = original_position.split()
        next_position = next_position.split()
        original_piece = board[int(original_position[0])][int(original_position[1])]
        next_piece = board[int(next_position[0])][int(next_position[1])]
        original_piece = list(original_piece)
        next_piece = list(next_piece)
        # the validation makes sure the players are only moving their pieces
        if (original_piece[0] == "B" and turn_counter % 2 == 0) or (original_piece[0] == "R" and turn_counter % 2 == 1):
            valid_turn = True
            # this validation makes sure the players can't move the flag
            if original_piece[1] != "F" and original_piece[1] != "M":
                valid_turn = True
                # this validation is limiting how far the pieces can move in one turn
                if (int(next_position[0]) + 1 == int(original_position[0])
                        or int(original_position[0]) == int(next_position[0]) - 1
                        or int(original_position[0]) == int(next_position[0])):
                    valid_turn = True
                    if (int(next_position[0]) + 1 == int(original_position[0])
                            or int(original_position[0]) == int(next_position[0]) - 1
                            or int(original_position[0]) == int(next_position[0])):
                        valid_turn = True
                        # this validation makes sure the player is actually moving the piece
                        if next_position[0] == original_position[0] and next_position[1] == original_position[1]:
                            print("You have to move a piece, try again.")
                            valid_turn = False
                            turn_counter -= 1
                        # this validation stops the player from attacking their own piece
                        if original_piece[0] == next_piece[0]:
                            print("This turn is invalid, try again.")
                            valid_turn = False
                            turn_counter -= 1
                    else:
                        print("This turn is invalid, try again.")
                        valid_turn = False
                        turn_counter -= 1
                else:
                    print("This turn is invalid, try again.")
                    valid_turn = False
                    turn_counter -= 1
            else:
                print("You can't move a flag or a mine, try again.")
                valid_turn = False
                turn_counter -= 1
        else:
            print("This turn is invalid, try again.")
            valid_turn = False
            turn_counter -= 1
        if valid_turn is True:
            # if it is a valid turn, the piece could either be attacking or moving to blank space
            if len(next_piece) == 2 and (next_piece[0] == "B" or next_piece[0] == "R"):
                if next_piece[1] == "F":
                    game_over = True
                    board[int(original_position[0])][int(original_position[1])] = "  "
                    original_piece = "".join(original_piece)
                    board[int(next_position[0])][int(next_position[1])] = original_piece
                elif next_piece[1] == "M" and original_piece[1] == "S":
                    board[int(original_position[0])][int(original_position[1])] = "  "
                    original_piece = "".join(original_piece)
                    board[int(next_position[0])][int(next_position[1])] = original_piece
                elif next_piece[1] == "M" and original_piece[1] != "S":
                    board[int(original_position[0])][int(original_position[1])] = "  "
                    board[int(next_position[0])][int(next_position[1])] = "  "
                elif next_piece[1] == "S" and original_piece[1] == "S":
                    game_over = True
                    board[int(original_position[0])][int(original_position[1])] = "  "
                    original_piece = "".join(original_piece)
                    board[int(next_position[0])][int(next_position[1])] = original_piece
                elif next_piece[1] == "S":
                    board[int(original_position[0])][int(original_position[1])] = "  "
                    original_piece = "".join(original_piece)
                    board[int(next_position[0])][int(next_position[1])] = original_piece
                elif original_piece[1] == "S":
                    board[int(original_position[0])][int(original_position[1])] = "  "
                elif int(original_piece[1]) >= int(next_piece[1]):
                    board[int(original_position[0])][int(original_position[1])] = "  "
                    original_piece = "".join(original_piece)
                    board[int(next_position[0])][int(next_position[1])] = original_piece
                elif int(original_piece[1]) < int(next_piece[1]):
                    board[int(original_position[0])][int(original_position[1])] = "  "
                # if you attack an assassin piece you always win
                elif next_piece[1] == "A":
                    board[int(original_position[0])][int(original_position[1])] = "  "
                    original_piece = "".join(original_piece)
                    board[int(next_position[0])][int(next_position[1])] = original_piece
                # if you attack using an assassin piece you will always win
                elif original_piece[1] == "A":
                    board[int(original_position[0])][int(original_position[1])] = "  "
                    original_piece = "".join(original_piece)
                    board[int(next_position[0])][int(next_position[1])] = original_piece
            # this is what happens if you move into a blank space
            elif len(next_piece) == 2 and (next_piece[0] != "B" or next_piece[0] != "R"):
                board[int(original_position[0])][int(original_position[1])] = "  "
                original_piece = "".join(original_piece)
                board[int(next_position[0])][int(next_position[1])] = original_piece
        print_board(board, game_list)
        # if someone wins the game_over value will be true, so the game checks whose turn it is when the game is over
        if game_over is True:
            if turn_counter % 2 == 0:
                print("Blue has won")
            elif turn_counter % 2 == 1:
                print("Red has won")
        turn_counter += 1
        if game_over is False:
            if turn_counter % 2 == 0:
                original_position = input("Blue Player, Select Piece to Move by Position >> ")
                next_position = input("Blue Player, Select Position to move Piece >> ")
            elif turn_counter % 2 == 1:
                original_position = input("Red Player, Select Piece to Move by Position >> ")
                next_position = input("Red Player, Select Position to move Piece >> ")


if __name__ == '__main__':
    random.seed(input('What is seed? '))
    file_name = input('What is the filename for the pieces? ')
    length = int(input('What is the length? '))
    width = int(input('What is the width? '))
    tactego()
