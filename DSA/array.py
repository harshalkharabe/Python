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


# Find 2 element in sorted array which sum is equal to target
def find_sum(arr,target):
    if not arr:
        return -1
    arr.sort()
    lb = 0
    ub = len(arr) - 1
    while lb<ub:
        if arr[lb]+arr[ub]==target:
            return (arr[lb], arr[ub])
        elif arr[lb]+arr[ub]<target:
            lb += 1
        else:
            ub -= 1
    return -1,-1

arr = [20,40,60,80,90,120,240]
target = 210
result = find_sum(arr, target)
print(f"Elements that sum to {target} are: {result}")  # Output: Elements that sum to 7 are: (1, 6) or (2, 5) or (3, 4)


# Stock by and sell problem -- Find max profit
def max_profit(prices):
    if not prices:
        return 0
    min_price = float('inf')
    max_profit = 0
    for i in range(len(prices)):
        if prices[i]<min_price:
            min_price = prices[i]
        elif prices[i]-min_price>max_profit:
            max_profit = prices[i] - min_price
    return max_profit

prices = [7, 1, 5, 3, 6, 4]
result = max_profit(prices)
print(f"Maximum profit is: {result}")  # Output: Maximum profit is: 5

# Find element in 2D array
arr = [[1,4,7],[9,12,45],[112,114,213]]

def find_element_2d(arr, target):
    if not arr or not arr[0]:
        return -1, -1
    rows = len(arr)
    cols = len(arr[0])
    right,left = rows*cols-1,0
    while left<right:
        mid = (left + right) // 2
        mid_ele = arr[mid//cols][mid%cols]
        if mid_ele == target:
            return mid // cols, mid % cols
        elif mid_ele < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1, -1

target = 12
result = find_element_2d(arr, target)
print(f"Element {target} found at position: {result}")  # Output: Element 12 found at position: (1, 1)