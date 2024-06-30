import random

WinCount = 0
LoseCount = 0
DrawCount = 0

while True:
    print('\n')
    print(f'Wins: {WinCount}, Losses: {LoseCount}, Draws: {DrawCount}')
    print(f'Your move: (r)ock, (p)aper, (s)cissors\n')
    PlayerMove = input()
    if PlayerMove.lower() not in ['r','p','s']: # check player move validity
        print('\nInvalid Move!')
        continue
    else:
        # Bot move
        BotMove = 'rps'[random.randint(0, 2)]
        if BotMove == 'r':
            BotMoveMeaning = 'Rock'
        if BotMove == 'p':
            BotMoveMeaning = 'Paper'
        if BotMove == 's':
            BotMoveMeaning = 'Scissor'
        print(f'\nBot uses {BotMoveMeaning}!')
        # check for draws
        if PlayerMove.lower() == BotMove:
            DrawCount += 1
            print('\nA Draw!')
            continue
        else:
            if (PlayerMove == 'r' and BotMove == 'p'):
                LoseCount += 1
                print('\nPlayer Loses!')
                continue
            elif PlayerMove == 'p' and BotMove == 's':
                LoseCount += 1
                print('\nPlayer Loses!')
                continue
            elif PlayerMove == 's' and BotMove == 'r':
                LoseCount += 1
                print('\nPlayer Loses!')
                continue
            else:
                WinCount += 1
                print('\nPlayer Wins!')
                continue
            
