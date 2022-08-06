def openBoxRecursive(playerNumber, playersQueue, boxByIndex, numberOfBoxesOpened):

    if boxByIndex == playerNumber and numberOfBoxesOpened != 0:
        print('Player ' + str(playerNumber) + ' found their number after opening ' + str(numberOfBoxesOpened) + ' boxes!')
        
        playerNumber = playersQueue.pop(0)

        openBoxRecursive(playerNumber, playersQueue, playerNumber, 0)

    if numberOfBoxesOpened == 50:
        print('Player ' + str(playerNumber) + ' did not find their number while opening 50 boxes.')
        return

    numberOfBoxesOpened = numberOfBoxesOpened + 1 
    openBoxRecursive(playerNumber, playersQueue, numbersInsideBoxes[boxByIndex], numberOfBoxesOpened)