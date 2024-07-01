# tic tac toe
import random, copy

BoardData = {'a3':"| |", 'b3':"| |", 'c3':"| |",
             'a2':"| |", 'b2':"| |", 'c2':"| |",
             'a1':"| |", 'b1':"| |", 'c1':"| |"}
BoardList = [   [BoardData['a3'], BoardData['b3'], BoardData['c3']],
                [BoardData['a2'], BoardData['b2'], BoardData['c2']],
                [BoardData['a1'], BoardData['b1'], BoardData['c1']]]
Notations = {   '7':'a1', '4':'a2', '1':'a3',
                '8':'b1', '5':'b2', '2':'b3',
                '9':'c1', '6':'c2', '3':'c3'}

PlayerVariable = ''
BotVariable = ''
PlayerTurn = 0
Victory = False
PlayerPoints = 0
BotPoints = 0

def MakeBoard():
	# board parameters. x is height, y is width
	x = 3
	y = 3
	NewBoard = []
	for a in range(x):
		List = []
		for b in range(y):
			List += ["| |"]
		NewBoard.append(List)
	return NewBoard

def ClearBoard():
        global BoardData
        for x, xKeys in enumerate(BoardData.keys):
                BoardData[xKeys] = '| |'

def PrintBoard(Board1):
	StringBoard = '\n'
	for x, xItems in enumerate(Board1):
		String = ''
		for y, yItems in enumerate(xItems):
			String += yItems
		StringBoard += ('\n' + String)
	print(StringBoard)

def PlayerMove():
        global BoardData
        global BoardList
        PrintBoard(BoardList)
        if PlayerTurn == 0: PlayerTurn += 1; return
        while PlayerTurn == 1:
                print(f'Your move: (You are {PlayerVariable})(1 - 9)')
                PlayerInput = input()

                # convert num to notation
                tempvar = Notations[PlayerInput] 
                PlayerInput = tempvar

                # avoid keys with already existing value
                if BoardData[PlayerInput] != "| |":
                        print('Invalid move!')
                        continue

                BoardData[PlayerInput] = PlayerVariable # sets dictionary to player variable

                # update BoardList based on boarddata dict
                BoardList = [   [BoardData['a3'], BoardData['b3'], BoardData['c3']], 
			        [BoardData['a2'], BoardData['b2'], BoardData['c2']], 
			        [BoardData['a1'], BoardData['b1'], BoardData['c1']]]
                break
        
	
	
	
def BotMove():
        global BoardData
        global BoardList
        PrintBoard(BoardList)
        while True:
                BotMove = random.choice(['a1', 'a2', 'a3', 
                                         'b1', 'b2', 'b3',
                                         'c1', 'c2', 'c3'])
                # avoid keys with already existing value
                if BoardData[BotMove] != "| |":
                        continue

                BoardData[BotMove] = BotVariable
                BoardList = [   [BoardData['a3'], BoardData['b3'], BoardData['c3']], 
			        [BoardData['a2'], BoardData['b2'], BoardData['c2']], 
			        [BoardData['a1'], BoardData['b1'], BoardData['c1']]]
                break
        print(f'Bot placed {BotVariable} at ')

def SetVariables():
        global PlayerVariable
        global BotVariable
        PlayerVariable = random.choice(["|x|", "|o|"])
        BotVariable = '|x|' if PlayerVariable == '|o|' else '|o|'
        PlayerTurn = (int(PlayerVariable == '|o|')) # PlayerTurn becomes 1 (skip turn) if true
        print(f"Player: {PlayerVariable[1]} \nBot: {BotVariable[1]}")

def Sight():
        return
        global PlayerPoints
        global BotPoints
        # check center victories:
        for x in range(Board):
                for y in range(Board[x]):
                        # check if playervariable or not
                        CellisPlayer = (Board[x][y] == PlayerVariable)
                        # check if it's on the edge of the board
                        Topmost = False
                        Bottommost = False
                        Leftmost = False
                        Rightmost = False

                        # if true then on first row
                        if ((Board[(x-1)%len(Board)][y] == Board[-1][y])): Topmost=True 
                        
                        # if true then on last row
                        if ((Board[(x+1)%len(Board)][y] == Board[0][y])): Bottommost=True

                        # if true then on first column
                        if ((Board[x][(y-1)%len(Board[x])] == Board[x][-1])): Leftmost=True

                        # if true then on last column
                        if ((Board[x][(y+1)%len(Board[x])] == Board[x][0])): Rightmost=True 

                        # victory checking
                        ## top edge victory check (checks left and right)
                        if Topmost and not(Leftmost or Rightmost):
                                if ((Board[x][y-1] == Board[x][y+1] and (Board[x][y] != Board[x][y-1]))
                        if Bottommost and not(Leftmost or Rightmost):
                                Victory += int((Board[x][y-1] == Board[x][y+1] and (Board[x][y] != Board[x][y-1]))

                        


def Connect():
        return

def VictoryCheck(board):
        return
                        




def Start():
        while True:
                SetVariables()
                while Victory == False:
                        PlayerMove()
                        BotMove()
                        VictoryCheck(BoardList)

		
		
	
	
