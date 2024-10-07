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
