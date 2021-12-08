import random as r
import time as tm
from NumDecor import DecorWinningNumbers as Decor
# ----------- CONTEXT ---------------
# Program 1: Lottery
# Create a program that ask 3 numbers (0-9) from the user.
# Generate 3 random winning numbers (0-9)
# Display “Winner” if all 3 input numbers matched the generated numbers
# Display ”You loss” if not
# Display ”Try again y/n” after each game
# If the user enter “y” the user will play again
# If “n” the program will exit.

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
                        print("\n", f"{Blue}{Itlc}Did you mean {End}{Yllw}{WholeVal}{End}?".center(48, " "),"\n", f"{Grn}Yes{End} or {Red}No{End}".center(42, " "))
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
        first_Number = input(f"\nEnter {Bldtxt}first{End} number: ")
        if first_Number.replace("-", "").replace(".", "").isdecimal() == True: # Checks whether the string is numeric or not.
            FGuess = NumericChecker(first_Number)                          # Uses NumericChecker if Numeric
            if FGuess == "not_valid":                                      # Uses InputValidator if non-Numeric
                continue
            elif FGuess > 9:
                print(f"{Red}For each input, the number value is limited to {Yllw}0-9{End}")
                continue
            else:
                while True:
                    second_Number = input(f"\nEnter {Bldtxt}second{End} number: ")
                    if second_Number.replace("-", "").replace(".", "").isdecimal() == True:
                        SGuess = NumericChecker(second_Number)
                        if SGuess == "not_valid":
                            continue
                        elif SGuess > 9:
                            print(f"{Red}The number value for this lottery is limited to {Yllw}0-9{End}")
                            continue
                        else:
                            if SGuess == FGuess:
                                print(f"{Red}Numbers cannot have a duplicate{End}")
                                continue
                            else:
                                while True:
                                    third_Number = input(f"\nEnter {Bldtxt}third{End} number: ")
                                    if third_Number.replace("-", "").replace(".", "").isdecimal() == True:
                                        ThGuess = NumericChecker(third_Number)
                                        if ThGuess == "not_valid":
                                            continue
                                        elif ThGuess > 9:
                                            print(f"{Red}The number value for this lottery is limited to {Yllw}0-9{End}")
                                            continue
                                        else:
                                            if (ThGuess == SGuess) or (ThGuess == FGuess):
                                                print(f"{Red}Numbers cannot have a duplicate{End}")
                                                continue
                                            else:
                                                return FGuess, SGuess, ThGuess 
                                                # If all the conditions are met, returns Multiple Values to be compared to the List of Winning Numbers.
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
        if random_number in RandomNumList: # Prevents numbers from repeating
            continue
        else:
            RandomNumList.append(random_number)
    else:
        return RandomNumList

def Decoratives(WinningNums): # Add-on - Decorations; Imports a function from different file. 
    print("\n","\n",f"{Itlc}All in?{End}".center(63, " "),"\n","\n",f"{Grn}Alright!{End}".center(63, " "),"\n",f"Let the lottery begin! {Bldtxt}\33[41m DRAW {End}".center(68, " "),"\n", "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━".center(56, " "))
    tm.sleep(1.3)
    number = 0
    while number <= 2:
        if number == 2:
            print(f"{Itlc}And for the final draw:{End}".center(64, " "))
            tm.sleep(1.6)
        for delay in "..":
            tm.sleep(1)
            print(delay.center(50, " "))
        Decor(WinningNums[number])
        number += 1

# Main Prog
Red = "\33[91m" # Decorative Variable Group
Grn = "\33[92m"
Yllw = "\33[93m"
Blue = "\33[94m"
End = "\33[0m"
Itlc = "\33[3m"
Bldtxt = "\33[1m"

Usr_Decision = "proceed" # Initial Counter - Variable

print("\n",f"Welcome to the \33[41m{Bldtxt} Lottery {End}!".center(71, " "), "\n","━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━".center(60, " "),"\n", f"Place your {Red}risky bets{End}!".center(67, " "), "\n", f"The winning numbers will be drawn {Grn}shortly{End}.".center(70, " "),"\n","\n","\n",f"{Blue}{Itlc}Pick three {End}{Blue}({Grn}3{Blue}) {Itlc}numbers from {End}{Yllw}0-9{End}")

while Usr_Decision == "proceed": # Main Loop
    LuckyNumbers = LotteryNumPicker()
    WagererGuess = list(BettorChoices())
    Usr_Decision = "normalized"
    Decoratives(LuckyNumbers) # Add-on Decor - Uses Function from NumDecor.py
    if sorted(WagererGuess) == sorted(LuckyNumbers):
        print("\n", f"{Grn}{Bldtxt}Winner{End}".center(35, " "))
    else:
        print("\n",f"{Red}You loss{End}".center(36, " "))
    print(f"Try again ( {Grn}y{End}/{Red}n{End} )".center(48, " "),"\n", f"\33[90m━━━━━━━━━━━━━━━━━━━━━━━{End}".center(35, " "))
    while Usr_Decision == "normalized":     # Inner while Loop - for repetition
        Rpt_Term_Choice = input("\n\n> ").lower()
        for charac in Rpt_Term_Choice:
            if charac == "n":
                Usr_Decision = "exit"
            elif charac == "y":
                print("\n\n",f" {Blue}{Itlc}Let's go one more round!{End}")
                print(f"\33[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{End}")
                Usr_Decision = "proceed"
        if Usr_Decision == "normalized":
            print(f"{Red}Unknown Command{End}")

print("\n", f"{Itlc}Have a good day :){End}")
