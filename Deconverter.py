import itertools

values_dictionary={
    "M":1000,
    "CM":900,
    "D":500,
    "CD":400,
    "C":100,
    "XC":90,
    "L":50,
    "XL":40,
    "X":10,
    "IX":9,
    "V":5,
    "IV":4,
    "I":1
}
def valid_roman_string(roman_string):
    for letter_combos in [''.join(value) for key, value in itertools.groupby(roman_string)]:
        if letter_combos.__len__()>3:
            return False
    if roman_string.__len__() != 0:
        try:
            [values_dictionary[letter] for letter in roman_string]
        except:
            return False
    return True


def __main__(roman_string):
    value = 0
    if valid_roman_string(roman_string):
        index=0
        while index < roman_string.__len__():
             try:
                 value+=values_dictionary[roman_string[index] + roman_string[index + 1]]
                 index+=2
             except:
                 value+=values_dictionary[roman_string[index]]
                 index+=1
        print(value)
    else:
        print("Invalid string")

