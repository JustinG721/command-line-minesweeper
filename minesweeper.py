#simple text minesweeper
#Justin Grant

import random

#user can specify size of the board
def boardSize(size):
    board = [[' '] * size for _ in range(size)]
    return board


# board that the player will not see
#This board has all the info from the start.
def realBoard(board):
    for i in range(len(board)):
        row = ''
        for j in range(len(board)):
            tens = str(board[i][j])
            row += tens
            row += ' '
        print row
    print '\n'

def playerBoard(pboard, size):
    letters = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H')
    print 'the board so far: \n'
    print '    1    2    3    4    5    6    7    8'
    for i in range(size):
        print '{} {}'.format(letters[i], pboard[i])
 
#adds the bombs to the real board
def populate(board, b):
    iterations = 0
    length = len(board)
    while b > 0:
        for i in range(length):
            for j in range(length):
                ran = random.randint(0, 100)
                iterations += 1
                if ran <= 10 and board[i][j] != 'b':
                    board[i][j] = 'b'
                    b -= 1
                    if b == 0:
                        print ('bombs have been added.'+
                        'it did so in {} iterations\n'.format(iterations))
                        return
                
# there has to be a better way to do this.....
def getNums(board):
    length = len(board)
    for i in range(length):
        for j in range(length):
            numNear = 0
            # if the space isn't a bomb
            if board[i][j] != 'b':
                #check if all the spaces above are a bomb.
                for k in range(-1, 2):
                    try:
                        if board[i - 1][j + k] == 'b':
                            if i - 1 == -1 or (j + k) == -1:
                                pass
                            else:
                                numNear += 1
                    except IndexError:
                        pass
                #check if all the spaces below are a bomb
                for l in range(-1, 2):
                    try:
                        if board[i + 1][j + l] == 'b':
                            if i + 1 == -1 or j + 1 == -1:
                                pass
                            else:
                                numNear += 1
                    except IndexError:
                        pass
                #and the left space
                try: 
                    if board[i][j - 1] == 'b':
                        if j - 1 == -1 or i == -1:
                            pass
                        else:
                            numNear += 1
                except IndexError:
                        pass
                #and the right
                try:
                    if board[i][j + 1] == 'b':
                        numNear += 1
                except IndexError:
                        pass
                board[i][j] = numNear

def makeMove(board, pboard, space):
    letterDict = {'A': 0, 'B': 1, 'C': 2, 'D': 3,
                  'E': 4, 'F': 5, 'G': 6, 'H': 7}
    tens = list(space)
    row = int(letterDict.get(tens[0]))
    col = int(tens[1]) - 1
    pboard[row][col] = str(board[row][col])
              
            
def main():
    
    size = 8
    tens = boardSize(size)
    pboard = [[' '] * size for _ in range(size)]

    populate(tens, 15)
    getNums(tens)
    realBoard(tens)
    makeMove(tens, pboard, 'C5')
    playerBoard(pboard, size)

main()
