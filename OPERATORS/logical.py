"""Logical Operator
Logical operators are used to combine two or more Boolean expressions.
In python logical operators are represented using 3 keywords.

1. and
2. or
3. not

and operator
and is binary operator, it required 2 operands
truth table of and operator

Opr1    Opr2    Opr1 and Opr2
True    True        True
True    False       False
False   True        False
False   False       False

or keyword or operator
“or” operator is binary operator and required 2 operands
Truth table of “or” operator

Opr1    Opr2    Opr1 or Opr2
True    False       True
False   True        True
True    True        True
False   False       False

not keyword or operator
This operator is used with combination of other operators.
It is a unary operator and required one operand
Truth table of “not” operator

opr1    not opr1
True    False
False   True
"""


print("Logical Operators ")

a = int(input("Enter value : "))
b = int(input("Enter value : "))
if a>b and b<1:
    print("Shinal")
else :
    print("Kunal")

a = int(input("Enter value : "))
b = int(input("Enter value : "))
if a>b or b<1:
    print("Shinal")
else :
    print("Kunal")

num = int(input("Enter number : "))
if not num>0:
    print("Negative")
else:
    print("Positive")