def playCrappierAlgo(playersQueue, numbersInsideBoxes):

    playerNumber = playersQueue.pop(0)
    numberOfBoxesOpened = 0
    indexOfBoxToOpen = playerNumber

    while len(playersQueue) > 0:

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