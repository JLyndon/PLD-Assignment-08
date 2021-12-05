import random as r
# ----------- CONTEXT ---------------
# Program 1: Lottery
# Create a program that ask 3 numbers (0-9) from the user.
# Generate 3 random winning numbers (0-9)
# Display “Winner” if all 3 input numbers matched the generated numbers
# Display ”You loss” if not
# Display ”Try again y/n” after each game
# If the user enter “y” the user will play again
# if “n” the program will exit.

def InputValidator(Usr_Input):
    if Usr_Input.isdecimal() == True:
        return int(Usr_Input)
    elif (Usr_Input.isalpha() == True) or (Usr_Input.isalnum() == True):
        return print("Input must only be a number!")
    elif (Usr_Input.isspace() == True) or (Usr_Input == None):
        return print("You've typed in an empty value! Please enter a number")
    else:
        if Usr_Input.replace(".", "").isdecimal() == True:
            return print("Input must be a whole number! A fraction cannot be wagered")
        elif "-" and "." in Usr_Input:
            if Usr_Input.replace("-", "").replace(".", "").isdecimal() == True:
                return print("Negative values and fractions cannot be wagered")
        elif "-" in Usr_Input:
            return print("Negative values cannot be wagered")
        else:
            print("Invalid input format")

def BettorChoices(): # Input Prompts
    first_Number = input("Enter first number: ")
    second_Number = input("Enter second number: ")
    third_Number = input("Enter third number: ")
    return first_Number, second_Number, third_Number

def LotteryNumPicker(): # Randomizer Function - Number Generator
    random_no_01 = r.randint(0,9)
    random_no_02 = r.randint(0,9)
    random_no_03 = r.randint(0,9)
    return random_no_01, random_no_02, random_no_03

# Main Prog
Usr_Decision = "proceed"

while Usr_Decision == "proceed":
    LuckyNumbers = list(LotteryNumPicker())
    WagererGuess = list(BettorChoices())
    Usr_Decision = "normalized"
    if sorted(WagererGuess) == sorted(LuckyNumbers):
        print("Winner")
    else:
        print("You loss")
    print("Try again \n y/n")
    while Usr_Decision == "normalized":
        Rpt_Term_Choice = input("\n\n> ").lower()
        if Rpt_Term_Choice == "n":
            Usr_Decision = "exit"
        elif Rpt_Term_Choice == "y":
            Usr_Decision = "proceed"
        else:
            print("Unknown Command")