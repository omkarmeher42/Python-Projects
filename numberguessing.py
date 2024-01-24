import random

print("Number Guessing Game")
print("We have chosen a random number between 1-100 and you have to guess it within 10 tries.")
print("You will also receive feedback on your incorrect guess to help to Guess the correct number")

def game():
    number = random.randrange(1,101)
    tries = 0
    result = 0
    
    while tries <10:
        tries+=1
        guess = int(input("\nEnter your guessed number : "))
        previous = []

        if guess > number:
            previous.append(guess)
            print("Previous Guess = ", previous)
            print("Your Guess it too high!")
        elif guess < number:
            previous.append(guess)
            print("Previous Guess = ", previous)
            print("Your Guess is too low!")
        else:
            result+=1
            print("Congratulations! You got it right!")
        

        if result == 1:
            return result
        
    return result

def main():
    result = game()

    if result != 1:
        print("\nBetter Luck Next Time!")
        print("Try Again.")
        if input("\nWant to play again?(Yes / No) :- ").lower() == 'yes':
            main()
        else:
            quit()
    else:
        print("You Have Won the Game.")
        if input("\nWant to play again?(Yes / No) :- ").lower() == 'yes':
            main()
        else:
            quit()
        

main()