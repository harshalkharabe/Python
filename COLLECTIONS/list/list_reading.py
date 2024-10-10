#SLICING OF LIST

list1 = list(range(10,101,10))
print(list1[::])
print(list1[:])

print(list1[::-1])
print(list1[::1])
print(list1[::-2])
print(list1[::2])

print(list1[2:])
print(list1[-3::])
print(list1[8::])

print(list1[:5:])
print(list1[:-2:])
print(list1[-1:-3:-1])

s1 = slice(5)
s2 = slice(-1,-12,-4)
list1 = list(range(12,34,2))

print(list1[s2])

list1 = list(range(21,211,21))
print(list1)

list2 = list1[::-1]
print(list2)

list3 = list1[-8:5:]
print(list3)

list1 = [1,23,3]
list1[len(list1):len(list1)]=[2]
print(list1) 

l1 = iter(list1)
# print(next(l1))
print(next(l1))
print(next(l1))
print(next(l1))
print(next(l1))

l1 = [1,2,3,4,5]
b = iter(l1)
for i in b:
    print(i)

list1 = [12,45,23,89,32]
a = enumerate(list1)

val = next(a)
print(val,type(val))

# list1 = list([int(input("Enter a number : ")) for i in range(1,6)])
# print(list1)
# list1.append(12)
# print(list1)
# list2 = [12,54,6,734,23,221]
# list2.append([23,1])
# print(list2)

#append without using append function
list3 = [1,2]
list3.append(list([int(input("Enter number : ")) for i in range(1,6)]))
print(list3)

list3[len(list3):len(list3)]=[2]
print(list3)

# n = int(input("How many numbers you want to enter : "))
# list4 = []
# oc,ec=0,0
# for i in range(n):
#     num = int(input("Enter a number : "))
#     list4.append(num)
#     if num % 2 == 0:
#         ec+=1
#     else:
#         oc+=1
# print(f"Even count : {ec} and Odd count : {oc}")
# print(f"List : {list4}")

# list5 = [1,2,4]
# list5.extend((1,2,8))
# print(list5)

x = "Harshal"
l1 = []
l1.extend(x)
print(l1)

