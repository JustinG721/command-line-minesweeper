#simple text minesweeper
#Justin Grant

import random
import sys


#user can specify size of the board
def boardSize(size):
    board = [[' '] * size for _ in range(size)]
    return board


#board that the player will not see
#this board has all the info from the start.
def showRealBoard(board):
    for i in range(len(board)):
        row = ''
        for j in range(len(board)):
            tens = str(board[i][j])
            row += tens + '  '
        print (row)
    print '\n'

def showPlayerBoard(pboard, size):
    letters = (map(chr, range(65,91)))
    numString = '    ' + '    '.join(str(i + 1) for i in range(size))
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
                        ' Loop ran {} times\n'.format(iterations))
                        return

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
                
def makeMove(board, pboard, coords):
    row, col = coords[0], coords[1]
    if pboard[row][col] != ' ':
        return
    pboard[row][col] = str(board[row][col])
    if str(board[row][col]) == '0':
        for r, c in getNeighbors(row, col, len(pboard)):
            makeMove(board, pboard, (r, c))

    

def createChoice(space):
    letterDict = dict(zip(map(chr, range(65,91)), range(26)))
    row = int(letterDict.get(space[0]))
    col = int(''.join(space[1:])) - 1
    return (row, col)
            
def main():
    #size = int(raw_input('what will the size of the board be?'))
    size = 8
    backendBoard, pboard = boardSize(size), boardSize(size)
    numBombs = (size ** 2) / 8

    populate(backendBoard, numBombs)
    getNums(backendBoard)
    showRealBoard(backendBoard)
    chosenTile = createChoice('H8')
    makeMove(backendBoard, pboard, chosenTile)
    showPlayerBoard(pboard, size)
    
main()
