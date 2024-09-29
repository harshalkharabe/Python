"""Conditional Operators
Conditional operators are used to create conditional expression.
Conditional operators are used to evaluate expression based on condition
or Boolean expression.
Conditional operator is a ternary operator and required 3 operands.

Syntax:
<variable>=opr1 if opr2 else opr3 (OR)
<variable>=<true-expression> if <condition> else <false-expression>
Evaluation of expression is done based on condition
If condition is True, Python evaluate true-expression and assign result to
variable
If condition is False, Python evaluate false-expression and assign to result
to variable.
"""

# Write a program to find max of two integers
n1=int(input("Enter First Integer "))
n2=int(input("Enter Second Integer "))
n3=n1 if n1>n2 else n2
print("maximum of ",n1,n2,"is",n3)