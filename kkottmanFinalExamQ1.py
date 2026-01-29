#Karl Kottman
#Final Exam Question 1


print("GAME MENU")

print("__________")

print("Option 1")
print("Option 2")
print("Option 3")

print("__________")

x =int(input("Hi! Please enter a number to choose one of the options above:"))
if (x == 1):
    name = input("You chose Option 1. Please enter your name:")
    print("What did", name,"say when they walked into a bar? ...Ouch!")
elif (x == 2):
    print("You chose Option 2. Do you like...")
    for i in range(20):
        print("durian???")
elif (x == 3):
    print("You chose Option 3. Can you guess the number I'm thinking of?")
    x = -1
    while (x != 0):
        x = float(input("Enter a number: "))
        if (x > 0):
            print("Too high! Guess again: ")
        elif (x < 0):
            print("Too low! Guess again: ")
        elif (x == 0):
            print("You got it! I was thinking of 0!")

