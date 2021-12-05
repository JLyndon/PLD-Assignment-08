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

def NumericChecker(Usr_Input): # Checks Input Eligibility - Separate Function for Numeric Input
    if "-" and "." not in Usr_Input:
        return int(Usr_Input)
    elif "." in Usr_Input:
        WholeVal, Fraction = Usr_Input.split(".")
        if ((Fraction == None) or (Fraction == "")) or (Fraction.isspace() == True) or (int(Fraction) == 0): # Verification - Clarify if the User is including the decimal as input and convert if not.
            print(f"Did you mean {WholeVal}? \n    Yes or No")
            while True:
                VerifyUsr = input("\n> ").lower()
                for char in VerifyUsr:
                    if char == "y":
                        return int(WholeVal)
                    elif char == "n":
                        print("Input must be a whole number! A fraction cannot be wagered")
                        return "not_valid"
        elif int(Fraction) > 0:
            print("Input must be a whole number! A fraction cannot be wagered")
            return "not_valid"
    elif "-" and "." in Usr_Input:
        if Usr_Input.replace("-", "").replace(".", "").isdecimal() == True:
            print("Negative values and fractions cannot be wagered")
            return "not_valid"
    elif "-" in Usr_Input:
        print("Negative values cannot be wagered")
        return "not_valid"
    else:
        print("Invalid input format")
        return "not_valid"

def InputValidator(EvalueeStr): # Checks Input Eligibility - Separate Function for non-Numeric Input
    if (EvalueeStr.isalpha() == True) or (EvalueeStr.isalnum() == True):
        return print("Input must only be a number!")
    elif (EvalueeStr.isspace() == True) or (EvalueeStr == None):
        return print("You've typed in an empty value! Please enter a number")
    elif " " in EvalueeStr:
        return print("Inputs must not have a space!")
    else:
        print("Invalid input format")

def BettorChoices(): # Input Prompts
    while True:
        first_Number = input("\nEnter first number: ")
        if (first_Number.isdecimal() == True) or ("-" or "." in first_Number):
            FGuess = NumericChecker(first_Number)
            if FGuess == "not_valid":
                continue
            else:
                while True:
                    second_Number = input("\nEnter second number: ")
                    if (second_Number.isdecimal() == True) or ("-" or "." in second_Number):
                        SGuess = NumericChecker(second_Number)
                        while True:
                            third_Number = input("\nEnter third number: ")
                            if (third_Number.isdecimal() == True) or ("-" or "." in third_Number):
                                ThGuess = NumericChecker(third_Number)
                                return FGuess, SGuess, ThGuess
                            else:
                                InputValidator(third_Number)
                    else:
                        InputValidator(second_Number)
        else:
            InputValidator(first_Number)

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