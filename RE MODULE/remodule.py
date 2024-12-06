#Regular expression

#2 ways to define regular expression
# 1. using r'string' (row string)
# 2. using compile method of re 

import re
s1 = r'Harshal kharabe'
print(type(s1)) # --> <class 'str'>
s2 = re.compile("Harshal Kharabe")
print(type(s2)) # --> <class 're.Pattern'>

# searching methods of re module

# 1.re.search()

s1 = "Python java Python python"
data = re.search("Python",s1)
print(data) # Python is 2 times in s1 but it returns only 1 

data = re.search("java",s1)
print(data)

data = re.search("python",s1)
print(data)

data = re.search("ythonjj",s1)
print(data)

# 2. re.match()

s1 = "Python java Python python"
data = re.match(s1,"java")
print(data) # it checks only at staring of string

data = re.match("python",s1)
print(data)

data = re.match("Python",s1)
print(data)

# 3. re.findall()

s1 = "Python java Python python"
data = re.findall("python",s1)
print(data) # it returns in list and all occurens of 

s1 = "Python java Python python"
data = re.findall("Python",s1)
print(data) # it returns in list

data = re.findall('java',s1)
print(data)


s1 = "Python"
is_equal = re.fullmatch("python",s1)
print(is_equal) # it is similar to == operator

s1 = "Python"
is_equal = re.fullmatch("Python",s1)
print(is_equal)


# special characters 

# . (Dot)
print("-------------------------------------------------------------------------")
s1 = "naresh suresh harshal kunal kishore rajesh ramesh"
data = re.findall(r"k.",s1)
print(data)

data = re.findall(r".a",s1)
print(data)

data = re.findall(r".r.",s1)
print(data)

data = re.findall(r"...",s1)
print(data)

#  ^ (cap)
print("-------------------------------------------------------------------------")
list1 = ["harshal","narsah","kunal","suresh","rakesh","rajesh","kishor"]
for i in list1:
    data = re.search(r"^r",i)
    if data != None:
        print(i)

list1 = ["harshal","narsah","kunal","suresh","rakesh","rajesh","kishor"]
for i in list1:
    data = re.search(r"^n",i)
    if data != None:
        print(i)

list1 = ["harshal","narsah","kunal","suresh","rakesh","rajesh","kishor"]
for i in list1:
    data = re.search(r"^",i)
    if data != None:
        print(i)

# $ (dollar)
print("-------------------------------------------------------------------------")
list1 = ["harshal","narsah","kunal","suresh","rakesh","rajesh","kishor"]
for name in list1:
    data = re.search(r'l$',name)
    if data!=None:
        print(name)

list1 = ["harshal.in","narsah.tech","kunal.com","suresh.in","rakesh.in","rajesh.tech","kishor.com"]
for i in list1:
    data = re.search(r".com$",i)
    if data!=None:
        print(i)


print("-------------------------------------------------------------------------")
# * (star)

s1 = "abb a abbb a abb ab bb"
data = re.findall(r'ab*',s1)
print(data) # 'ch*' means need 0 or more (ch)characters


print("-------------------------------------------------------------------------")
# + (plus)

s1 = "abb a abbb a abb ab bb"
data = re.findall(r'ab+',s1)
print(data) # 'ch+' means need 1 or more characters(ch)


print("-------------------------------------------------------------------------")
# ? (question)
s1 = "abb a abbb a abb ab bb"
data = re.findall(r'ab?',s1)
print(data) # ['ab', 'a', 'ab', 'a', 'ab', 'ab'] it need 0 or 1 character


print("-------------------------------------------------------------------------")
# {m} (curly braces)

s1 = ["naresh","suresh","rajesh","kishore","ramesh"]
for name in s1:
    data = re.fullmatch(r'.{6}',name)
    if data!=None:
        print(name)
print()
s1 = ["naresh","suresh","rajesh","kishore","ramesh"]
for name in s1:
    data = re.fullmatch(r'r.{5}',name)
    if data!=None:
        print(name)
print()
s1 = ["naresh","suresh","rajesh","kishore","ramesh"]
for name in s1:
    data = re.fullmatch(r'r.{4}h$',name)
    if data!=None:
        print("name :",name)


print("-----------------------------------------------------------")
# {m,n}
# m = minimum characters
# n = mximum characters

s1 = "ab abbb a abb abbbbbb ab"
list1 = re.findall(r"ab{2,4}",s1)
print("Between minimum and maximum :",list1)

s1 = "ab abbb a abb abbbbbb ab"
list1 = re.findall(r"ab{,4}",s1)
print("Minnimun is 0 : ",list1)

s1 = "ab abbb a abb abbbbbb ab"
list1 = re.findall(r"ab{2,}",s1)
print("Maximum is any : ",list1)


print("-----------------------------------------------------------")

# [] (Square brackets)

s1 = "python 3.13 Python 3.14"
data = re.findall(r'[a-zA-Z]',s1)
print(data)

s1 = "python 3.13 Python 3.14"
data = re.findall(r'[a-zA-Z]',s1)
print(data)

s1 = "python 3.13 Python 3.14"
data = re.findall(r'[0-9]',s1)
print(data)

str1 = "date of joining 20-08-2024"
date = re.search(r'[0-9]{2}-[0-9]{2}-[0-9]{4}',str1)
print("Date validation : ",date.group(0))

str1 = "date of joining 20-08-2024 12:34:2024"
date = re.search(r'[0-9]{2}:[0-9]{2}:[0-9]{2}',str1)
print("Time validation : ",date.group(0))

str1 = "my email-id is naresh123@nareshit.com"
data = re.search(r"[a-z0-9]+@[a-z]+\.[a-z]{2,3}",str1)
print("Email validation :",data.group(0))

# or operator (|) used to check two or more pattern

str1 = "date of joining 20-08-2024 12:34:24"
data = re.findall(r"[0-9]{2}-[0-9]{2}-[0-9]{4}|[0-9]{2}:[0-9]{2}:[0-9]{2}",str1)
print(data)

print("----------------------------------------------------------------")
# (?P='name'...)

str1 = "date of joining 20-08-2024 12:34:24"
data = re.search(r"(?P<hh>[0-9]{2}):(?P<mm>[0-9]{2}):(?P<ss>[0-9]{2})",str1)
print(data.group(0))
print(data.group(1))
print(data.group(2))
print(data.group(3))
print(data.group('hh'),":",data.group('mm'),":",data.group('ss'),sep='')
