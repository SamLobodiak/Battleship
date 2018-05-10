from random import randint
username = input("What's your name? ")
print ("Alright,", username,",", "damn the torpedos!!!", "Let's play battleship!!!")


board = []
#appending a list of lists onto board.  row choice is board[][x] and column choice is board[x][]
for x in range(5):
  board.append(["*"] * 5)

#print function so it looks good without array commas
def print_board(board):
    for row in board:
        print (" ".join(row))
#prints board to console
print_board(board)

#Using Random int to be the random coordinates for the battleship
def random_row(board):
    return randint(0, len(board) - 1)
def random_col(board):
    return randint(0, len(board[0]) - 1)
ship_row = random_row(board)
ship_col = random_col(board)
print (ship_row)
print (ship_col)

for turn in range(4):
    guess_row = int(input("Guess Row: "))
    guess_col = int(input("Guess Col: "))

    if guess_row == ship_row and guess_col == ship_col:
      board[guess_row][guess_col] = "X"
      #using this for the celebration
      empty_string = ""
      for x in range(2500):
          print (empty_string, "Congratulations!")
          if x % 25 == 0:
              empty_string = empty_string + " "
      break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print ("Oops, that's not even in the ocean.")
        elif (board[guess_row][guess_col] == "X"):
            print ("You guessed that one already.")
        else:
            print ("You missed my battleship!")
board[guess_row][guess_col] = "X"
print_board(board)

    # Print (turn + 1) here!
if turn == 3:
    print ("Game over")

print_board(board)
