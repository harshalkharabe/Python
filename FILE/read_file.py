# Reading data from text file
# Reading data from text file is done using methods of file object
# 1. read()
# 2. readline()

# Reading text from file1.txt
fileobject = open('text.txt','r')
data = fileobject.read()
print(data)
fileobject.close()


fileobject=open('text.txt','r')
data = fileobject.read(6) # it gives particular number of characters
print(data)
fileobject.close()


fileobject = open('text2.txt','r')
while True:
    data = fileobject.readline()
    if data=='':
        break
    print(data.split())

fileobject.close()


fileobject = open('text.txt','r')
alphacount,digitcount,specialcount = 0,0,0
while True:
    ch = fileobject.read(1)
    if ch=='':
        break
    if ch.isalpha():
        alphacount+=1
    elif ch.isdigit():
        digitcount+=1
    else:
        specialcount+=1
print("Total alphabates in file :",alphacount)
print("Total digits in file :",digitcount)
print("Total special characters in file :",specialcount)
fileobject.close()


#Program for Demonstrating How to Open the File

try:
    with open('text.txt','r') as fobj:
        print("Inside File.")
        print("File opening mode :",fobj.name)
        print("File opening mode :",fobj.mode)
        print("Can we read data from File :",fobj.readable())
        print("Can we write data from File :",fobj.writable())
        print("Is file closed :",fobj.closed)
        fobj.close()
    print("file closed after opened :",fobj.closed)
except FileNotFoundError:
    print("File not found")