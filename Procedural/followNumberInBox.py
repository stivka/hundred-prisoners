import random
import os
import sys

verboseLogging = os.getenv('LOG_LEVEL') =='verbose'

n = int(sys.argv[1])
# n = 5

increment = 0
if len(sys.argv) > 2:
    increment = int(sys.argv[2])

# Create set 0-99
zeroUpTillHundred = list(range(100))
# print('The players are numbered 0 - 99 and ready to be sent in\n')
# printInGrid(zeroUpTillHundred)

# Reposition the values in the list so that they do not all have to correspond to their indexes
numbersInsideBoxes = random.sample(zeroUpTillHundred, len(zeroUpTillHundred))
# print('Here is what numbers are hidden within the boxes\n')
# printInGrid(numbersInsideBoxes)

# Create queue of players
playersQueue = zeroUpTillHundred

# def recreatePlayerAndBoxNumbers():
#     zeroUpTillHundred = list(range(100))
#     numbersInsideBoxes = random.sample(zeroUpTillHundred, len(zeroUpTillHundred))
#     playersQueue = zeroUpTillHundred

def play(playersQueue, numbersInsideBoxes):
    
    # in the outer loop, a next player is chosen and given a clean slate
    while len(playersQueue) > 0:
               
        if len(playersQueue) == 1:
                playerNumber = playersQueue[0]
                playersQueue.clear()
        else:
                playerNumber = playersQueue.pop(0)

        numberOfBoxesOpened = 0
        indexOfBoxToOpen = playerNumber
        indexOfBoxToOpen = (playerNumber + increment) % 100

        # in the inner loop, the player opens boxes until they find their number or run out of tries
        while numberOfBoxesOpened <= 50:
            
            numberOfBoxesOpened = numberOfBoxesOpened + 1
            numberInBox = numbersInsideBoxes[indexOfBoxToOpen]

            if numberInBox == playerNumber:
                if (verboseLogging):
                    print('Player ' + str(playerNumber) + ' found their number after opening ' + str(numberOfBoxesOpened) + ' boxes!')
                break
            elif numberOfBoxesOpened == 50:
                if (verboseLogging):
                    print('Player ' + str(playerNumber) + ' did not find their number while opening ' + str(numberOfBoxesOpened) + ' boxes. All players shall die!')
                return False
            else:
                indexOfBoxToOpen = (numberInBox + increment) % 100
    if (verboseLogging):
        print('The last of 100 players managed to find their number! All their lives will be spared!') 
    return True

def init(numberOfTimes):

    i = 0
    numberOfWinsWithOriginalStrategy = 0
    numberOfLossesWithOriginalStrategy = 0
    numberOfWinsWithIncrementStrategy = 0
    numberOfLossesWithIncrementStrategy = 0

    while i < n:
        i = i + 1

        zeroUpTillHundred = list(range(100))
        numbersInsideBoxes = random.sample(zeroUpTillHundred, len(zeroUpTillHundred))
        playersQueue = zeroUpTillHundred

        # Plays two games in succession with the same players and boxes but different strategy
        if increment != 0:
            strategyWithIncrementResult = play(playersQueue, numbersInsideBoxes)
            if  strategyWithIncrementResult == False:
                numberOfLossesWithIncrementStrategy = numberOfLossesWithIncrementStrategy + 1
            elif strategyWithIncrementResult == True:
                numberOfWinsWithIncrementStrategy = numberOfWinsWithIncrementStrategy + 1
        
        originalStrategyResult = play(playersQueue, numbersInsideBoxes)
        if  originalStrategyResult == False:
            numberOfLossesWithOriginalStrategy = numberOfLossesWithOriginalStrategy + 1
        elif originalStrategyResult == True:
            numberOfWinsWithOriginalStrategy = numberOfWinsWithOriginalStrategy + 1
             
    print('Number of wins = ' + str(numberOfWinsWithOriginalStrategy) + ', number of losses = ' + str(numberOfLossesWithOriginalStrategy))
    print('Win probability with original strategy = ' + str(round(numberOfWinsWithOriginalStrategy / (numberOfWinsWithOriginalStrategy + numberOfLossesWithOriginalStrategy) * 100, 2))+ '%')   
    if increment != 0:
        print('Number of wins = ' + str(numberOfWinsWithIncrementStrategy) + ', number of losses = ' + str(numberOfLossesWithIncrementStrategy))
        print('Win probability with increment strategy = ' + str(round(numberOfWinsWithIncrementStrategy / (numberOfWinsWithIncrementStrategy + numberOfLossesWithIncrementStrategy) * 100, 2))+ '%')
        
def printInGrid(numbers):
    for i in range(0, 100):
        if (i % 10 == 0 and i > 9):
            print('\n')
        if numbers[i] < 10:
            print(str(numbers[i]) + ' ', end="  ")
        else :
            print(numbers[i], end="  ")
    print('\n\n') 

init(n)
