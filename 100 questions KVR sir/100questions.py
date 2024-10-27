# # # 1. Write a Python program to sum all the items in a list.

# l1 = [1,3,6,8,3,5,7,99]
# print(f"Sum : {sum(l1)}")

# # # 2. Write a Python program to multiply all the items in a list. 
# l1 = [1,3,6,8,3,5,7,99]
# p = 1
# for i in l1:
#     p *= i
# print(f"Multiplication : {p}")

# # # 3. Write a Python program to get the largest number from a list. 
# l1 = [1,3,6,8,3,5,7,99]
# print(f"Maximum : {max(l1)}")

# # # 4. Write a Python program to get the smallest number from a list.
# l1 = [1,3,6,8,3,5,7,99]
# print(f"Minimum : {min(l1)}")

# # # 5. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings. 
# # # 		Sample List : ['abc', 'xyz', 'aba', '1221']
# # # 		Expected Result : 2

# l1 = ['abc', 'xyz', 'aba', '1221']
# for i in range(len(l1)):
#     if l1[i][0]==l1[i][-1]:
#         if l1[i].isalpha():
#             idx = i

# print(f"String : {l1[idx]} Index : {idx}")

# # # 6. Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples. 
# # # 	Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# # # 	Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

# l1 = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# for i in range(len(l1)):
#     for j in range(i+1,len(l1)):
#         if l1[i][-1]>l1[j][-1]:
#             l1[i],l1[j]=l1[j],l1[i]
# print("Sorted listed : ",l1)

# # 7. Write a Python program to remove duplicates from a list.
# l1 = [12,45,12,56,78,33]
# l2 = []
# for i in l1:
#     if i not in l2:
#         l2.append(i)
# print(f"Original list : {l1}")
# print(f"After removing duplicates : {l2}")

# # # 8. Write a Python program to check a list is empty or not.

# l1 = [12]
# res = "Non-Empty list" if len(l1)>0 else "Empty"
# print(res)

# # # 9. Write a Python program to clone or copy a list.

# l1 = [12,45,32,21,78,56]
# l2 = []
# for i in l1:
#     l2.append(i)
# print(f"After copy list : {l2}")

# # # 10. Write a Python program to find the list of words that are longer than n from a given list of words.
l1 = ['Harshal','Sagar','Kunal',"Ram",'Ankush','paa','pukii']
l = int(input("Enter lenght : "))
for i in l1:
    if len(i)>=l:
        print(i)

# # #====================Remove given element from list===============================
# list1=[10,20,30,10,10,20,40,50,60,10,10,90,80]
# value=10
# print(list1)

# while True:
#     if value in list1:
#         list1.remove(10)
#     else:
#         break
# print(list1)

# # #========================================================================
# # # 11. Write a Python function that takes two lists and returns True if they have at least one common member.
# def checkCommonMember(l1,l2):
#     for i in l1:
#         for j in l2:
#             if i==j:
#                 return True
#     else:
#         return False

# l1 = [12,34,5,678,90]
# l2 = [12,31,50,67,9]
# print(f"Lists contain common elements : {checkCommonMember(l1,l2)}")


# # # 12. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements. 
# # # 		Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# # # 		Expected Output : ['Green', 'White', 'Black']

# l1 = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# print(l1)
# # value = '_'
# # while True:
# #     for i in range(len(l1)):
# #         if i==0 or i==4 or i==5:
# #             l1.remove(l1[i])
# #             l1.insert(i,"_")
# #             print("hjhjk")
# #     else:
# #         break
# # while True:
# #     if value in l1:
# #         l1.remove(value)
# #     else:
# #         break

# for i in range(len(l1)-1,-1,-1):
#     if i==5 or i==4 or i==0:
#         del l1[i]

# print(l1)


# # # 13. Write a Python program to generate a 3*4*6 3D array whose each element is *. 




# # # 14. Write a Python program to print the numbers of a specified list after removing even numbers from it. 

# l1 = list(range(1,51))
# for i in range(len(l1)-1,-1,-1):
#     if l1[i]%2==0:
#         del l1[i]
# print(l1)

# # # 15. Write a Python program to shuffle and print a specified list.
# l1 = [12,3,45,66,789,0]
# l1.sort()
# print(l1)

# #========================================================================
# # 16. Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30 (both included). 

# l1 = list(range(1,31))
# for i in l1:
#     if i<=5 or i>=25:
#         print(f"{i} --> {i*i}")

# # 17. Write a Python program to generate and print a list except for the first 5 elements, where the values are square of numbers between 1 and 30 (both included). 

# l1 = list(range(1,31))
# s1 = list([i*i for i in range(1,31)])
# # for i in range(5):
# #     val = int(input("Enter value : "))
# #     if val in l1 or val in s1:
# #         print(f"Present in list")
# #     else:
# #         print("Not present")

# # 18. Write a Python program to generate all permutations of a list in Python.



# # 19. Write a Python program to get the difference between the two lists. 

# l1 = [1,2,3,4,5,6,7,8,9,]
# l2 = [11,12,8,9,10]
# l3 =[]
# for i in l1:
#     if i not in l2:
#         l3.append(i)
# print(l1,l2,l3,sep='\n')

# # 20. Write a Python program access the index of a list.
# l1 = list(range(1,11))
# for i in range(len(l1)):
#     print(i,end=' ')


# # 21. Write a Python program to convert a list of characters into a string. 

# l1 = ['H','a','r','s','h','a','l']
# s = ''
# for i in l1:
#     s += i
# print(f"After Converting list :{l1} into string : {s}")

# # 22. Write a Python program to find the index of an item in a specified list. 
l1 = [12,34,56,78,34,34,89]
n = int(input("Enter number : "))
idx=-1
for i in range(len(l1)):
    if l1[i]==n:
        idx=i
print(f"Index of given value in list is {idx}")



# # 23. Write a Python program to flatten a shallow list. 

# l1 = [[22,33,44],[12,34,56,9],[1,2,3,4,5,6]]
# l2 = []

# for i in l1:
#     for j in i:
#         l2.append(j)
# l2.sort()
# print("Flatten : ",l2)

# # 24. Write a Python program to append a list to the second list. 

# l1 = [1,2,3,4,5,6,7,8,9,10,]
# l2 = []
# for i in l1:
#     l2 = l2 + [i]
# print("After appending 1st list into 2nd : ",l2)

# # 25. Write a Python program to select an item randomly from a list. 
# import random
# list1 = ["Harshal","Sagar","Aniket","Prathamesh","Kunal"]
# l1 = random.choice(list1)
# print(l1)

# # 26. Write a python program to check whether two lists are circularly identical.



# # 27. Write a Python program to find the second smallest number in a list. 

# l1 = [12,34,56,78,9,2,2,2]
# m = min(l1)
# c = l1.count(m)
# l1.sort()
# print(f"Second Smallest : {l1[c]}")

# #=================SECOND WAY=========================
# l1 = [12,34,56,78,9,2,2,2]
# min = l1[0]
# smin = l1[0]
# for i in l1:
#     if i<min:
#         smin=min
#         min = i
#     if i<smin<min:
#         smin=i
    
# print(f"Min : {min} Second Min : {smin}")
    

# # 28. Write a Python program to find the second largest number in a list. 

# l1 = [12,34,5,21,45,76,21,76]
# m = max(l1)
# c = l1.count(m)
# l1.sort()
# print(f"Second Maximum : {l1[-(c+1)]}")

# l2 = [12,34,5,21,45,76,21,76]
# m = 0
# smax = 0
# for i in l2:
#     if i>m:
#         smax=m
#         m = i
#     if m>i>smax:
#         smax=i
# print(f"Max {m} Second Max : {smax}")

# # 29. Write a Python program to get unique values from a list. 

# l1 = [12,34,4,56,78,56,65,5,4,56,64,67,12,543,4]
# print("unique values : ",end=' ')
# for i in l1:
#     if l1.count(i)==1:
#         print(i,end=' ')

# # 30. Write a Python program to get the frequency of the elements in a list.
# print()
# l1 = [12,34,4,56,78,56,65,5,4,56,64,67,12,543,4]
# dict1 = {}
# for i in l1:
#     dict1[i] = l1.count(i)
# print("Frequency of the elements : ",dict1)

# #==============================================================================
# # 31. Write a Python program to count the number of elements in a list within a specified range.
# l1 = [12,3,54,22,17,20,14,4,6,7,9,8]
# for i in range(3,21):
#     if i in l1:
#         print(i,end=' ')

# #=================================================================================
# # 32. Write a Python program to check whether a list contains a sublist.
# print()
# l1 = [1,2,3,4,5,6,7]
# l2 = [4,5,6,7]
# l=len(l2)
# for i in range(len(l1)-len(l2)+1):
#     if l1[i:i+l]==l2:
#         print(f"{l2} is sublist of {l1}")
#         break
# else:
#     print(f"{l2} is not sublist of {l1}")


# #=================================================================================
# # 33. Write a Python program to generate all sublists of a list. 


# #=================================================================================
# # 35. Write a Python program to create a list by concatenating a given list which range goes from 1 to n. 
# # 	Sample list : ['p', 'q']
# # 	n =5
# # 	Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']

# # s1 = ['p','q']
# # n=5
# # s2 = []
# # for i in range(n):
# #     s2.append(s1[0]+str(i+1))
# #     s2.append(s1[1]+str(i+1))
# # print(s2)

# #=================================================================================
# # 36. Write a Python program to get variable unique identification number or string. 

# #=================================================================================
# # 37. Write a Python program to find common items from two lists.
# # l1 = [3,4,5,6,7,8]
# # l2 = [1,2,3,4,5,8]
# # l3 = []
# # for i in l1:
# #     if i in l2:
# #         l3.append(i)
# # print(l3)

# #=================================================================================
# # 38. Write a Python program to change the position of every n-th value with the (n+1)th in a list. 
# # 	Sample list: [0,1,2,3,4,5]
# # 	Expected Output: [1, 0, 3, 2, 5, 4]

# # l1 = [0,1,2,3,4,5]
# # i=0
# # while i<len(l1)-1:
# #     l1[i],l1[i+1]=l1[i+1],l1[i]
# #     i+=2
# # print(l1)
# #=================================================================================
# # 39. Write a Python program to convert a list of multiple integers into a single integer. 
# # 		Sample list: [11, 33, 50]
# # 		Expected Output: 113350

# # l1 = [11,32,50]
# # digit = 0
# # for num in l1:
# #     num1=num
# #     c = 0
# #     while num>0:
# #         c+=1
# #         num//=10
# #     print(c)
# #     digit = (digit*(10**c))+num1
# #     print(digit)
# # print(digit)
    
# #=================================================================================
# # 40. Write a Python program to split a list based on first character of word.      
# # words = ["apple", "banana", "apricot", "berry", "cherry", "carrot","pappya"]
# # dict1 = {}
# # i=0
# # while i<len(words):
# #     ch = words[i][0]
# #     dict1[ch]=list()
# #     for word in words:
# #         if ch == word[0]:
# #             dict1[ch].append(word)
# #     i+=1
# # print(dict1)

# # 41. Write a Python program to create multiple lists.      
# l1 = list()
# print(f"Empty list : {l1}")
# l2 = [12,34,56,9]
# print(f"List : {l2}")
# l3 = [i for i in range(1,11)]
# print(f"List : {l3}")

# # 42. Write a Python program to find missing and additional values in two lists.      
# # 	Sample data : Missing values in second list: b,a,c
# # 	Additional values in second list: g,h

l1 = [12,34,56,78,54,3]
l2 = [34,56,7,12]
missing_values = []
additional_values = []
for i in l1:
    if i not in l2:
        missing_values.append(i)
for i in l2:
    if i not in l1:
        additional_values.append(i)
    
print("Missing values in second list : ",missing_values)
print("Additional values in l2 : ",additional_values)

# # 43. Write a Python program to split a list into different variables. 
a,b,c=[12,34,56]
print("After spliting list intop three variables : ",a,b,c)
a,b,*c=[12,34,56,43,21,23]
print("After spliting list intop three variables : ",a,b,c)

# # 44. Write a Python program to generate groups of five consecutive numbers in a list. 
# l1 = [[int(input("Values : ")) for i in range(3)] for val in range(2)]
# print(l1)

# # 45. Write a Python program to convert a pair of values into a sorted unique array.
a=int(input("Enter number : "))
b=int(input("Enter number : "))
if a==b:
    l1 = [a]
else :
    l1 = [a]+[b]
print(l1)

# 46. Write a Python program to select the odd items of a list. 
l1 = list(range(5,51,5))
l2 = [num for num in l1 if num%2!=0]
print(l1,l2,sep='\n')

# 47. Write a Python program to insert an element before each element of a list.
# l1 = [12,34,56,78,89]
# l2 = []
# for i in range(len(l1)):
#     l2.append(l1[i])
#     item = int(input(f"Enter number to insert at place :"))
#     l2.append(item)

# print(l2)

# 48. Write a Python program to print a nested lists (each list on a new line) using the print() function. 
l1 = [[1,2],[3,4],[5,6],[7,8]]
print(l1)
for i in l1:
    print(i)

# 49. Write a Python program to convert list to list of dictionaries.
# Sample lists: ["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]
# Expected Output: [{'color_name': 'Black', 'color_code': '#000000'}, {'color_name': 'Red', 'color_code': '#FF0000'}, {'color_name': 'Maroon', 'color_code': '#800000'}, {'color_name': 'Yellow', 'color_code': '#FFFF00'}]

l1 = ["Black", "Red", "Maroon", "Yellow"]
l2 = ["#000000", "#FF0000", "#800000", "#FFFF00"]
color = []
for i in range(len(l1)):
    dic = {}
    dic['color_name'] = l1[i]
    dic['color_code'] = l2[i]
    color.append(dic)
print(color)

# 50. Write a Python program to sort a list of nested dictionaries. 
data = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'Charlie', 'age': 35},
    {'name': 'David', 'age': 20}
]
print(f"Before sorting : {data}")
for i in range(len(data)):
    for j in range(i+1,len(data)):
        if data[i]['age']>data[j]['age']:
            data[i],data[j]=data[j],data[i]
print("After Sorting : ",data)



# 51. Write a Python program to split a list every Nth element. 
# 	Sample list: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
# 	Expected Output: [['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]



# 52. Write a Python program to compute the difference between two lists.      
# Sample data: ["red", "orange", "green", "blue", "white"], ["black", "yellow", "green", "blue"]
# Expected Output:
# 	Color1-Color2: ['white', 'orange', 'red']
# 	Color2-Color1: ['black', 'yellow']
l1 = ["red", "orange", "green", "blue", "white"]
l2 = ["black", "yellow", "green", "blue"]

print("Color1-Color2")
for i in l2:
    if i not in l1:
        print(i)

print("Color2-Color1")
for i in l1:
    if i not in l2:
        print(i)

# 53. Write a Python program to create a list with infinite elements.
# n=0
# i=0
# l1=[]
# while True:
#     n+=1
#     l1.append(n)
#     print(l1)

# 54. Write a Python program to concatenate elements of a list.

l1 = ["My","Name","is","Harshal","Kharabe"]
s1 = ''
for i in l1:
    s1 = s1+i+" "
print(s1)

# 55. Write a Python program to remove key values pairs from a list of dictionaries.

# 56. Write a Python program to convert a string to a list. 
s = "Harshal"
l1 = [ch for ch in s]
print("String to List :",l1)

# 57. Write a Python program to check if all items of a given list of strings is equal to a given string.
def check(l1,s) :
    for i in l1:
        if i != s:
            return False
    return True
l1 = ["Harshal","Kharabe"]
s = "Harshal"
print(f"Check {s} is equal to all words in list or not : ",check(l1,s))

# 58. Write a Python program to replace the last element in a list with another list. 
# 	Sample data : [1, 3, 5, 7, 9, 10], [2, 4, 6, 8]
# 	Expected Output: [1, 3, 5, 7, 9, 2, 4, 6, 8]

l1 = [1, 3, 5, 7, 9, 10]
l2 = [2, 4, 6, 8]
l3 = []
for i in range(len(l1)-1):
    l3.append(l1[i])
for i in range(len(l2)):
    l3.append(l2[i])
print(l3)
# 59. Write a Python program to check whether the n-th element exists in a given list. 
l1 = [12,34,32,56,54,78,9,10]
nth_ele = int(input("Enter nth element position : "))
if nth_ele<len(l1):
    print("Exist")
else:
    print("Not Exist")

# 60. Write a Python program to find a tuple, the smallest second index value from a list of tuples.
l1 = [(2,4),(2,3),(5,1),(4,3),(2,4)]
stup = l1[0][-1]
print(stup)
smallest=None
for i in range(len(l1)):
        if stup>l1[i][-1]:
            stup = l1[i][-1]
            smallest=l1[i]
print("Smallest second tuple value : ",smallest)
