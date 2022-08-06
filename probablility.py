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

        # in the inner loop, the player opens boxes until they find their number or run out of tries
        while numberOfBoxesOpened <= 50:
            
            numberOfBoxesOpened = numberOfBoxesOpened + 1
            numberInBox = numbersInsideBoxes[indexOfBoxToOpen]

            if numberInBox == playerNumber:
                # print('Player ' + str(playerNumber) + ' found their number after opening ' + str(numberOfBoxesOpened) + ' boxes!')
                break
            elif numberOfBoxesOpened == 50:
                print('Player ' + str(playerNumber) + ' did not find their number while opening ' + str(numberOfBoxesOpened) + ' boxes. All players shall die!')
                return False
            else:
                indexOfBoxToOpen = numberInBox
    
    print('The last of 100 players managed to find their number! All their lives will be spared!') 
    return True

def playNumberOfTimes(number):

    i = 0
    numberOfWins = 0
    numberOfLosses = 0
    while i < number:
        i = i + 1

        zeroUpTillHundred = list(range(100))
        numbersInsideBoxes = random.sample(zeroUpTillHundred, len(zeroUpTillHundred))
        playersQueue = zeroUpTillHundred
        
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
