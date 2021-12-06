import time
# ----------- CONTEXT --------------
# Decorations for the Lottery.py

def DecorWinningNumbers(LuckyNumValue):
    NumberDecor = ""
    time.sleep(1)
    if LuckyNumValue == 2:
        for row_1 in range(0, 7):
            for column_1 in range(0, 40):
                if (column_1 == 21 and (row_1 == 1 or (row_1 >= 3 and row_1 <= 6))) or (column_1 == 22 and (row_1 == 1 or (row_1 >= 3 and row_1 <= 6))) or (column_1 == 23 and (row_1 == 1 or row_1 == 3 or row_1 == 6)) or (column_1 == 24 and (row_1 == 1 or row_1 == 3 or row_1 == 6)) or (column_1 == 25 and (row_1 == 1 or row_1 == 3 or row_1 == 6)) or (column_1 == 26 and (row_1 == 1 or row_1 == 3 or row_1 == 6)) or (column_1 == 27 and ((row_1 >= 1 and row_1 <= 3) or row_1 == 6)) or (column_1 == 28 and (row_1 == 6 or (row_1 >= 1 and row_1 <= 3))):
                    NumberDecor = NumberDecor  + "\33[91m▮\33[0m"
                else:
                    NumberDecor = NumberDecor + " "
            NumberDecor = NumberDecor + "\n"
        return print(NumberDecor)
    elif LuckyNumValue == 1:
        for row_1 in range(0, 7):
            for column_1 in range(0, 40):
                if (column_1 == 23 and (row_1 == 1 or row_1 == 6)) or (column_1 == 24 and (row_1 == 1 or row_1 == 6)) or (column_1 == 25 and (row_1 >= 1 and row_1 <= 6)) or (column_1 == 26 and (row_1 >= 1 and row_1 <= 6)) or (column_1 == 27 and row_1 == 6):
                    NumberDecor = NumberDecor  + "\33[91m▮\33[0m"
                else:
                    NumberDecor = NumberDecor + " "
            NumberDecor = NumberDecor + "\n"
        return print(NumberDecor)
    elif LuckyNumValue == 3:
        for row_1 in range(0, 7):
            for column_1 in range(0, 40):
                if (column_1 == 21 and (row_1 == 1 or row_1 == 6 or row_1 == 3)) or (column_1 == 22 and (row_1 == 1 or row_1 == 6 or row_1 == 3)) or (column_1 == 23 and (row_1 == 1 or row_1 == 6 or row_1 == 3)) or (column_1 == 24 and (row_1 == 1 or row_1 == 6 or row_1 == 3)) or (column_1 == 25 and (row_1 == 1 or row_1 == 6 or row_1 == 3)) or (column_1 == 26 and (row_1 == 1 or row_1 == 6 or row_1 == 3)) or (column_1 == 27 and ((row_1 >= 1 and row_1 <= 6) or row_1 == 3)) or (column_1 == 28 and ((row_1 >= 1 and row_1 <= 6) or row_1 == 3)):
                    NumberDecor = NumberDecor  + "\33[91m▮\33[0m"
                else:
                    NumberDecor = NumberDecor + " "
            NumberDecor = NumberDecor + "\n"
        return print(NumberDecor)
    elif LuckyNumValue == 4:
        for row_1 in range(0, 7):
            for column_1 in range(0, 40):
                if (column_1 == 21 and (row_1 >= 1 and row_1 <= 4)) or (column_1 == 22 and (row_1 >= 1 and row_1 <= 4)) or (column_1 == 23 and row_1 == 4) or (column_1 == 24 and row_1 == 4) or (column_1 == 25 and row_1 == 4) or (column_1 == 26 and row_1 == 4) or (column_1 == 27 and (row_1 >= 1 and row_1 <= 6)) or (column_1 == 28 and (row_1 >= 1 and row_1 <= 6)) or (column_1 == 29 and row_1 == 4):
                    NumberDecor = NumberDecor  + "\33[91m▮\33[0m"
                else:
                    NumberDecor = NumberDecor + " "
            NumberDecor = NumberDecor + "\n"
        return print(NumberDecor)
    elif LuckyNumValue == 5:
        for row_1 in range(0, 7):
            for column_1 in range(0, 40):
                if (column_1 == 21 and ((row_1 >= 1 and row_1 <= 3) or row_1 == 6)) or (column_1 == 22 and ((row_1 >= 1 and row_1 <= 3) or row_1 == 6)) or (column_1 == 23 and (row_1 == 1 or row_1 == 3 or row_1 == 6)) or (column_1 == 24 and (row_1 == 1 or row_1 == 3 or row_1 == 6)) or (column_1 == 25 and (row_1 == 1 or row_1 == 3 or row_1 == 6)) or (column_1 == 26 and (row_1 == 1 or row_1 == 3 or row_1 == 6)) or (column_1 == 27 and ((row_1 >= 3 and row_1 <= 6) or row_1 == 6 or row_1 == 1)) or (column_1 == 28 and ((row_1 >= 3 and row_1 <= 6) or row_1 == 6 or row_1 == 1)):
                    NumberDecor = NumberDecor  + "\33[91m▮\33[0m"
                else:
                    NumberDecor = NumberDecor + " "
            NumberDecor = NumberDecor + "\n"
        return print(NumberDecor)
    elif LuckyNumValue == 6:
        for row_1 in range(0, 7):
            for column_1 in range(0, 40):
                if (column_1 == 21 and (row_1 >= 1 and row_1 <= 6)) or (column_1 == 22 and (row_1 >= 1 and row_1 <= 6)) or (column_1 == 23 and (row_1 == 1 or row_1 == 3 or row_1 == 6)) or (column_1 == 24 and (row_1 == 1 or row_1 == 3 or row_1 == 6)) or (column_1 == 25 and (row_1 == 1 or row_1 == 3 or row_1 == 6)) or (column_1 == 26 and (row_1 == 1 or row_1 == 3 or row_1 == 6)) or (column_1 == 27 and ((row_1 >= 3 and row_1 <= 6) or row_1 == 6 or row_1 == 1)) or (column_1 == 28 and ((row_1 >= 3 and row_1 <= 6) or row_1 == 6 or row_1 == 1)):
                    NumberDecor = NumberDecor  + "\33[91m▮\33[0m"
                else:
                    NumberDecor = NumberDecor + " "
            NumberDecor = NumberDecor + "\n"
        return print(NumberDecor)
    elif LuckyNumValue == 7:
        for row_1 in range(0, 7):
            for column_1 in range(0, 40):
                if (column_1 == 21 and row_1 == 1) or (column_1 == 22 and row_1 == 1) or (column_1 == 23 and row_1 == 1) or (column_1 == 24 and row_1 == 1) or (column_1 == 25 and row_1 == 1) or (column_1 == 26 and row_1 == 1) or (column_1 == 27 and (row_1 >= 1 and row_1 <= 6)) or (column_1 == 28 and (row_1 >= 1 and row_1 <= 6)):
                    NumberDecor = NumberDecor  + "\33[91m▮\33[0m"
                else:
                    NumberDecor = NumberDecor + " "
            NumberDecor = NumberDecor + "\n"
        return print(NumberDecor)
    elif LuckyNumValue == 8:
        for row_1 in range(0, 7):
            for column_1 in range(0, 40):
                if (column_1 == 21 and (row_1 >= 1 and row_1 <= 6)) or (column_1 == 22 and (row_1 >= 1 and row_1 <= 6)) or (column_1 == 23 and (row_1 == 1 or row_1 == 3 or row_1 == 6)) or (column_1 == 24 and (row_1 == 1 or row_1 == 3 or row_1 == 6)) or (column_1 == 25 and (row_1 == 1 or row_1 == 3 or row_1 == 6)) or (column_1 == 26 and (row_1 == 1 or row_1 == 3 or row_1 == 6)) or (column_1 == 27 and (row_1 >= 1 and row_1 <= 6)) or (column_1 == 28 and (row_1 >= 1 and row_1 <= 6)):
                    NumberDecor = NumberDecor  + "\33[91m▮\33[0m"
                else:
                    NumberDecor = NumberDecor + " "
            NumberDecor = NumberDecor + "\n"
        return print(NumberDecor)
    elif LuckyNumValue == 9:
        for row_1 in range(0, 7):
            for column_1 in range(0, 40):
                if (column_1 == 21 and ((row_1 >= 1 and row_1 <= 4) or row_1 == 6)) or (column_1 == 22 and ((row_1 >= 1 and row_1 <= 4) or row_1 == 6)) or (column_1 == 23 and (row_1 == 1 or row_1 == 4 or row_1 == 6)) or (column_1 == 24 and (row_1 == 1 or row_1 == 4 or row_1 == 6)) or (column_1 == 25 and (row_1 == 1 or row_1 == 4 or row_1 == 6)) or (column_1 == 26 and (row_1 == 1 or row_1 == 4 or row_1 == 6)) or (column_1 == 27 and (row_1 >= 1 and row_1 <= 6)) or (column_1 == 28 and (row_1 >= 1 and row_1 <= 6)):
                    NumberDecor = NumberDecor  + "\33[91m▮\33[0m"
                else:
                    NumberDecor = NumberDecor + " "
            NumberDecor = NumberDecor + "\n"
        return print(NumberDecor)
    elif LuckyNumValue == 0:
        for row_1 in range(0, 7):
            for column_1 in range(0, 40):
                if (column_1 == 21 and (row_1 >= 1 and row_1 <= 6)) or (column_1 == 22 and (row_1 >= 1 and row_1 <= 6)) or (column_1 == 23 and (row_1 == 1 or row_1 == 6)) or (column_1 == 24 and (row_1 == 1 or row_1 == 6)) or (column_1 == 25 and (row_1 == 1 or row_1 == 6)) or (column_1 == 26 and (row_1 == 1 or row_1 == 6)) or (column_1 == 27 and (row_1 >= 1 and row_1 <= 6)) or (column_1 == 28 and (row_1 >= 1 and row_1 <= 6)):
                    NumberDecor = NumberDecor  + "\33[91m▮\33[0m"
                else:
                    NumberDecor = NumberDecor + " "
            NumberDecor = NumberDecor + "\n"
        return print(NumberDecor)