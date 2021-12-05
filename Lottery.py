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
    if ("." not in Usr_Input) and ("-" not in Usr_Input):
        return int(Usr_Input)
    elif ("." in Usr_Input) and ("-" in Usr_Input):
        print("Negative values and fractions cannot be wagered")
        return "not_valid"
    elif "-" or "." in Usr_Input:
        if "." in Usr_Input:
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
        elif "-" in Usr_Input:
            print("Negative values cannot be wagered")
            return "not_valid"
    else:
        InputValidator(Usr_Input)
        return "not_valid"

def InputValidator(EvalueeStr): # Checks Input Eligibility - Separate Function for non-Numeric Input
    if (EvalueeStr.isalpha() == True) or (EvalueeStr.isalnum() == True):
        return print("Input must only be a number!")
    elif (EvalueeStr.isspace() == True) or (EvalueeStr == None) or (EvalueeStr == ""):
        return print("You've typed in an empty value! Please enter a number")
    elif " " in EvalueeStr:
        return print("Inputs must not have a space!")
    else:
        print("Invalid input format")

def BettorChoices(): # Input Prompts
    while True:
        first_Number = input("\nEnter first number: ")
        if first_Number.replace("-", "").replace(".", "").isdecimal() == True: # Checks whether the string is numeric or not.
            FGuess = NumericChecker(first_Number)                          # Uses NumericChecker if Numeric
            if FGuess == "not_valid":                                      # Uses InputValidator if non-Numeric
                continue
            elif FGuess > 9:
                print("For each input, the number value is limited to 9")
                continue
            else:
                while True:
                    second_Number = input("\nEnter second number: ")
                    if second_Number.replace("-", "").replace(".", "").isdecimal() == True:
                        SGuess = NumericChecker(second_Number)
                        if SGuess == "not_valid":
                            continue
                        if SGuess > 9:
                            print("The number value for this lottery is limited to 9")
                            continue
                        else:
                            while True:
                                third_Number = input("\nEnter third number: ")
                                if third_Number.replace("-", "").replace(".", "").isdecimal() == True:
                                    ThGuess = NumericChecker(third_Number)
                                    if ThGuess == "not_valid":
                                        continue
                                    elif ThGuess > 9:
                                        print("The number value for this lottery is limited to 9")
                                        continue
                                    else:
                                        return FGuess, SGuess, ThGuess
                                else:
                                    InputValidator(third_Number)
                    else:
                        InputValidator(second_Number)
        else:
            InputValidator(first_Number)

def LotteryNumPicker(): # Randomizer Function - Number Generator
    RandomNumList = list()
    while len(RandomNumList) <= 2:
        random_number = r.randint(0,9)
        RandomNumList.append(random_number)
    else:
        return RandomNumList

# Main Prog
Usr_Decision = "proceed"

while Usr_Decision == "proceed":
    LuckyNumbers = LotteryNumPicker()
    WagererGuess = list(BettorChoices())
    Usr_Decision = "normalized"
    if sorted(WagererGuess) == sorted(LuckyNumbers):
        print("\n", "Winner".center(38, " "))
    else:
        print("\n","You loss".center(36, " "))
    print("Try again ( y/n )".center(40, " "))
    while Usr_Decision == "normalized":
        Rpt_Term_Choice = input("\n\n> ").lower()
        for charac in Rpt_Term_Choice:
            if charac == "n":
                Usr_Decision = "exit"
            elif charac == "y":
                Usr_Decision = "proceed"
        if Usr_Decision == "normalized":
            print("Unknown Command")
