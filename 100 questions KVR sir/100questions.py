# 1. Write a Python program to sum all the items in a list.

l1 = [1,3,6,8,3,5,7,99]
print(f"Sum : {sum(l1)}")

# 2. Write a Python program to multiply all the items in a list. 
l1 = [1,3,6,8,3,5,7,99]
p = 1
for i in l1:
    p *= i
print(f"Multiplication : {p}")

# 3. Write a Python program to get the largest number from a list. 
l1 = [1,3,6,8,3,5,7,99]
print(f"Maximum : {max(l1)}")

# 4. Write a Python program to get the smallest number from a list.
l1 = [1,3,6,8,3,5,7,99]
print(f"Minimum : {min(l1)}")

# 5. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings. 
# 		Sample List : ['abc', 'xyz', 'aba', '1221']
# 		Expected Result : 2

l1 = ['abc', 'xyz', 'aba', '1221']
for i in range(len(l1)):
    if l1[i][0]==l1[i][-1]:
        if l1[i].isalpha():
            idx = i

print(f"String : {l1[idx]} Index : {idx}")

# 6. Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples. 
# 	Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# 	Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

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

# 8. Write a Python program to check a list is empty or not.

l1 = [12]
res = "Non-Empty list" if len(l1)>0 else "Empty"
print(res)

# 9. Write a Python program to clone or copy a list.

l1 = [12,45,32,21,78,56]
l2 = []
for i in l1:
    l2.append(i)
print(f"After copy list : {l2}")

# 10. Write a Python program to find the list of words that are longer than n from a given list of words.

l1 = [1,2,3,4,5,6]
for i in range(-1,-(len(l1)+1),-1):
    print(l1[i])

l1[0:3]=[12]
print(l1)


list1=[10,20,30,10,10,20,40,50,60,10,10,90,80]
value=10
print(list1)

while True:
    if value in list1:
        list1.remove(10)
    else:
        break
print(list1)

l1 = [10,30,40,20,50]
l1.pop()
print(l1)
l1.pop(0)
print(l1)
l1.pop(1)
print(l1)

