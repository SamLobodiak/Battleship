from random import randint
username = input("What's your name? ")
print ("Alright,", username,",", "damn the torpedos!!!", "Let's play battleship!!!")
difficuly = input("What difficulty would you like to play on? Easy, Medium, Hard, or Ultra? ")
board = []
tries_allowed = 5
count = 0
destroyer_notification = 0
submarine_notification = 0
loop_number = 999
if difficuly.lower() == "easy":
    for x in range(5):
      board.append(["*"] * 5)
elif difficuly.lower() == "medium":
    for x in range(10):
      board.append(["*"] * 10)
elif difficuly.lower() == "hard":
    for x in range(15):
      board.append(["*"] * 15)
elif difficuly.lower() == "ultra":
    for x in range(40):
      board.append(["*"] * 40)


def print_board(board):
    for row in board:
        print (" ".join(row))

def random_row(board):
    return randint(0, len(board) - 1)
def random_col(board):
    return randint(0, len(board[0]) - 1)

# setting the RNG for a 2 length ship
horizontal_ship_row_index = random_row(board)
#This is minus 2 because we don't want our 2 length ship to go off the board if it gets a second coordinate greater than the len
first_coordinate_random_horizontal_ship_column = randint(0, len(board[0]) - 2)
second_coordinate_random_horizontal_ship_column = first_coordinate_random_horizontal_ship_column + 1


#Drawing a ship of 3 length that won't ever go off the board
first_vertical_ship_row_index = randint(0, len(board) - 3)
second_vertical_ship_row_index = first_vertical_ship_row_index + 1
third_vertical_ship_row_index = first_vertical_ship_row_index + 2
VERTICAL_ship_column = random_col(board)


#RADAR to help me test
print ("")
print ("*********Our radar detects a Submarine at: ", horizontal_ship_row_index, "row, and", (first_coordinate_random_horizontal_ship_column), "and", second_coordinate_random_horizontal_ship_column, "column****************")
print ("")
print ("*****Our radar detects a Destroyer ship at: ", first_vertical_ship_row_index, second_vertical_ship_row_index, third_vertical_ship_row_index, "rows, and the", VERTICAL_ship_column, "column")
print ("")

for turn in range(loop_number):
    #If we have HITS on ALL coordinates of ALL ships
    if board[horizontal_ship_row_index][first_coordinate_random_horizontal_ship_column] == "X" and board[horizontal_ship_row_index][second_coordinate_random_horizontal_ship_column] == "X" and board[first_vertical_ship_row_index][VERTICAL_ship_column] == "X" and board[second_vertical_ship_row_index][VERTICAL_ship_column] == "X" and board[third_vertical_ship_row_index][VERTICAL_ship_column] == "X":
        for x in range(5):
            print ("*************YOU WIN!!!!!****************")
        for x in range(0, len(board)):
            for y in range(0, len(board[0])):
                if board[x][y] != "X":
                    board[x][y] = "O"
        print_board(board)
        break
    #This is to run only once when the player destroys the destroyer ship
    if destroyer_notification == 0 and board[first_vertical_ship_row_index][VERTICAL_ship_column] == "X" and board[second_vertical_ship_row_index][VERTICAL_ship_column] == "X" and board[third_vertical_ship_row_index][VERTICAL_ship_column] == "X":
        print ("YOU DESTROYED THEIR DESTROYER!!!")
        destroyer_notification += 1
    if submarine_notification == 0 and board[horizontal_ship_row_index][first_coordinate_random_horizontal_ship_column] == "X" and board[horizontal_ship_row_index][second_coordinate_random_horizontal_ship_column] == "X":
        print ("YOU DESTROYED THEIR SUBMARINE")
        submarine_notification += 1
    print ("You have done ", count, "out of", tries_allowed, "tries.")
    print ("")

    print_board(board)
    print ("")

    #If user inputs anything other than an int it will not let them
    while True:
        try:
            guess_row = int(input("Guess Row: "))
            guess_col = int(input("Guess Col: "))
            break
        except ValueError:
            print ("Oops!  That was no valid number.  Try again...")
    #if player guesses the right coordinates of any ship
    if guess_row == horizontal_ship_row_index and (guess_col == first_coordinate_random_horizontal_ship_column or guess_col == second_coordinate_random_horizontal_ship_column) or (guess_row == first_vertical_ship_row_index or guess_row == second_vertical_ship_row_index or guess_row == third_vertical_ship_row_index) and guess_col == VERTICAL_ship_column:
        print ("DIRECT HIT!!!")
        board[guess_row][guess_col] = "X"
        #player gets their turn back from guessing correct
    else:
        #If there is an edge case, if the player guesses off the board, or guesses one they have already guesseds
        if (guess_row < 0 or guess_row > (len(board) - 1)) or (guess_col < 0 or guess_col > (len(board[0]) - 1)):
            print ("That's off the board")
        elif (board[guess_row][guess_col] == "X") or (board[guess_row][guess_col] == "O"):
            print ("You guessed that one already.")
        else:
            print ("You missed!!!")
            board[guess_row][guess_col] = "O"
            #Count is for the turns taken when missed
            count = count + 1
    #If the player misses 5 times
    if count == 5:
        print ("Game over,", username)
        #Setting the boat coordinates to X
        board[horizontal_ship_row_index][first_coordinate_random_horizontal_ship_column] = "X"
        board[horizontal_ship_row_index][second_coordinate_random_horizontal_ship_column] = "X"

        board[first_vertical_ship_row_index][VERTICAL_ship_column] = "X"
        board[second_vertical_ship_row_index][VERTICAL_ship_column] = "X"
        board[third_vertical_ship_row_index][VERTICAL_ship_column] = "X"
        #Anything not X gets an O.
        for x in range(0, len(board)):
            for y in range(0, len(board[0])):
                if board[x][y] != "X":
                    board[x][y] = "O"
        print_board(board)
        break
