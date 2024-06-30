# trying to manipulate lists

import sys, random, time

List = []

while True:
    print("""Want to add something to the list?
          (Press Enter to show the list and exit)""")
    UserInput = input()
    if UserInput.strip() == '':
          print(List)
          time.sleep(3)
          sys.exit()
    List += [UserInput]
