import random as rnd
# ------------- CONTEXT ----------------
# Program 2: Guess the Number
# Generate 1 random number (0-100)
# Ask the user to guess the number
# Display “Greater than” if the inputed number is greater than the random number
# Display “Less than” if the inputed number is less than the random number
# Repeat asking the user until the random number has been guessed correctly.

mysteryNum = rnd.randint(0,100)

while mysteryNum != "guessed":
    Usr_Guess = input("Guess the number: ")
    if Usr_Guess.isdecimal() == True:
        if int(Usr_Guess) != mysteryNum:
            if int(Usr_Guess) < mysteryNum:
                print("Less than")
            elif int(Usr_Guess) > mysteryNum:
                print("Greater than")
        elif int(Usr_Guess) == mysteryNum:
            mysteryNum = "guessed"
    else:
        print("Invalid number")
else:
    print("Congratulations! You win!")