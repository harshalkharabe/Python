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