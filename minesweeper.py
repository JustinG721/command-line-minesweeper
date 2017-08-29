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
            row += '  '
        print row
    print '\n'

def playerBoard(pboard, size):
    letters = ('A', 'B', 'C', 'D',
               'E', 'F', 'G', 'H',
               'I', 'J', 'K', 'L')
    #print 'the board so far: \n'
    numString = ''
    for i in range(size):
        numString += '    '
        numString += str(i + 1)
    print numString
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

'''               
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
                            if j + 1 == -1 or j + l == -1:
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
'''
def getNeighbors(x, y, maxLen):
    neighbors = []
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if (j != -1 and i != -1 and
                j < maxLen and i < maxLen and
                ((i,j) != (x,y))):
                
                neighbors.append((i,j))
    return(neighbors)

def getIndexes(arr, tups):
    indexes = []
    for i in tups:
        indexes.append(arr[i[0]][i[1]])
    return indexes


def getNums(arr):
    length = len(arr)
    test = []
    numNear = 0
    for i in range(length):
        for j in range(length):
            if arr[i][j] != 'b':
                numNear = 0
                neighbors = getNeighbors(i, j, length)
                indexes = getIndexes(arr, neighbors)
                for k in indexes:
                    if k == 'b':
                        numNear += 1
                arr[i][j] = numNear
    #print (arr)
                
def makeMove(board, pboard, space):
    letterDict = {'A': 0, 'B': 1, 'C': 2, 'D': 3,
                  'E': 4, 'F': 5, 'G': 6, 'H': 7,
                  'I': 8, 'J': 9, 'K': 10,'L': 11}
  
    parsedSpace = list(space)
    row = int(letterDict.get(parsedSpace[0]))
    col = int(parsedSpace[1]) - 1
    pboard[row][col] = str(board[row][col])
    
    
              
            
def main():
    
    #size = int(raw_input('what will the size of the board be?'))
    size = 3
    tens = boardSize(size)
    pboard = boardSize(size)

    populate(tens, 4)
    getNums(tens)
    realBoard(tens)
    makeMove(tens, pboard, 'C2')
    playerBoard(pboard, size)
main()
