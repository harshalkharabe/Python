"""match..case statement is introduced in python 3.10 version.
match..case is similar to switch..case in C,C++ and Java languages.
match is soft keyword.
A match statement takes an expression and compares its value to
successive patterns given as one or more case blocks. 
Syntax:
match expression:
    case pattern1:
        statement-1
    case pattern2:
        statement-2
    case pattern3:
        statement-3
    case _:
        statement-4"""

#WAP TO FIND CORRECT DAY IN WEEK
day = input("Enter day :")
match day.upper():
    case "MONDAY":
        print(f"Today is {day}")
    case "TUESDAY":
        print(f"Today is {day}")
    case "WEDNUSDAY":
        print(f"Today is {day}")
    case "THUSDAY":
        print(f"Today is {day}")
    case "FRIDAY":
        print(f"Today is {day}")
    case "SATURDAY":
        print(f"Today is {day}")
    case _:
        print("Sunday")