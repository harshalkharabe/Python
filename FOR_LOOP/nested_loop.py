"""Nested Looping Statements
A looping statement within looping statement is called nested looping
statement.
These nested looping statements can be,
1. Nested for loop
2. Nested while loop
Nested for loop
For loop inside for loop is called nested for loop
Syntax:
for variable in iterable: # Outer For loop
    for variable in iterable: # Inner For loop
        statement-1
        statement-2
    statement-3"""

# 1 1 1 1 1 
# 2 2 2 2 2 
# 3 3 3 3 3 
# 4 4 4 4 4 
# 5 5 5 5 5 
for row in range(1,6):
    for col in range(1,6):
        print(row,end=' ')
    print()

print()

# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
for row in range(1,6):
    for col in range(1,6):
        print(col,end=' ')
    print()

print()

# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
for row in range(1,6):
    for col in range(1,6):
        if col<=row:
            print(row,end=' ')
    print()

print()

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
for row in range(1,6):
    for col in range(1,6):
        if col<=row:
            print(col,end=' ')
    print()

print()

# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1
for row in range(5,0,-1):
    for col in range(1,6):
        if col<=row:
            print(col,end=' ')
    print()

print()

#         1
#       2 1
#     3 2 1
#   4 3 2 1
# 5 4 3 2 1
for row in range(1,6):
    for col in range(5,0,-1):
        if col<=row:
            print(col,end=' ')
        else:
            print(" ",end=' ')
    print()

print()

#         1
#       2 2
#     3 3 3
#   4 4 4 4
# 5 5 5 5 5
for row in range(1,6):
    for col in range(5,0,-1):
        if col<=row:
            print(row,end=' ')
        else:
            print(" ",end=' ')
    print()

print()

# 5 5 5 5 5
#   4 4 4 4
#     3 3 3
#       2 2
#         1
for row in range(5,0,-1):
    for col in range(5,0,-1):
        if col<=row:
            print(row,end=' ')
        else:
            print(" ",end=' ')
    print()

print()

# 5 4 3 2 1
#   4 3 2 1
#     3 2 1
#       2 1
#         1
for row in range(5,0,-1):
    for col in range(5,0,-1):
        if col<=row:
            print(col,end=' ')
        else:
            print(" ",end=' ')
    print()

print()

spaces = 0
for row in range(5,0,-1):
    for col1 in range(1,6):
        if col1<=row:
            print("*",end=' ')
    for s in range(spaces):
        print(' ',end=' ')
    for col2 in range(5,0,-1):
        if col2<=row:
            print("*",end=' ')
        else:
            print(' ',end=' ')
    spaces+=1            
    print()

spaces = 4
for row in range(1,6):
    for s in range(spaces):
        print(end=" ")
    for col1 in range(1,6):
        if col1<=row:
            print("*",end=' ')
    spaces-=1
    print()

spaces = 0
num = 6
for row in range(1,6):
    for s in range(spaces):
        print(' ',end=' ')
    for col1 in range(1,num):
        print(col1,end=' ')
    for col2 in range(num-2,0,-1):
        print(col2,end=' ')
    spaces+=1
    num-=1
    print()