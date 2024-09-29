"""Membership Operator
Membership operator is used for searching a given value in collection of values.
Membership operator is represented using one keyword “in”
1. in
2. not in
Membership operator is binary operator and required 2 operands.
Syntax:
<value> in <iterables/collection>"""

name = "Harshal Kharabe"

if "Kharabe" in name:
    print("Oola..!!")
else:
    print("Coca Cola..!!")

number = [1,2,3,4,5,6,7,8,9]

if 31 not in number:
    print("Number is not present")
else :
    print("...")