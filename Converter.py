values_dictionary = {
    900: "CM",
    500: "D",
    400: "CD",
    90: "XC",
    50: "L",
    40: "XL",
    9: "IX",
    5: "V",
    4: "IV",
}


def __main__(number_string):
    number_string = (4 - number_string.__len__()) * "0" + number_string

    if 0 < int(number_string) <= 3000:
        thousands = int(number_string[0])
        hundreds = int(number_string[1])
        tens = int(number_string[2])
        ones = int(number_string[3])

        result = ""

        result += "M" * thousands

        if 5 < hundreds < 9:
            result += "C" * (hundreds - 5) + "D"
        elif hundreds < 4:
            result += "C" * hundreds
        else:
            result += values_dictionary[hundreds * 100]

        if 5 < tens < 9:
            result += "L" + "X" * (tens - 5)
        elif tens < 4:
            result += "X" * tens
        else:
            result += values_dictionary[tens * 10]

        if 5 < ones < 9:
            result += "V" + "I" * (ones - 5)
        elif ones < 4:
            result += "I" * ones
        else:
            result += values_dictionary[ones * 1]

        print(result)
    else:
        print("Invalid number")
