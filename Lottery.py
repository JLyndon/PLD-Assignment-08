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
    else:
        if (Usr_Input.count("-") == 1) and (Usr_Input.count(".") == 1):
            if ("." in Usr_Input) and ("-" in Usr_Input):
                print(f"{Red}Negative values and fractions cannot be wagered{End}")
                return "not_valid"
        elif (Usr_Input.count("-") <= 1) and (Usr_Input.count(".") <= 1):
            if "-" or "." in Usr_Input:
                if "." in Usr_Input:
                    WholeVal, Fraction = Usr_Input.split(".")
                    if ((Fraction == None) or (Fraction == "")) or (Fraction.isspace() == True) or (int(Fraction) == 0): # Verification - Clarify if the User is including the decimal as input and convert if not.
                        print(f"{Blue}{Itlc}Did you mean {End}{Yllw}{WholeVal}{End}?".center(48, " "),"\n", f"{Grn}Yes{End} or {Red}No{End}".center(40, " "))
                        while True:
                            VerifyUsr = input("\n> ").lower()
                            for char in VerifyUsr:
                                if char == "y":
                                    return int(WholeVal)
                                elif char == "n":
                                    print(f"{Red}Input must be a whole number! A fraction cannot be wagered{End}")
                                    return "not_valid"
                            print(f"{Red}Unknown command{End}")
                    elif int(Fraction) > 0:
                        print(f"{Red}Input must be a whole number! A fraction cannot be wagered{End}")
                        return "not_valid"
                elif "-" in Usr_Input:
                    print(f"{Red}Negative values cannot be wagered{End}")
                    return "not_valid"
        else:
            print(f"{Red}Invalid input format{End}")
            return "not_valid"

def InputValidator(EvalueeStr): # Checks Input Eligibility - Separate Function for non-Numeric Input
    if (EvalueeStr.isalpha() == True) or (EvalueeStr.isalnum() == True):
        return print(f"{Red}Input must only be a number!{End}")
    elif (EvalueeStr.isspace() == True) or (EvalueeStr == None) or (EvalueeStr == ""):
        return print(f"{Red}You've typed in an empty value! Please enter a number{End}")
    elif " " in EvalueeStr:
        return print(f"{Red}Inputs must not have a space!{End}")
    else:
        print(f"{Red}Invalid input format{End}")

def BettorChoices(): # Input Prompts
    while True:
        first_Number = input("\nEnter first number: ")
        if first_Number.replace("-", "").replace(".", "").isdecimal() == True: # Checks whether the string is numeric or not.
            FGuess = NumericChecker(first_Number)                          # Uses NumericChecker if Numeric
            if FGuess == "not_valid":                                      # Uses InputValidator if non-Numeric
                continue
            elif FGuess > 9:
                print("For each input, the number value is limited to 0-9")
                continue
            else:
                while True:
                    second_Number = input("\nEnter second number: ")
                    if second_Number.replace("-", "").replace(".", "").isdecimal() == True:
                        SGuess = NumericChecker(second_Number)
                        if SGuess == "not_valid":
                            continue
                        if SGuess > 9:
                            print("The number value for this lottery is limited to 0-9")
                            continue
                        else:
                            if SGuess == FGuess:
                                print(f"{Red}Numbers cannot have a duplicate{End}")
                                continue
                            else:
                                while True:
                                    thiRed_Number = input("\nEnter third number: ")
                                    if thiRed_Number.replace("-", "").replace(".", "").isdecimal() == True:
                                        ThGuess = NumericChecker(thiRed_Number)
                                        if ThGuess == "not_valid":
                                            continue
                                        elif ThGuess > 9:
                                            print("The number value for this lottery is limited to 0-9")
                                            continue
                                        else:
                                            if (ThGuess == SGuess) or (ThGuess == FGuess):
                                                print(f"{Red}Numbers cannot have a duplicate{End}")
                                                continue
                                            else:
                                                return FGuess, SGuess, ThGuess 
                                                # If all the conditions are met, returns Multiple Values to be compared to the List of Winning Numbers.
                                    else:
                                        InputValidator(thiRed_Number)
                    else:
                        InputValidator(second_Number)
        else:
            InputValidator(first_Number)

def LotteryNumPicker(): # Randomizer Function - Number Generator
    RandomNumList = list()
    while len(RandomNumList) <= 2:
        random_number = r.randint(0,9)
        if random_number in RandomNumList: # Prevents numbers from repeating
            continue
        else:
            RandomNumList.append(random_number)
    else:
        return RandomNumList

# Main Prog
Red = "\33[91m"
Grn = "\33[92m"
Yllw = "\33[93m"
Blue = "\33[94m"
End = "\33[0m"
Itlc = "\33[3m"

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
