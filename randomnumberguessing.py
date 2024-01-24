import random

while True :
    top_of_range = input("Enter a Number :- ")
    if top_of_range.isdigit():
        top_of_range = int(top_of_range)
        if top_of_range <= 0:
            print("Please Enter a Number Greater than 0.")
        else:
            break
    else:
        print("Please Enter a Number greator than 0.")


random_number = random.randrange(1,top_of_range+1)
guesses = 0

while True:
    guesses+=1

    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please Enter a Number next time.")
        continue

    if user_guess ==  random_number:
        print("You got it Correct!")
        break
    elif user_guess < random_number:
        print("Your guess is too low")
    else:
        print("Your guess is too high.")
    
print("You got it in", guesses,"guesses" )

