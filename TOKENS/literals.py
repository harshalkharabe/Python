"""Literals
Literals are nothing but values.
Literals are values which never changed.
Python literals are classified into different categories
1. Numeric Literal
2. Non Numeric Literal
Numeric literals are nothing numbers
1. Integer Literal
2. Float literal
3. Complex literal"""

"""Integer literals or values
Integer literal is a numeric value, which does not have fractional part or
decimal part.
Example: whole numbers, even numbers, odd numbers,…"""

"""What is variable?
Variable is an identifier, which is used to identify value.
Variable is a named memory location.
Variable is bind with data type.
type() : returns type of value hold by variable
&gt;&gt;&gt; a=25
&gt;&gt;&gt; type(a)
&lt;class &#39;int&#39;&gt;
&gt;&gt;&gt; a=40
&gt;&gt;&gt; a
40
&gt;&gt;&gt; type(a)
&lt;class &#39;int&#39;&gt;
&gt;&gt;&gt; int a
SyntaxError: invalid syntax

In python integer literals are represented in 4 formats
1. Decimal Integer
2. Octal Integer
3. Hexadecimal Integer
4. Binary Integer"""

"""Decimal Integer
An integer value with base 10 is decimal integer.
This integer is created using digits range from 0-9
This integer is not prefix with 0
This integer is prefix with + or –
Default representation of integer in decimal format."""
a = 10
print("Decimal number",a)
print("Decimal to Octal : ",oct(a))
print("Decimal to Hexadecimal : ",hex(a))
print("Decimal to binary : ",bin(a))

"""Octal Integer
An integer value with base 8 is called octal integer.
This integer is prefix with 0o or 0O
This integer is created using digits range from 0-7"""

b = 0o21
print("Octal number ",b)
print("Octal to Binary ",bin(b))
print("Octal to Hexadecimal ",hex(b))

"""Binary Integer literal
An integer value with base 2 is called binary integer literal/value.
This integer is prefix with 0b or 0B
This integer is created using 0’s and 1’s"""

c = 0b001101
print("Binary number ",c)
print("Binary to octal ",oct(c))
print("Binary to Hexadecimal ",hex(c))

d = 0x1212
print("Hexadecimal number ",d)
print("Hexadecimal to octal ",oct(d))
print("Hexadecimal to binary ",bin(d))

"""String literal
What is string?
String is a non numeric data type.
String is a collection of characters. These characters can be alphabets,
digits or special characters.
The string contains only alphabets is called alphabetic string.
The string contains alphabet, digits is called alphanumeric string.
How to represent string literal or value in python?
In python string value is represented using “str” data type.
“str” is a sequence data type or collection type which represents more than
one character."""

name = 'Harshal Kharabe'
print(name)
snmae = "Gayatri Bhad"
print(snmae)
print("""Triple quots are used for 
      multi line comments""")