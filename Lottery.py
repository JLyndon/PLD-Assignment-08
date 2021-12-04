import random
# ----------- CONTEXT ---------------
# Program 1: Lottery
# Create a program that ask 3 numbers (0-9) from the user.
# Generate 3 random winning numbers (0-9)
# Display “Winner” if all 3 input numbers matched the generated numbers
# Display ”You loss” if not
# Display ”Try again y/n” after each game
# If the user enter “y” the user will play again
# if “n” the program will exit.

first_Number = input("Enter first number: ") 
second_Number = input("Enter second number: ") 
third_Number = input("Enter third number: ") 

random_no_01 = random.randint(0-9)
random_no_02 = random.randint(0-9)

print("Winner")
print("You loss")
print("Try again \n y/n")