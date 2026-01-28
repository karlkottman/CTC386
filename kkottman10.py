#Karl Kottman
#Lab 10

def FtoC(F):
    C = (F -32) * (5 / 9)
    return C

def quiz_game():
    print("Welcome to the Cities Quiz Game!")
    print("Answer the questions below:")

    questions = {
            "What is the largest city in the world?": "Jakarta",
            "What was the first city in the world?": "Uruk",
            "What is the oldest city that is still inhabited?": "Jericho",
            "What city has the highest elevation?": "La Rinconada",
            "What is the northernmost city in the world?": "Longyearbyen",
            "How many megacities (population > 10 million) does China have?": "18"
    }

    score = 0
    total_questions = len(questions)
    
    for question, answer in questions.items():
        user_answer = input(question).strip().capitalize()

        if user_answer == answer:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer was '{answer}'.")

    print("\nQuiz completed!")
    print(f"You got {score} out of {total_questions} questions correct.")
    print(f"Your final score is {int((score/total_questions) * 100)}&") 


name = input("Please enter your name:")


print("MENU")

print("___________")

print("Option 1")
print("Option 2")
print("Option 3")
print("Option 4")
print("Option 5")
print("Option 6")

print("__________")


print("Hi,", name,"!")
x =int(input("Enter a number to choose an option:"))
if (x == 1):
    print("You chose Option 1,", name,"! Here's a joke!") 
    print("What kind of computer sings the best? ...A Dell.")
elif (x == 2):
    print("You chose Option 2,", name,"!")
    for i in range(15):
        print(name)
elif (x == 3):
    print("You chose Option 3,", name,"!")
    number = int(input("Please enter a whole number:"))
    for i in range(number):
        print("All language is but a poor translation")
elif (x == 4):
    print("You chose Option 4,", name,"!")
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
elif (x == 5):
    print("You chose Option 5,", name,"!")
    F =int(input("Please enter the current temperature in Fahrenheit: "))
    print("It's", (FtoC(F)), "degrees Celsius")
elif (x == 6):
    print("You chose Option 6,", name,"!")
    quiz_game()

