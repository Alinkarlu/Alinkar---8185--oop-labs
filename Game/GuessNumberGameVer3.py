from GuessNumberGameVer2 import GuessNumberGameVer2

class GuessNumberGameVer3(GuessNumberGameVer2):
    def __init__(self, *args, **kwargs):
        super(GuessNumberGameVer3, self).__init__(*args, **kwargs)
        self._validChoices = ['y','q','a','g','v','m','x']
    
    def promptGameMsg(self):
        answer = input(f"If you want to play again? type 'y' to continue or 'q' to quit.\n"+
                       f"Type 'a' to see all your guesses or 'g' to see a specific play.\n"+
                       f"Type 'v' to see average or 'm' to see maximum of all your guesses.\n")
        answer = answer.lower()
        if answer in self._validChoices:
            return answer
        else:
            return None

    def guessAverage(self):
        print(f"Average = {sum(self._guesses) / self._numGuesses:0.02f}")
    
    def guessMin(self):
        print(f"Min = {min(self._guesses)}")

    def guessMax(self):
        print(f"Max = {max(self._guesses)}")
    
    def playGames(self):
        self.playGame()
        while True:
            answer = self.promptGameMsg()
            if answer == 'q':
                break
            elif answer == 'y':
                self.playGame()
            elif answer == 'a':
                self.showGuesses()
            elif answer == 'g':
                self.showSpecific()
            elif answer == 'v':
                self.guessAverage()
            elif answer == 'm':
                self.guessMin()
            elif answer == 'x':
                self.guessMax()


if __name__ == "__main__":
    gng1 = GuessNumberGameVer3(5, 10, 2)
    gng1.playGames()





