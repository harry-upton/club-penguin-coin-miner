from pynput.keyboard import Key, Controller as kc
from pynput.mouse import Button, Controller as mc
import time
import random
import math
import argparse

keyboard = kc()
mouse = mc()

oldX = 0
oldY = 0

# Pass the arguments from the command line.
parser = argparse.ArgumentParser()

parser.add_argument("x1", type=int, help="The x coordinate of the upper left corner of the zone to dig within.")
parser.add_argument("y1", type=int, help="The y coordinate of the upper left corner of the zone to dig within.")
parser.add_argument("x2", type=int, help="The x coordinate of the lower right corner of the zone to dig within.")
parser.add_argument("y2", type=int, help="The y coordinate of the lower right corner of the zone to dig within.")

parser.add_argument("-i", "--iterations", type=int, help="The number of times the mining loop will run, meaning the number of the times the script will make the penguin dig.", default=10)
parser.add_argument("-d", "--digtime", type=int, help="The amount of time the script will wait while digging before moving on to a new location.", default=12)
parser.add_argument("-w", "--walktime", type=int, help="The amount of time the script will wait while walking to give the penguin enough time to move.", default=3)
parser.add_argument("-m", "--mindistance", type=int, help="The minimum distance a new coordinate must be from the previous coordinate.", default=50)

args = parser.parse_args()

# X and Y of the upper left corner of the area to dig within.
x1 = args.x1
y1 = args.y1

# X and Y of the lower right corner of the area to dig within.
x2 = args.x2
y2 = args.y2

# The number of times the loop will run, meaning the number of times the script will make the penguin dig.
numberOfIterations = args.iterations
# The amount of time the script will wait while digging before moving on to a new location
digtime = args.digtime
# The amount of time the script will wait while walking to give the penguin enough time to move.
walktime = args.walktime
# The minimum distance a new coordinate must be from the previous coordinate.
minDistance = args.mindistance

if(x1 > x2 or y1 > y2):
    raise ValueError("Invalid mining area!")

def pick_position():
    while True:
        # Pick a random position within the area defined.
        rx = random.random()
        ry = random.random()
        xPos = x1 + ((x2-x1)* rx)
        yPos = y1 + ((y2-y1)* ry)
    
        # Compare this position is far enough away from the old position so that we do not accidently click on ourselves.
        dist = math.hypot(xPos - oldX, yPos - oldY)
        if(abs(dist) > minDistance):
            # If we are far enough away, break the loop and return the coordinates.
            break
        
    # Return the coordinates.
    return {'xPos': xPos, 'yPos': yPos}
    
print('Beginning {0} iterations of Club Penguin coin mining in zone: {1},{2} - {3},{4}  in 5 seconds. Have the Club Penguin browser window open and selected, in the correct position as to align with the inputted mining zone.'.format(numberOfIterations,x1,y1,x2,y2))
time.sleep(5)

for x in range(1, numberOfIterations):
    
    # Find the position we will move the penguin to.
    result = pick_position()
    newXPos = result['xPos']
    newYPos = result['yPos']
    
    oldX = newXPos
    oldY = newYPos
    
    # Move to that position.
    print('Moving to coordinates: {0},{1}  [Iteration number: {2}]'.format(newXPos,newYPos, x))
    mouse.position = (newXPos,newYPos)
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(walktime)

    # Begin digging then wait long enough to mine all possible coins.
    keyboard.press('d')
    keyboard.release('d')
    time.sleep(digtime)
    
print('Finished {0} iterations of coin mining.'.format(numberOfIterations))
    

