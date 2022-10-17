#Alinkar Lu
#643040818-5
from random import randint

class GuessNumberGameVer1:
    #class attribute
    _numOfGames = 0

    def __init__(self, minNum=1, maxNum=10, maxTries=3):
        self._minNum = minNum #instance attribute
        self._maxNum = maxNum
        self._maxTries = maxTries
        self._correctNum = randint(self._minNum, self._maxNum)
        GuessNumberGameVer1._numOfGames = GuessNumberGameVer1._numOfGames + 1

    def setMinNum(self, minNum):
        self._minNum = minNum

    def getMinNum(self):
        return self._minNum

    def setMaxNum(self, maxNum):
        self._maxNum = maxNum

    def getMaxNum(self):
        return self._maxNum

    def setMaxTries(self, maxTries):
        self._maxTries = maxTries

    def getMaxTries(self):
        return self._maxTries

    def playGame(self):
        print(f"GuessNumberGame with min number as {self._minNum} max number as  {self._maxNum}, max num of tries as {self._maxTries}")
        numTries = self._maxTries
        while numTries > 0:
            guessNumber = input(f"Please enter a guess ({self._minNum}, {self._maxNum}):")
            guessNumberVal = int(guessNumber)
            numTries = numTries - 1
            if guessNumberVal == self._correctNum:
                print(f"Congratulations! That's correct")
                exit()
            elif guessNumberVal > self._correctNum:
                print(f"Please type a lower number! The number of remaining tries is {numTries}")
            elif guessNumberVal < self._correctNum:
                print(f"Please type a higher number! The number of remaining tries is {numTries}")
        if numTries == 0:
            print(f"Sorry that you run of the number of tries")

    @classmethod
    def getNumOfGames(cls):
        return GuessNumberGameVer1._numOfGames

    def __str__(self):
        return f"GuessNumberGame:({self._minNum}, {self._maxNum}, {self._maxTries})"

if __name__ == "__main__":
    gng1 = GuessNumberGameVer1()
    gng2 = GuessNumberGameVer1(5, 8)
    gng3 = GuessNumberGameVer1(5, 8, 4)
    print(gng3)
    print(f"The current number of game is {GuessNumberGameVer1.getNumOfGames()}")
    gng3.playGame()      