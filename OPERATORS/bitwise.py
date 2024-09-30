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

"""Logic Gates
A logic gate is a device that performs a Boolean function, a logical
operation performed on one or more binary inputs that produces a single
binary output.
A logic gate is a device that acts as a building block for digital circuits. They
perform basic logical functions that are fundamental to digital circuits.
These operations are done using bitwise operators
1. Bitwise & (AND) operator
2. Bitwise | (OR) operator
3. Bitwise ^ (XOR) operator
4. Bitwise ~ (NOT) operator"""

"""Bitwise (&) and Operator
This operator is used for applying and gate.
Truth table of (&amp;) operator
Opr1    Opr2    Opr1&amp;Opr2
1       1       1
1       0       0
0       1       0
0       0       0"""

a = 10      #1010
b = 120  #1111000
            #1000
print(bin(a),bin(b))
print("Value after AND (a&b) : ",a&b,bin(a&b))

"""Bitwise (|) or operator
This operator is used to apply or gate
Truth table of bitwise | operator
Opr1    Opr2    Opr1 | Opr2
1       1       1
1       0       1
0       1       1
0       0       0"""


a = 10      #1010
b = 120  #1111000
         #1111010
print(bin(a),bin(b))
print("Value after OR (a|b) : ",a|b,bin(a|b))

"""Bitwise ^ (XOR) operator
This operator is used for applying XOR gate
Truth table of XOR gate
Opr1    Opr2   Opr1^Opr2
1       1       0
1       0       1
0       1       1
0       0       0"""


a = 10      #1010
b = 120  #1111000
         #1110010
print(bin(a),bin(b))
print("Value after XOR (a^b) : ",a^b,bin(a^b))


"""Bitwise not (~) operator
Truth table of bitwise not (~) operator is
Opr1    ~Opr1
0       1
1       0"""

b = 120  #1111000
         #0000111
print(bin(b))
print("Value after NOT (~b) : ",~b,bin(~b))