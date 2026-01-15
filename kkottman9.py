#Karl Kottman
#GitHub Test

name = input("Please enter your name:")


print("MENU")

print("___________")

print("Option 1")
print("Option 2")
print("Option 3")
print("Option 4")
print("Option 5")

print("__________")


print("Hi,", name,"!")
x =int(input("Enter a number to choose an option:"))
if (x == 1):
    print("What kind of computer sings the best? ...A Dell.")
if (x == 2):
    for i in range(15):
        print(name)
if (x == 3):
    number = int(input("Please enter a whole number:"))
    for i in range(number):
        print("All language is but a poor translation")
if (x == 4):
    print("I'm thinking of a number between 0 and 100 inclusive. Can you guess it?")
    x = 0
    while (x != 44):
        x = float(input("Enter a number: "))
        if (x > 44) and (x <= 100):
            print("Too high! Guess again: ")
        elif (x >= 0) and (x < 44):
            print("Too low! Guess again: ")
        elif (x < 0) or (x > 100):
            print("Your guess was out of range. Please enter a number between 0 and 100 inclusive: ")
        elif (x == 44):
            print("That's it! The number is 44!")
if (x == 5):
    F =int(input("Please enter the current temperature in Fahrenheit: "))
    def FtoC(F):
        C = (F - 32) * (5 / 9)
        return C
    print("It's", (FtoC(F)), "degrees Celsius")

