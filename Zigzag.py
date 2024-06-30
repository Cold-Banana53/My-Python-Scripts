import time, sys

IndentFlow = 'increasing'
IndentAmount = 0

while True:
    for i in range(0, 20):
        print(f'{" " * IndentAmount}**{" " * IndentAmount}**')
        IndentAmount += 1
        time.sleep(0.1)
    for i in range(0, 20):
        print(f'{" " * IndentAmount}**{" " * IndentAmount}**')
        IndentAmount -= 1
        time.sleep(0.1)
