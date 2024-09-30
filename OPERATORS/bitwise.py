"""Bitwise Operator
Bitwise operators are used to perform operation on binary data (bits).
1. Shift Operators
a. Rightshift operator &gt;&gt;
b. Leftshift operator &lt;&lt;
2. Bitwise &amp; (and) operator
3. Bitwise | (or) operator
4. Bitwise ^ (xor) operator
5. Bitwise ~ (not) operator
Shift Operators
Shift operators are used to shift bits towards left side or right side.
1. Right shift operator
2. Left shift operator
Shift operators are used,
1. Adding or Removing bits
2. Memory Management"""

"""Right shift operator
This operator is used for shifting number of bits towards right side.
Right shift operator is used to delete or remove bits.
Syntax: opr>>n"""

a = 0b1010
print("Right shift in binary : ",bin(a>>2))
print("Right shift in decimal : ",a>>2)

"""Left shift operator
Left shift operator is used to shift number bits towards left side.
By shifting number of bits towards left side the value get incremented by adding
bits at right side.
Syntax: opr<<n"""

a = 0b1010
print("Left shift in binary : ",bin(a<<2))
print("Left shift in decimal : ",a<<2)