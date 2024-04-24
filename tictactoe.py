# Tutorial Tic Tac Toe Video: https://www.youtube.com/watch?v=n2o8ckO-lfk

# NOTE: I have modified the code to be more flexible, not the same as in the video.

# NOTE: Try to make it more interactive with the user and competitor
board = [
  ["1", "2", "3"],
  ["4", "5", "6"],
  ["7", "8", "9"]
]

user = True # when true it refers to x, otherwise o
turns = 0

def draw_line():
  print("-"*13)

def print_board(board):
  draw_line()
  for row in board:
    col_cnt = 0
    for col in row:
      pip = "|"
      new_row = pip + " " + col + " "
      if col_cnt == 2:
        new_row += pip
      print(new_row, end="")
      col_cnt += 1
    print()
    draw_line()


# Quit the game or program
def quit(user_input):
  if user_input.lower() == "q":
    print("Thanks for playing")
    return True
  else: return False


def check_input(user_input):
  # check if its a number
  if not isnum(user_input): return False
  user_input = int(user_input)
  # check if its 1 - 9
  if not bounds(user_input): return False # if number is not out of bound return False
  return True

def isnum(user_input):
  if not user_input.isnumeric():
    print("This is not a valid number!")
    return False
  else: return True

def bounds(user_input):
  if user_input > 9 or user_input < 1:
    print("This number is out of bounds")
    return False
  else: return True

def istaken(coords, board):
  row = coords[0]
  col = coords[1]
  if board[row][col] == "x" or board[row][col] == "o":
    print("This position(index) is already taken.")
    return True
  else: return False


def coordinates(user_input):
  row = int(user_input / 3)
  col =  user_input
  if col > 2: col = int(col % 3)
  return (row, col)

def add_to_board(coords, board, active_user):
  row = coords[0]
  col = coords[1]
  board[row][col] = active_user

def current_user(user):
  if user: return "x"
  else: return "o"

def iswin(user, board):
  if check_row(user, board): return True
  if check_col(user, board): return True
  if check_diag(user, board): return True
  return False

def check_row(user, board):
  for row in board:
    complete_row = True
    for slot in row:
      if slot != user:
        complete_row = False
        break
    if complete_row: return True
  return False

def check_col(user, board):
  for col in range(3):
    complete_col = True
    for row in range(3):
      if board[row][col] != user:
        complete_col = False
        break
    if complete_col: return True
  return False

def check_diag(user, board):
  # top left to bottom right
  if board[0][0] == user and board[1][1] == user and board[2][2] == user: return True
  # top right to bottom left
  elif board[0][2] == user and board[1][1] == user and board[2][0] == user: return True
  else: return False


while turns < 9:
  active_user = current_user(user)
  print_board(board)
  user_input = input("Enter a position 1 through 9 or enter \"q\" to quit: ")
  if quit(user_input): break
  if not check_input(user_input):
    print("Please try again.")
    continue
  user_input = int(user_input) - 1
  coords = coordinates(user_input)
  if istaken(coords, board):
    print("Please try again.")
    continue
  add_to_board(coords, board, active_user)
  if iswin(active_user, board):
    print_board(board)
    print(f"{active_user.upper()} won!")
    break
  turns += 1
  if turns == 9:
    print_board(board)
    print("Tie!")
  user = not user



# todo: 1. API to link html & CSS to python project
# todo: 2. Make AI to play with you in game and make it unbeatable to win
# todo: 3. Make the game has two choices to choose between to play with your freind or play with AI