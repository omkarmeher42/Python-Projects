print("Welcome to My Computer Quiz!")
#Starting the quiz
playing = input("Do you want to play(Enter yes/no)? ")

#if not yes, quit the game
if playing.lower() != "yes":
    quit()
print("Okay! Let's Play :) ")

#Track the score of player
score = 0

#q1
ans = input("What is the Capital of India? ")
if ans.lower() == "delhi":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

#q2
ans = input("What is the National Animal of India? ")
if ans.lower() == "tiger":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

#q3
ans = input("What is the Capital of Maharashtra? ")
if ans.lower() == "mumbai":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

#q4
ans = input("Who is the current Prime Minister of India? ")
if ans.lower() == "narendra modi":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

#q5
ans = input("What is the National Flower of India? ")
if ans.lower() == "lotus":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

#Result
print("You got " + str(score) + " out of 5 questions correct!")
print(f"you got {(score / 5)*100}%.")