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

def BettorChoices():
    first_Number = input("Enter first number: ") 
    second_Number = input("Enter second number: ") 
    third_Number = input("Enter third number: ") 
    return first_Number, second_Number, third_Number

def LotteryNumPicker():
    random_no_01 = r.randint(0,9)
    random_no_02 = r.randint(0,9)
    random_no_03 = r.randint(0,9)
    return random_no_01, random_no_02, random_no_03

Usr_Decision = "proceed"
Rpt_Term_Choice = "y"
while Usr_Decision == "proceed":
    WagererGuess = BettorChoices()
    LuckyNumbers = LotteryNumPicker()
    Usr_Decision = "normalized"
    while Rpt_Term_Choice == "y":
        Rpt_Term_Choice = "_"
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