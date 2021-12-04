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

print("Try again \n y/n")

WagererGuess = BettorChoices()
LuckyNumbers = LotteryNumPicker()

if sorted(WagererGuess) == sorted(LuckyNumbers):
    print("Winner")
else:
    print("You loss")