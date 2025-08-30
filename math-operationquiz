import random
score = 0
count = 0

characters = "+-*/"
for i in range(5):
    operator = random.choice(characters)

    if operator == '+':
        print("Add now")
        
    elif operator == '-':
        print("Sub now")
    elif operator == '*':
        print("Multiply now")
    elif operator == '/':
        print("divide now")
        
    print(operator)


    a = random.randint(1,20)

    b = random.randint(1,20)
    print("Question " + str(i + 1))
    player = input(str(a) + (conjuction) + str(b) + " = " )

    print("u typed: " + player)

    if int(player) == a + b:
        print("Correct 🤩")
        count = count + 1
        print(str(count) + "/" + str(5))
        score = score + 10
    else:
        print("Ur Wrong 😂")
        print(str(count) + "/" + str(5))
        score = score - 5
        
print("Ur Score is " + str(score))
print("You answered" + str(count) + "/" + str(5) + " correctly")

        
print("Game Over 🤗")
    


