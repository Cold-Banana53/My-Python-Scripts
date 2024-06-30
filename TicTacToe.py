# tic tac toe
import random

BoardData = {'a3':"| |", 'b3':"| |", 'c3':"| |",
             'a2':"| |", 'b2':"| |", 'c2':"| |",
             'a1':"| |", 'b1':"| |", 'c1':"| |"}
BoardList = [[BoardData['a3'], BoardData['b3'], BoardData['c3']], 
			 [BoardData['a2'], BoardData['b2'], BoardData['c2']], 
			 [BoardData['a1'], BoardData['b1'], BoardData['c1']]]
PlayerVariable = ''
BotVariable = ''

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
        while True:
                print(f'Your move: (You are {PlayerVariable})(1 - 9)')
                PlayerInput = input()
                # convert num to notation
                Notations = {'7':'a1', '4':'a2', '1':'a3', '8':'b1', '5':'b2', '2':'b3',
                             '9':'c1', '6':'c2', '3':'c3'}
                a = Notations[PlayerInput]
                PlayerInput = a
                '''print(PlayerInput)
                print(BoardData[PlayerInput])'''
                # avoid keys with already existing value
                if BoardData[PlayerInput] != "| |":
                        print('Invalid move!')
                        continue
                BoardData[PlayerInput] = PlayerVariable
                BoardList = [[BoardData['a3'], BoardData['b3'], BoardData['c3']], 
			 [BoardData['a2'], BoardData['b2'], BoardData['c2']], 
			 [BoardData['a1'], BoardData['b1'], BoardData['c1']]]
                break
	
	
	
def BotMove():
        global BoardData
        global BoardList
        while True:
                BotMove = random.choice(['a1', 'a2', 'a3', 'b1', 'b2', 'b3',
                                         'c1', 'c2', 'c3'])
                # avoid keys with already existing value
                if BoardData[BotMove] != "| |":
                        continue
                BoardData[BotMove] = BotVariable
                BoardList = [[BoardData['a3'], BoardData['b3'], BoardData['c3']], 
			 [BoardData['a2'], BoardData['b2'], BoardData['c2']], 
			 [BoardData['a1'], BoardData['b1'], BoardData['c1']]]
                # set the specified part of board data as the bot
                # ..variable
                break

def SetVariables():
        global PlayerVariable
        global BotVariable
        PlayerVariable = random.choice(["|x|", "|o|"])
        BotVariable = '|x|' if PlayerVariable == '|o|' else '|o|'
        print(f"Player: {PlayerVariable[1]} \nBot: {BotVariable[1]}")
        
def Start():
        while True:
                SetVariables()
                if PlayerVariable == '|x|':
                        while True:
                                PrintBoard(BoardList)
                                PlayerMove()
                                PrintBoard(BoardList)
                                BotMove()
                else:
                        while True:
                                PrintBoard(BoardList)
                                BotMove()
                                PrintBoard(BoardList)
                                PlayerMove()
		
		
	
	
