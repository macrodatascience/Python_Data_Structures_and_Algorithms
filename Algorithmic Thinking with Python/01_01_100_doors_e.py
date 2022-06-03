
"""
  The 100 Doors Coding Challenge
  There are 100 doors in a row that are initially closed
  Pass 1 - You go thru all the doors and toggle their state (O->C, C->O)
  Pass 2 - You go thru every second door (2,4,6..) and toggle it's state (O/C)
  Pass 3 - You go thru every third door (3,6,9,..) and toggle it's state
  ...
  Pass 100 - You go to 100th door and toggle it's state
  How many doors are open and how many are closed?
"""

## 1. List of the Boolean values to represent the state of the doors

doors = [False]*101  # ignore the 0th, and be able to map the door number to the index in the list

## 2. Nested For Loop

for i in range(1, len(doors)):
  for j in range(i,len(doors),i):
     doors[j] = not doors[j]

open, close = 0, 0
for i in range(1, len(doors)):
  if doors[i]:
    open+=1
    print(i, end=", ")
  else:
    close+=1
print()
print("Open doors: ",open, "; Closed doors: ",close)