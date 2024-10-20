#FIND Nth MAXIMUM AND MINIMUM ELEMENT IN TUPLE

t1 = (3,7,1)
k=1
l1 = sorted(t1)
mi = l1[:k]
mx = l1[-k:]
t2 = tuple(mi+mx)
print(t2)