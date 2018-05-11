from random import randint
username = input("What's your name? ")
print ("Alright,", username,",", "damn the torpedos!!!", "Let's play battleship!!!")
difficuly = input("What difficulty would you like to play on? Easy, Medium, Hard, or Ultra? ")
board = []
tries_allowed = 5
if difficuly.lower() == "easy":
    for x in range(10):
      board.append(["*"] * 10)
elif difficuly.lower() == "medium":
    for x in range(15):
      board.append(["*"] * 15)
elif difficuly.lower() == "hard":
    for x in range(20):
      board.append(["*"] * 20)
elif difficuly.lower() == "ultra":
    for x in range(30):
      board.append(["*"] * 30)


def print_board(board):
    for row in board:
        print (" ".join(row))

#Using Random int to be the random coordinates for one position on the grid
def random_row(board):
    return randint(0, len(board) - 1)
def random_col(board):
    return randint(0, len(board[0]) - 1)

horizontal_ship_row_index = random_row(board)
#This is minus 2 becuase we don't want our 2 lenght ship to go off the board if it gets a second coordinate greater than the len
first_coordinate_random_horizontal_ship_column = randint(0, len(board[0]) - 2)
second_coordinate_random_horizontal_ship_column = first_coordinate_random_horizontal_ship_column + 1



first_vertical_ship_row_index = random_row(board)
second_vertical_ship_row_index = first_vertical_ship_row_index - 1
VERTICAL_ship_column = random_col(board)


#RADAR
print ("*********Our radar detects a ship coordinates is on the: ", horizontal_ship_row_index, "row, and", (first_coordinate_random_horizontal_ship_column), "and", second_coordinate_random_horizontal_ship_column, "column****************")
print ("*****Our radar also reads a ship at the ", first_vertical_ship_row_index, "and", second_vertical_ship_row_index, "rows, and", VERTICAL_ship_column, "column")


for turn in range(tries_allowed):
    #If player runs out of turns, it's game over and you get to see the board
    print ("You have done ", turn, "out of", tries_allowed, "tries.")
    if board[horizontal_ship_row_index][first_coordinate_random_horizontal_ship_column] == "X" and board[horizontal_ship_row_index][second_coordinate_random_horizontal_ship_column] == "X" and board[first_vertical_ship_row_index][VERTICAL_ship_column] == "X" and board[second_vertical_ship_row_index][VERTICAL_ship_column] == "X":
        for x in range(50):
            print ("*************YOU WIN!!!!!****************")
        for x in range(0, len(board)):
            for y in range(0, len(board[0])):
                if board[x][y] != "X":
                    board[x][y] = "O"
        print_board(board)

        break
    print_board(board)
    print ("")
    guess_row = int(input("Guess Row: "))
    guess_col = int(input("Guess Col: "))
    if guess_row == horizontal_ship_row_index and (guess_col == first_coordinate_random_horizontal_ship_column or guess_col == second_coordinate_random_horizontal_ship_column) or (guess_row == first_vertical_ship_row_index or guess_row == second_vertical_ship_row_index) and guess_col == VERTICAL_ship_column:
        print ("You got that correct")
        board[guess_row][guess_col] = "X"
        #player gets their turn back from guessing correct
        print ("You have done ", turn, "out of 4 tries")
        turn = turn -1
    else:
        if (guess_row < 0 or guess_row > (len(board) - 1)) or (guess_col < 0 or guess_col > (len(board[0]) - 1)):
            print ("That's off the board")
            turn = turn -1

        elif (board[guess_row][guess_col] == "X") or (board[guess_row][guess_col] == "O"):
            print ("You guessed that one already.")
            turn = turn -1
        else:
            print ("You missed!!!")
            board[guess_row][guess_col] = "O"
if turn == tries_allowed - 1:
    print ("Game over,", username)
    #This just gives the answers for the player to see if they lose
    board[horizontal_ship_row_index][first_coordinate_random_horizontal_ship_column] = "X"
    board[horizontal_ship_row_index][second_coordinate_random_horizontal_ship_column] = "X"

    board[first_vertical_ship_row_index][VERTICAL_ship_column] = "X"
    board[second_vertical_ship_row_index][VERTICAL_ship_column] = "X"
    for x in range(0, len(board)):
        for y in range(0, len(board[0])):
            if board[x][y] != "X":
                board[x][y] = "O"
    print_board(board)
