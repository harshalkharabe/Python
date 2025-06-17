# Linear Search

def linear_search(arr, target):
    if not arr:
        return -1
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr = [1, 2, 3, 4, 5]
target = 3
result = linear_search(arr, target)
print(f"Element {target} found at index: {result}")  # Output: Element 3 found at index: 2    


# Binary Search
def binary_search(arr,target):
    if not arr:
        return -1
    arr.sort()
    ub = len(arr)-1
    lb = 0
    mid = len(arr)//2
    while lb<ub:
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            lb = mid + 1
        else:
            ub = mid - 1
        mid = (lb + ub) // 2
    return mid

arr = [1, 2, 3, 4, 5, 6]
target = 3
result = binary_search(arr, target)
print(f"Element {target} found at index: {result}")  # Output: Element 3 found at index: 2