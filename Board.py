import random, time

Board = [['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
         ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
         ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
         ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
         ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
         ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
         ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
         ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
         ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
         ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_']]

def MakeBoard():
    # relevant lists
    Board = []
    List = []

    # x and y parameters. x is height, y is width
    x = 10 
    y = 10
    for i in range(x):
        for i in range(y):
            List += ['_', '#'][random.randint(0, 1)]
        Board.append(List)
        List = []
    return Board

def ApplyRules(board):
    NewBoard = []
    # pinpoint a cell then apply rules, but directly make new list to put in
    # new board
    for x in range(len(board)):
        NewList = []
        for y in range(len(board[x])):
            # check current cell status
            CC = board[x][y] # CC means 'CurrentCell'
            CCStatus = 'dead' if (CC == '_') else 'alive'

            # count living neighbor cells
            ## coordinates simplified
            up = (x - 1) % len(board)
            down = (x + 1) % len(board)
            left = (y - 1) % len(board[x])
            right = (y + 1) % len(board[x])
            
            NeighborLiveCount = 0
            if board[up][y] == '#': NeighborLiveCount += 1 # up
            if board[down][y] == '#': NeighborLiveCount += 1 # down
            if board[x][left] == '#': NeighborLiveCount += 1 # left
            if board[x][right] == '#': NeighborLiveCount += 1 # right
            if board[up][left] == '#': NeighborLiveCount += 1 # up left
            if board[up][right] == '#': NeighborLiveCount += 1 # up right
            if board[down][left] == '#': NeighborLiveCount += 1 # down left
            if board[down][right] == '#': NeighborLiveCount += 1 # down right

            # apply rules
            if (CCStatus == 'alive' and NeighborLiveCount in [2, 3]):
                NewList += ['#']
            elif (CCStatus == 'dead' and NeighborLiveCount == 3):
                NewList += ['#']
            else:
                NewList += ['_']
        NewBoard.append(NewList)
    return NewBoard
   

def PrintBoard(board):
    '''
    # for loop same as the other one used here
    # difference is that this one accesses the list directly
    # whereas the other one only references it and prints it
    for x in board:
        String = ''
        for y in x:
            String += y
        print(String)
        String = ''
    '''
    for x in range(len(board)):
        String = ''
        for y in range(len(board[x])):
            String += board[x][y]
        print(String)

def ActualStart():
    Board = MakeBoard() 
    while True:
        print()
        PrintBoard(Board)
        Board = ApplyRules(Board)
        #time.sleep(0.2)
			


