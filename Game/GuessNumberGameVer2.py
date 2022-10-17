#Alinkar Lu
#643040818-5

from GuessNumberGameVer1 import GuessNumberGameVer1
from random import randint

class GuessNumberGameVer2(GuessNumberGameVer1):
    def __init__(self, *args, **kwargs):
        super(GuessNumberGameVer2, self).__init__(*args, **kwargs)
        self._guesses = []
        self._numOfGames = 0

    def promptGameMsg(self):
        answer = input(f"If you wanna play again?Type 'y' to continue and 'q' to quit. \n" +
                       f"Type 'a' to see all your guesses or 'g' to see a guess on a specific play: ")
        return answer

    def showGuesses(self):
        print(self._guesses)

    def showSpecific(self):
        
        if self._numGuesses == 1:
            print(self._guesses[0])
        else:
            position = input(f"Enter which guess is in the range [1, {len(self._guesses)}]")
            posVal = int(position)
            print(self._guesses[posVal - 1])

    def checkGuessVal(self, guess):
        guessVal = int(guess)
        if guessVal < self._minNum or guessVal > self._maxNum:
            print(f"Please enter only an integer in the range [{self._minNum},{self._maxNum}]")
            return None
        self._guesses.append(guessVal)
        self._numGuesses = self._numGuesses + 1
        return guessVal

    def playGame(self):
        self._correctNum = randint(self._minNum, self._maxNum)
        self._numGuesses = 0
        self._guesses.clear()
        print(f"GuessNumberGame with min number as {self._minNum},max num as {self._maxNum},max num of tries {self._maxTries}")
        # print("correct =" ,self._correctNum)
        numTries = self._maxTries
        while numTries > 0:
            guess = input(f"Please enter a guess ({self._minNum},{self._maxNum}): ")
            guessVal = self.checkGuessVal(guess)
            if guessVal is None:
                continue
            numTries = numTries - 1
            if guessVal == self._correctNum:
                print("Congratulations!That's correct")
                break
            elif  guessVal > self._correctNum:
                print(f"Please type a lower number!The number of remaining tries is {numTries}")
            elif guessVal < self._correctNum:
                print(f"Please type a higher number!The number of remaining tries is {numTries}")
                
            
        if numTries == 0:
            print (f"Sorry that you run of the number of tries")
        
    def playGames(self):
        self.playGame()
        while True:
            answer = self.promptGameMsg()
            if answer == 'q':
                exit()
            elif answer == 'y':
                self.playGame()
            elif answer == 'a':
                self.showGuesses()
            elif answer == 'g':
                self.showSpecific()


if __name__ == "__main__":
    
    gng2 = GuessNumberGameVer2(2, 8, 1)
    gng2.setMaxTries(3)
    gng2.playGames()
