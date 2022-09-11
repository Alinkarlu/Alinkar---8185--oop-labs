import random 
numbers = range(1,11)
numberfind = random.choice(numbers)
tries = 4

while tries > 0:
    guess = input("Enter an integer to guess: ")
    try:
        guess = float(guess)
        if guess == numberfind:
            print("Congrats that you get the number correctly")
            exit()
        elif guess > numberfind and guess > 1 and guess <= 10:
            tries -= 1
            print("You have", (tries), "guesses remaining")
            print("Try a lower number")
        elif guess < numberfind and guess > 1 and guess <= 10:
            tries -= 1
            print("You have", (tries), "guesses remaining")
            print("Try a higher number")
        elif tries == 0:
            print("Sorry, you are out of tries, feel free to try again.")
        else:
            print("Please guess with an integer in the range [1,10]")   
    except ValueError:
        print("Please enter an integer to guess")

# Name = Alinkar Lu
# Student_ID = 643040818-5


