#! Find the Second Largest Number in a List
# Write a Python program to find the second largest number in a list.
#----------- FIRST WAY --------------------#

list1 = [12,56,90,43,90,21]
max = max(list1)
smax = 0

for i in range(len(list1)):
    if max>list1[i]>smax:
        smax = list1[i]

print(f"Second largest in list is {smax}")

#======================================================================
# Write a Python program to find the second largest number in a list.
#----------------- SECOND WAY ---------------#

list1 = [12,56,90,43,90,21]
max = 0
smax = 0

for value in list1:
    if value > max:
        smax = max
        max = value
    elif max>value>smax:
        smax = value

print(f"Second largest value is {smax}")

#======================================================================
# Write a Python program to find the second largest number in a list.
#----------------- THIRD WAY ---------------#

list1 = [12,56,90,43,90,21]
max = 0
smax = 0

for val in list1:
    if val>max:
        max = val
for val in list1:
    if max>val>smax:
        smax = val

print(f"Second largest value is {smax}")

#======================================================#
# Write a Python function to find the common elements between two lists without using set operations.
#---------------- FIRST WAY ----------------#

l1 = [1,2,3,4]
l2 = [5,6,3,4]
l3 = []
for val in l1:
    if val in l2:
        l3.append(val)
print(f"{l1} and {l2}")
print(f"Common elements between them : {l3}")

# Write a Python function to find the common elements between two lists without using set operations.
#---------------- SECOND WAY ----------------#

l1 = [3,5,4]
l2 = [5,6,3,4]
l3 = []
for i in range(len(l1)):
    for j in range(len(l2)):
        if l1[i]==l2[j]:
            l3.append(l1[i])
print(f"{l1} and {l2}")
print(f"Common elements between them : {l3}")


#=====================================================================================
# Write a Python function that checks if a list of integers is sorted in ascending order. Return True if sorted, False otherwise.
#------------ FIRST WAY ----------------#

l1 = [1,2,6,4,3,9]
# l2 = l1
# print(l2)
# for i in range(len(l1)):
#     for j in range(i+1,len(l1)):
#         if l1[i]>l1[j]:
#             l1[i],l1[j] = l1[j],l1[i]
# print(l1)
bool = False
for i in range(len(l1)-1):
    if l1[i]>l1[i+1]:
        bool = False
        break
    else:
        bool = True
    
print(f"{l1} is sorted : {bool}")

#=====================================================================================
# Write a Python function that checks if a list of integers is sorted in ascending order. Return True if sorted, False otherwise.
#------------ SECOND WAY ----------------#

l1 = [1,2,3,4,9,5]
bool = l1 == sorted(l1)
# sorted(nums) returns a new list with the elements sorted in ascending order.
# The comparison nums == sorted(nums) checks if the original list is already sorted. If they are the same, it returns True; otherwise, it returns False.
print(f"{l1} is Sorted : {bool}")


#==============================================================================================
# Write a Python function that takes a list and returns a new list with all duplicate elements removed, keeping only the first occurrence of each element.
#------------------- FIRST WAY --------------#

l1 = [1,2,3,4,5,3,6,7,8,1]
l2 = []

for val in l1:
    if val not in l2:
        l2.append(val)
print(f"After removing duplicates : {l2}")

# Write a Python function that takes a list and returns a new list with all duplicate elements removed, keeping only the first occurrence of each element.
#------------------- SECOND WAY --------------#

l1 = [1,2,3,4,5,5,4,7,8,9]
l2 = set(l1)
print(f"After Removing Duplicates : {l2}")


#---------------------------------------------------------------------
# Write a Python program that takes a sentence as input and prints the words of the sentence in reverse order.

s = "python is owsome language"
print(s)
l1 = s.split(' ')
l2 = []
print(l1)
for i in range(len(l1)-1,-1,-1):
    l2.append(l1[i])
print(l2)
s1 = ' '.join(l2)
print(s1)


#---------------------------------------------------------------------
# Write a Python program that takes a sentence as input and prints the words of the sentence in reverse order.
#----------------- SECOND WAY -----------------------------------

s = "python is owsome language"
print(s)
l1 = s.split(' ')
s1 = l1[::-1]
s1 = ' '.join(s1)
print(f"Reverse string : {s1}")

#=======================================================================
# Write a Python program to find the sum of all even numbers in a given list.

l1 = [10,20,30,25,45]
s = 0
for i in l1:
    if i%2==0:
        s += i
print(f"Sum of even numbers in list is {s}")


#========================================================================
# Write a Python program that prints the first n numbers in the Fibonacci sequence using a for or while loop.
#------------FOR LOOP--------------------------------#
n = 10
n1 = 0
n2 = 1
n3 = 0
print(f"Fibonacci series : {n1} {n2}",end=' ')
for i in range(n):
    n3 = n1 + n2
    print(n3,end=' ')
    n1,n2 = n2,n3
print()

#========================================================================
# Write a Python program that prints the first n numbers in the Fibonacci sequence using a for or while loop.
#------------WHILE LOOP--------------------------------#
n = 10
n1 = 0
n2 = 1
n3 = 0
count = 0
print(f"Fibonacci series : {n1} {n2}",end=' ')
while count<n:
    n3 = n1 + n2
    print(n3,end=' ')
    n1,n2 = n2,n3
    count +=1 
print()

#=====================================================================
# Find the Unique Element Write a Python function that takes a list where every element appears twice except for one element, which appears only once. Return that unique element.

l1 = [1,33,3,2,4,1,4,2]
l2 = []
l = len(l1)-1
for i in range(len(l1)):
    for j in range(i+1,len(l1)):
        if l1[i]==l1[j]:
            l2.append(l1[i])
print(l2)
l3=[]
for i in l1:
    if i not in l2:
        l3.append(i)
print(l3)

#========================================================================
#Write a Python function that takes two sorted lists and merges them into a single sorted list.
l1 = [1,23,3]
l2 = [2,4,6]
l3 = l1 + l2
print(l3)
for i in range(len(l3)):
    for j in range(i+1,len(l3)):
        if l3[i]>l3[j]:
            l3[i],l3[j]=l3[j],l3[i]
print(f'lists after merge and sorted {l3}')
print()

#================================================================================
# Write a Python function that checks if there are any duplicates in a list and returns True if there are, and False otherwise.
l1 = [1,2,3,4,5,11]
bool = False
for i in range(len(l1)):
    for j in range(i+1,len(l1)):
        if l1[i]==l1[j]:
            bool=True
            break
print(f"{l1} contains duplicate elements : {bool}")

#==============================================================================
# Write a Python program that takes a string input and counts the number of vowels and consonants in it (ignore spaces and punctuation).
str1 = "Hello World!"
vcount,ccount=0,0
for i in str1:
    if i in "AEIOUaeiou":
        vcount += 1
    elif (i>='A' and i<='Z') or (i>='a' and i<='z'):
        ccount +=1
print(f"Vowels : {vcount} Consonent : {ccount}")

#===================================================================
# Write a python program to check the string is palandriom or not
s1 = "madam1"
s2 = ""
for i in s1[::-1]:
    s2 = s2+i
print(s2)
if s1==s2:
    print(f"it is a plandrom string {s2}")
else:
    print(f"it is not a plandrom string {s2}")

# Write a python program to check the string is palandriom or not
#-----------------Second Way----------------#

s1 = "madam"
s2 = s1[::-1]
ans = "Palandriom" if s1==s2 else "Not palandriom" 
print(ans)

# Write a python program to check the string is palandriom or not
s1 = ["racecar", "hello", "level", "world"]
s2 =[]
for i in range(len(s1)):
    s3 = ''
    for j in s1[i][::-1]:
        s3 = s3+j
    if s3==s1[i]:
        s2.append(s3)

#======================================================================e 
#Flatten a Nested List Write a Python function that takes a nested list and returns a flat list containing all the elements.

l1 = [[1, 2, [3, 4]], [5, 6], 7]
l2 = []
print(isinstance(l2,float))
for i in l1:
    if isinstance(i,list): # isinstance check karte ki jar i cha type list aasel tr true nhi tr false
        print(i,type(i))
        for j in i:
            print(j)
            if j is isinstance(j,list):
                l2.extend(j)
            else:
                l2.append(j)
    else:
        l2.append(i)
print(l2)

#================= SECOND WAY ============================
def flatten_list(nested_list):
    flat_list = []
    for element in nested_list:
        if isinstance(element, list):
            # Recursively flatten the nested list
            flat_list.extend(flatten_list(element))
        else:
            # Append non-list elements directly
            flat_list.append(element)
    return flat_list

nested_list = [[1, 2, [3, 4]], [5, 6], 7]
result = flatten_list(nested_list)
print("Flattened List:", result)

#=============================================================================
#Convert decimal to binary
val = '0b'
num = 10
while num>0:
    r = num%2
    val = val + str(r)
    num//=2
print(val)
