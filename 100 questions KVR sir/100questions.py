# # 1. Write a Python program to sum all the items in a list.

l1 = [1,3,6,8,3,5,7,99]
print(f"Sum : {sum(l1)}")

# # 2. Write a Python program to multiply all the items in a list. 
l1 = [1,3,6,8,3,5,7,99]
p = 1
for i in l1:
    p *= i
print(f"Multiplication : {p}")

# # 3. Write a Python program to get the largest number from a list. 
l1 = [1,3,6,8,3,5,7,99]
print(f"Maximum : {max(l1)}")

# # 4. Write a Python program to get the smallest number from a list.
l1 = [1,3,6,8,3,5,7,99]
print(f"Minimum : {min(l1)}")

# # 5. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings. 
# # 		Sample List : ['abc', 'xyz', 'aba', '1221']
# # 		Expected Result : 2

l1 = ['abc', 'xyz', 'aba', '1221']
for i in range(len(l1)):
    if l1[i][0]==l1[i][-1]:
        if l1[i].isalpha():
            idx = i

print(f"String : {l1[idx]} Index : {idx}")

# # 6. Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples. 
# # 	Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# # 	Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

l1 = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
for i in range(len(l1)):
    for j in range(i+1,len(l1)):
        if l1[i][-1]>l1[j][-1]:
            l1[i],l1[j]=l1[j],l1[i]
print("Sorted listed : ",l1)

# 7. Write a Python program to remove duplicates from a list.
l1 = [12,45,12,56,78,33]
l2 = []
for i in l1:
    if i not in l2:
        l2.append(i)
print(f"Original list : {l1}")
print(f"After removing duplicates : {l2}")

# # 8. Write a Python program to check a list is empty or not.

l1 = [12]
res = "Non-Empty list" if len(l1)>0 else "Empty"
print(res)

# # 9. Write a Python program to clone or copy a list.

l1 = [12,45,32,21,78,56]
l2 = []
for i in l1:
    l2.append(i)
print(f"After copy list : {l2}")

# # 10. Write a Python program to find the list of words that are longer than n from a given list of words.


# #====================Remove given element from list===============================
list1=[10,20,30,10,10,20,40,50,60,10,10,90,80]
value=10
print(list1)

while True:
    if value in list1:
        list1.remove(10)
    else:
        break
print(list1)

# #========================================================================
# # 11. Write a Python function that takes two lists and returns True if they have at least one common member.
def checkCommonMember(l1,l2):
    for i in l1:
        for j in l2:
            if i==j:
                return True
    else:
        return False

l1 = [12,34,5,678,90]
l2 = [12,31,50,67,9]
print(f"Lists contain common elements : {checkCommonMember(l1,l2)}")


# # 12. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements. 
# # 		Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# # 		Expected Output : ['Green', 'White', 'Black']

l1 = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print(l1)
# value = '_'
# while True:
#     for i in range(len(l1)):
#         if i==0 or i==4 or i==5:
#             l1.remove(l1[i])
#             l1.insert(i,"_")
#             print("hjhjk")
#     else:
#         break
# while True:
#     if value in l1:
#         l1.remove(value)
#     else:
#         break

for i in range(len(l1)-1,-1,-1):
    if i==5 or i==4 or i==0:
        del l1[i]

print(l1)


# # 13. Write a Python program to generate a 3*4*6 3D array whose each element is *. 




# # 14. Write a Python program to print the numbers of a specified list after removing even numbers from it. 

l1 = list(range(1,51))
for i in range(len(l1)-1,-1,-1):
    if l1[i]%2==0:
        del l1[i]
print(l1)

# # 15. Write a Python program to shuffle and print a specified list.
l1 = [12,3,45,66,789,0]
l1.sort()
print(l1)

#========================================================================
# 16. Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30 (both included). 

l1 = list(range(1,31))
for i in l1:
    if i<=5 or i>=25:
        print(f"{i} --> {i*i}")

# 17. Write a Python program to generate and print a list except for the first 5 elements, where the values are square of numbers between 1 and 30 (both included). 

l1 = list(range(1,31))
s1 = list([i*i for i in range(1,31)])
# for i in range(5):
#     val = int(input("Enter value : "))
#     if val in l1 or val in s1:
#         print(f"Present in list")
#     else:
#         print("Not present")

# 18. Write a Python program to generate all permutations of a list in Python.



# 19. Write a Python program to get the difference between the two lists. 

l1 = [1,2,3,4,5,6,7,8,9,]
l2 = [11,12,8,9,10]
l3 =[]
for i in l1:
    if i not in l2:
        l3.append(i)
print(l1,l2,l3,sep='\n')

# 20. Write a Python program access the index of a list.
l1 = list(range(1,11))
for i in range(len(l1)):
    print(i,end=' ')


# 21. Write a Python program to convert a list of characters into a string. 

l1 = ['H','a','r','s','h','a','l']
s = ''
for i in l1:
    s += i
print(f"After Converting list :{l1} into string : {s}")

# 22. Write a Python program to find the index of an item in a specified list. 


# 23. Write a Python program to flatten a shallow list. 

l1 = [[22,33,44],[12,34,56,9],[1,2,3,4,5,6]]
l2 = []

for i in l1:
    for j in i:
        l2.append(j)
l2.sort()
print("Flatten : ",l2)

# 24. Write a Python program to append a list to the second list. 

l1 = [1,2,3,4,5,6,7,8,9,10,]
l2 = []
for i in l1:
    l2 = l2 + [i]
print("After appending 1st list into 2nd : ",l2)

# 25. Write a Python program to select an item randomly from a list. 
import random
list1 = ["Harshal","Sagar","Aniket","Prathamesh","Kunal"]
l1 = random.choice(list1)
print(l1)

# 26. Write a python program to check whether two lists are circularly identical.



# 27. Write a Python program to find the second smallest number in a list. 

l1 = [12,34,56,78,9,2,2,2]
m = min(l1)
c = l1.count(m)
l1.sort()
print(f"Second Smallest : {l1[c]}")

#=================SECOND WAY=========================
l1 = [12,34,56,78,9,2,2,2]
min = l1[0]
smin = l1[0]
for i in l1:
    if i<min:
        smin=min
        min = i
    if i<smin<min:
        smin=i
    
print(f"Min : {min} Second Min : {smin}")
    

# 28. Write a Python program to find the second largest number in a list. 

l1 = [12,34,5,21,45,76,21,76]
m = max(l1)
c = l1.count(m)
l1.sort()
print(f"Second Maximum : {l1[-(c+1)]}")

l2 = [12,34,5,21,45,76,21,76]
m = 0
smax = 0
for i in l2:
    if i>m:
        smax=m
        m = i
    if m>i>smax:
        smax=i
print(f"Max {m} Second Max : {smax}")

# 29. Write a Python program to get unique values from a list. 

l1 = [12,34,4,56,78,56,65,5,4,56,64,67,12,543,4]
print("unique values : ",end=' ')
for i in l1:
    if l1.count(i)==1:
        print(i,end=' ')

# 30. Write a Python program to get the frequency of the elements in a list.
print()
l1 = [12,34,4,56,78,56,65,5,4,56,64,67,12,543,4]
dict1 = {}
for i in l1:
    dict1[i] = l1.count(i)
print("Frequency of the elements : ",dict1)

