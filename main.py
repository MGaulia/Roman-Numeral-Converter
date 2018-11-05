import Converter
import Deconverter
print("Choose:")
print("1.V to 5 ")
print("2.5 to V \n")
choice = input()
try:
    int(choice)
    if choice == "1":
        roman_string = input("Enter roman string\n")
        Deconverter.__main__(roman_string)
    elif choice == "2":
        number_string = input("Enter number between 1 and 3000\n")
        Converter.__main__(number_string)
    else:
        print("Invalid choice")
except:
    print("Invalid choice")



