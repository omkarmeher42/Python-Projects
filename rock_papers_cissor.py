import random

user_wins = 0
computer_wins = 0
options = {
    1 : 'rock',
    2: 'paper',
    3: 'scissors'
}

while True:
    user_input = int(input("\nEnter \n1 -> Rock, 2 -> Paper, 3 -> Scissors or 4 -> Quit: "))
    if user_input == 4:
        break
# Rock : 1, Paper : 2, Scissors : 3
    random_number = random.randint(1,3)
    
    computer_pick = options[random_number]
    user_pick = options[user_input]
    print("You Picked", user_pick + ".")
    print("Computer Picked", computer_pick + ".")
    
    if user_pick=="rock" and computer_pick == "scissors":
        print("You won!")
        user_wins+=1

    elif user_pick=="paper" and computer_pick == "rock":
        print("You won!")
        user_wins+=1

    elif user_pick=="scissors" and computer_pick == "paper":
        print("You won!")
        user_wins+=1

    elif user_pick == computer_pick:
        print("Draw")
        print("No Points")

    else:
        print("You Lost!")
        computer_wins+=1

    
print(f"You Won {user_wins} times.")    
print(f"Computer Won {computer_wins} times.")
    
print("Good Bye!!")

                     