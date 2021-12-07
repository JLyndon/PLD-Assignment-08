import random as rnd
# ------------- CONTEXT ----------------
# Program 2: Guess the Number
# Generate 1 random number (0-100)
# Ask the user to guess the number
# Display “Greater than” if the inputed number is greater than the random number
# Display “Less than” if the inputed number is less than the random number
# Repeat asking the user until the random number has been guessed correctly.

Red = "\33[91m" # Decorative Variable Group
Grn = "\33[92m"
Yllw = "\33[93m"
Blue = "\33[94m"
End = "\33[0m"
Itlc = "\33[3m"
Bldtxt = "\33[1m"

mysteryNum = rnd.randint(0,100) # Generates a Random Number; serves as 'counter' variable to Loop
                    
while mysteryNum != "guessed": # Continue iteration if the value is unchanged
    Usr_Guess = input("\nGuess the number: ")
    if Usr_Guess.isdecimal() == True:
        if int(Usr_Guess) != mysteryNum:
            if int(Usr_Guess) < mysteryNum: # Display Criteria 1
                print(f"{Red}Less than{End}")
            elif int(Usr_Guess) > mysteryNum: # Display Criteria 2
                print(f"{Grn}Greater than{End}")
        elif int(Usr_Guess) == mysteryNum:
            mysteryNum = "guessed"
    else:
        print(f"{Red}Invalid number{End}")
else:
    print(f"{Bldtxt}{Yllw}Congratulations! You win!{End}m,")