# Roman Numerals (Римские цифры)
# Напишите прогр., которая считывает целое число и выводит соответствующую ему римскую цифру.
# 1 -I  2 - II  3 - III 4 - IV 5 - V 6 - VI 7 - VII 8 - VIII 9 - IX 10 - X

def convert(number):
    if number < 1 or number > 10:
        return "Error.Number should be between 1 and 10."

    msg = ""

    if number <= 3:
        msg = "I" * number
    elif number == 4:
        msg = "IV"
    elif number <= 8:
        msg = "V" + "I" * (number - 5)
    elif number == 9:
        msg = "IX"
    else:
        msg = "X"

    return msg


def main():
    number = int(input("Input the number 1-10 : "))
    print(convert(number))


def testing():
    result = "1 --> I: " + str(convert(1) == "I")
    result += "\n2 --> II: " + str(convert(2) == "II")
    result += "\n3 --> III: " + str(convert(3) == "III")
    result += "\n4 --> IV: " + str(convert(4) == "IV")
    result += "\n5 --> V: " + str(convert(5) == "V")
    result += "\n6 --> VI: " + str(convert(6) == "VI")
    result += "\n7 --> VII: " + str(convert(7) == "VII")
    result += "\n8 --> VIII: " + str(convert(8) == "VIII")
    result += "\n9 --> IX: " + str(convert(9) == "IX")
    result += "\n10 --> X: " + str(convert(10) == "X")

    result += "\n-1 --> Error: " + str(convert(-1) == "Error.Number Number should be between 1 and 10.")
    result += "\n0 --> Error: " + str(convert(0) == "Error.Number Number should be between 1 and 10.")
    result += "\n100 --> Error: " + str(convert(100) == "Error.Number Number should be between 1 and 10.")

    print(result)


testing()
