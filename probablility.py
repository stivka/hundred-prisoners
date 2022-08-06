import random

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

def recreatePlayerAndBoxNumbers():
    zeroUpTillHundred = list(range(100))
    numbersInsideBoxes = random.sample(zeroUpTillHundred, len(zeroUpTillHundred))
    playersQueue = zeroUpTillHundred


def play(playersQueue, numbersInsideBoxes):

    playerNumber = playersQueue.pop(0)
    numberOfBoxesOpened = 0
    indexOfBoxToOpen = playerNumber

    while playerNumber < 100:

        numberOfBoxesOpened = numberOfBoxesOpened + 1
        numberInBox = numbersInsideBoxes[indexOfBoxToOpen]

        if numberInBox == playerNumber:
            # print('Player ' + str(playerNumber) + ' found their number after opening ' + str(numberOfBoxesOpened) + ' boxes!')
            if len(playersQueue) == 0:
                print('The last of 100 players managed to find their number! All their lives will be spared!') 
                return True
            if len(playersQueue) == 1:
                playerNumber = playersQueue[0]
                playersQueue.clear()
            else:
                playerNumber = playersQueue.pop(0)

            numberOfBoxesOpened = 0
            indexOfBoxToOpen = playerNumber
        elif numberOfBoxesOpened == 50: 
            print('Player ' + str(playerNumber) + ' did not find their number while opening ' + str(numberOfBoxesOpened) + ' boxes. All players shall die!')
            return False    
        else:
            indexOfBoxToOpen = numberInBox

def playNumberOfTimes(number):

    recreatePlayerAndBoxNumbers()

    i = 0
    numberOfWins = 0
    numberOfLosses = 0
    while i < number:
        i = i + 1
        result = play(playersQueue, numbersInsideBoxes)
        if  result == False:
            numberOfLosses = numberOfLosses + 1
        elif result == True:
            numberOfWins = numberOfWins + 1
    print('Number of wins = ' + str(numberOfWins) + ', number of losses = ' + str(numberOfLosses))
        

def printInGrid(numbers):
    for i in range(0, 100):
        if (i % 10 == 0 and i > 9):
            print('\n')
        if numbers[i] < 10:
            print(str(numbers[i]) + ' ', end="  ")
        else :
            print(numbers[i], end="  ")
    print('\n\n')

playNumberOfTimes(100)





