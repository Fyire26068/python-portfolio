#Tic Tac Toe
#Plays the game of tic tac toe against a human opponent
#Anthony Garrard
# 11/13/20
import time
import sys

#globals
X = "X"
O = "O"
EMPTY = " "
TIE = "TIE"
NUMSQUARES = 9


#build functions
################
def slowText(text, speed=.03):
    """MAKES TYPING EFFECT TEXT"""

    for char in text:
        time.sleep(speed)
        sys.stdout.write(char)
        sys.stdout.flush()

    time.sleep(0.5)
    print()

def getNumber(question, low, high):
    responce = None
    while True:
      slowText(question)
      response = input()
      if response.isnumeric() and int(response) in range(low, high):
          response = int(response)
          break
      else:
          slowText(str.format("Please enter a number between {} and {}.", low, high-1))
    return(response)

def displayInstruct():
    """Display game instructions. to use simply type (displayInstruct)()"""
    slowText("""
    Welcome to the greatest intellectual challenge of all time: Tic-Tac-Toe.
    This will be a showdown between your human brain and my silicon processor

    You will make your move known by entering a number, 0-8. The number
    will correspond to the board position as illustrated:
                \t0 | 1 | 2
                \t---------
                \t3 | 4 | 5
                \t---------
                \t6 | 7 | 8
    
    Prepare yourself human. The ultimate battle is about to begin \n""")

def nextTurn(turn):
    """ this function switches the turn in the game. to use type turn = nextTurn(turn)"""
    if turn == X:
        return O
    else:
        return X

def pieces():
    """Determine if player or computer goes first. to use (computer, human = pieces())"""
    goFirst = askYesNo("Do you require the first move? (y/n): ")
    if(goFirst == "y" or goFirst == "yes"):
        slowText("\nThen take the first move. You will need it.")
        human = X
        computer = O
    else:
        slowText("\n Your bravery will be your undoing... I will go first.")
        human = O
        computer = X
    return computer, human
    
def askYesNo(question):
    """Ask a yes or no question and get back a yes or no answer. to use (answer = askYesNo(question))"""
    response = None
    while response not in ("y", "n", "yes", "no"):
        slowText(question)
        response = input().lower()
    return response

def newBoard():
    """Create new game board. To use (board = newBoard())"""
    board = []
    for square in range(NUMSQUARES):
        board.append(EMPTY)
    return board

def displayBoard(board):
    """Display game board on screen. to use (displayboard(board))"""
    print("\t",board[0],"|",board[1],"|",board[2])
    print("\t","---------")
    print("\t",board[3],"|",board[4],"|",board[5])
    print("\t","---------")
    print("\t",board[6],"|",board[7],"|",board[8])

def legalMove(board):
    moves = []
    for i in range(len(board)):
        if board[i] == " ":
            moves.append(i)
    return moves

def humanMove(board, human) :
    """Get human move. to use (move = humanMove(board, human))"""
    legal = legalMove(board)
    move = None
    while move not in legal:
        move = getNumber("Where would you like to make your move? (0-8)", 0, NUMSQUARES)
        if move not in legal:
            print("\nThat square is already occupied, foolish human. Choose another.\n")
    print("Fine. . .")
    return move


def computerMove(board, computer, human):
    """make the computer move"""
    #copying board
    cboard = board[:]
    #best positions to have
    BESTMOVES = (4,0,2,6,8,1,3,5,7)
    print("I shall take square number", end =" ")
    #if cpu can win, take that move
    for move in legalMove(cboard):
        cboard[move] = computer
        if winner(cboard) == computer:
            print(move)
            return move
        cboard[move] = EMPTY
   #if human can win, block that move
    for move in legalMove(cboard):
        cboard[move] = human
        if winner(cboard) == human:
            print(move)
            return move
        cboard[move] = EMPTY
   #if no one can win, next bestmove
    for move in BESTMOVES:
        if move in legalMove(board):
            print(move)
            return move

def winner(board):
    """Determine the game winner."""
    WAYSTOWIN = ((0, 1, 2),
                 (3, 4, 5),
                 (6, 7, 8),
                 (0, 4, 8),
                 (2, 4, 6),
                 (0, 3, 6),
                 (2, 5, 8),
                 (1, 4, 7))
    for row in WAYSTOWIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner
    if EMPTY not in board:
        return TIE


#main game
##########
def main():
    displayInstruct()
    turn = X
    computer, human = pieces()
    board = newBoard()
    
    while not winner(board):
        if turn == human:
            move = humanMove(board, human)
            board[move] = human
        else:
            move = computerMove(board, computer, human)
            board[move] = computer
        displayBoard(board)
        turn = nextTurn(turn)
    print(winner(board))


        
    



main()
