name = input("Welcome to the game, What's ur name? ")
print("Hi " + name + "! Nice to meet you. ")
print("Lets Begin!😇")

'\n'
print("Lets start with simple math")
import random
score = 0
for i in range(5):
    a = random.randint(1,20)
    b = random.randint(1,10)
    answer = a + b
    print("Question", i+1, ":" , a, "+", b, "=")
    guess = int(input("Youw answer: "))
    
    if guess == answer:
        print("Good Job 🤩" , i+1, ":")
        score +=1
    else:
        print("Sorry thats worng but maybe next time")
        
print("you got" , score, "out of 5 correct 👍")

player_choice = input("Do you want to play guess the number (yes/no)? ")

if player_choice.lower() == "yes": 
    print("starting a new game...")
    secret = random.randint(1,20)
    for i in range(4):
        guess = int(input("Guess a number between 1 and 20: "))
        if guess == secret:
            print("got it 😄")
            break
        else:
            print("Nope Not there yet")
        if guess < secret:
            print("too low!")
        elif guess > secret:
            print("too high")
            
    print("Game over it was" , secret ,)
    print("Thats it for today")
else:
    print("No worries.")
    








