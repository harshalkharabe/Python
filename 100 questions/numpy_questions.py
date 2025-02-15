# NumPy: Exercise-100 with Solution
# Exercise 1:
# Create a 1D array with values ranging from 0 to 9.
# import numpy as np
# arr = np.arange(10)
# print(arr)
 
# [0 1 2 3 4 5 6 7 8 9]
# Exercise 2:
# Convert a 1D array to a 2D array with 2 rows.
# import numpy as np
# arr = np.arange(10).reshape(2, -1)
# print(arr)
 
# [[0 1 2 3 4]
#  [5 6 7 8 9]]
# Exercise 3:
# Multiply a 5x3 matrix by a 3x2 matrix.
# import numpy as np
# mat1 = np.random.random((5, 3))
# mat2 = np.random.random((3, 2))
# result = np.dot(mat1, mat2)
# print(result)
 
# [[1.05787846 0.32439392]
#  [2.18241234 0.68182548]
#  [1.23629853 0.39596044]
#  [0.42973189 0.12403945]
#  [1.08039539 0.36356378]]
# Exercise 4:
# Extract all odd numbers from an array of 1-10.
# import numpy as np
# arr = np.arange(1, 11)
# odd_numbers = arr[arr % 2 != 0]
# print(odd_numbers)
 
# [1 3 5 7 9]
# Exercise 5:
# Replace all odd numbers in an array of 1-10 with -1.
# import numpy as np
# arr = np.arange(1, 10)
# arr[arr % 2 != 0] = -1
# print(arr)
 
# [-1  2 -1  4 -1  6 -1  8 -1]
# Exercise 6:
# Convert a 1D array to a boolean array where all positive values become True.
# import numpy as np
# arr = np.array([-1, 2, 0, -4, 5])
# boolean_arr = arr > 0
# print(boolean_arr)
 
# [False  True False False  True]
# Exercise 7:
# Replace all even numbers in a 1D array with their negative.
# import numpy as np
# arr = np.arange(1, 10)
# arr[arr % 2 == 0] *= -1
# print(arr)
 
# [ 1 -2  3 -4  5 -6  7 -8  9]
# Exercise 8:
# Create a random 3x3 matrix and normalize it.
# import numpy as np
# matrix = np.random.random((3,3))
# normalized_matrix = (matrix - np.mean(matrix)) / np.std(matrix)
# print(normalized_matrix)
 
# [[ 1.07755282 -0.27940552 -1.57739216]
#  [ 1.53962723  1.25274094 -0.97454418]
#  [-0.30801978 -0.26192698 -0.46863236]]
# Exercise 9:
# Calculate the sum of the diagonal elements of a 3x3 matrix.
# import numpy as np
# matrix = np.random.random((3, 3))
# diagonal_sum = np.trace(matrix)
# print(diagonal_sum)
 
# 1.0183501284750802
# Exercise 10:
# Find the indices of non-zero elements from [1,2,0,0,4,0].
# import numpy as np
# arr = np.array([1, 2, 0, 0, 4, 0])
# non_zero_indices = np.nonzero(arr)
# print(non_zero_indices)
 
# (array([0, 1, 4], dtype=int64),)
# Exercise 11:
# Reverse a 1D array (first element becomes the last).
# import numpy as np
# arr = np.arange(10)
# reversed_arr = np.flip(arr)
# print(reversed_arr)
 
# [9 8 7 6 5 4 3 2 1 0]
# Exercise 12:
# Create a 3x3 identity matrix.
# import numpy as np
# identity_matrix = np.eye(3)
# print(identity_matrix)
 
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]

# Exercise 13:
# Reshape a 1D array to a 2D array with 5 rows and 2 columns.
# import numpy as np
# arr = np.arange(10)
# reshaped_arr = arr.reshape(5, 2)
# print(reshaped_arr)
 
# [[0 1]
#  [2 3]
#  [4 5]
#  [6 7]
#  [8 9]]
# Exercise 14:
# Stack two arrays vertically.
# import numpy as np
# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])
# stacked_arr = np.vstack((arr1, arr2))
# print(stacked_arr)
 
# [[1 2 3]
#  [4 5 6]]
# Exercise 15:
# Get the common items between two arrays.
# import numpy as np
# arr1 = np.array([1, 2, 3, 4, 5])
# arr2 = np.array([3, 4, 5, 6, 7])
# common_items = np.intersect1d(arr1, arr2)
# print(common_items)
 
# [3 4 5]
# Exercise 16:
# Create a 5x5 matrix with row values ranging from 0 to 4.
# import numpy as np
# matrix = np.zeros((5, 5))
# matrix += np.arange(5)
# print(matrix)
 
# [[0. 1. 2. 3. 4.]
#  [0. 1. 2. 3. 4.]
#  [0. 1. 2. 3. 4.]
#  [0. 1. 2. 3. 4.]
#  [0. 1. 2. 3. 4.]]
# Exercise 17:
# Find the index of the maximum value in a 1D array.
# import numpy as np
# arr = np.array([3, 7, 1, 10, 4])
# max_index = np.argmax(arr)
# print(max_index)
 
# 3
# Exercise 18:
# Normalize the values in a 1D array between 0 and 1.
# import numpy as np
# arr = np.array([2, 5, 10, 3, 8])
# normalized_arr = (arr - np.min(arr)) / (np.max(arr) - np.min(arr))
# print(normalized_arr)
 
# [0.    0.375 1.    0.125 0.75 ]
# Exercise 19:
# Calculate the dot product of two arrays.
# import numpy as np
# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])
# dot_product = np.dot(arr1, arr2)
# print(dot_product)
 
# 32
# Exercise 20:
# Count the number of elements in an array within a specific range.
# import numpy as np
# arr = np.array([2, 5, 8, 10, 12, 15])
# count_within_range = np.sum((arr >= 5) & (arr <= 12))
# print(count_within_range)
 
# 4
# Exercise 21:
# Find the mean of each row in a 2D array.
# import numpy as np
# matrix = np.random.random((3, 4))
# row_means = np.mean(matrix, axis=1)
# print(row_means)
 
# [0.437043   0.73541944 0.45005375]
# Exercise 22:
# Create a random 4x4 matrix and extract the diagonal elements.
# import numpy as np
# matrix = np.random.random((4, 4))
# diagonal_elements = np.diag(matrix)
# print(diagonal_elements)
 
# [0.3968107  0.3355669  0.91924761 0.907174  ]
# Exercise 23:
# Count the number of occurrences of a specific value in an array.
# import numpy as np
# arr = np.array([1, 2, 3, 4, 2, 3, 2, 1])
# count_of_2 = np.count_nonzero(arr == 2)
# print(count_of_2)
 
# 3
# Exercise 24:
# Replace all values in a 1D array with the mean of the array.
# import numpy as np
# arr = np.array([10, 20, 30, 40, 50])
# arr[:] = np.mean(arr)
# print(arr)
 
# [30 30 30 30 30]
# Exercise 25:
# Find the indices of the maximum and minimum values in a 1D array.
# import numpy as np
# arr = np.array([5, 2, 8, 1, 7])
# max_index = np.argmax(arr)
# min_index = np.argmin(arr)
# print("Index of max:", max_index)
# print("Index of min:", min_index)
 
# Index of max: 2
# Index of min: 3
# Exercise 26:
# Create a 2D array with 1 on the border and 0 inside.
# import numpy as np
# arr = np.ones((5, 5))
# arr[1:-1, 1:-1] = 0
# print(arr)
 
# [[1. 1. 1. 1. 1.]
#  [1. 0. 0. 0. 1.]
#  [1. 0. 0. 0. 1.]
#  [1. 0. 0. 0. 1.]
#  [1. 1. 1. 1. 1.]]
# Exercise 27:
# Find the unique values and their counts in a 1D array.
# import numpy as np
# arr = np.array([1, 2, 3, 2, 4, 1, 5, 4, 6])
# unique_values, counts = np.unique(arr, return_counts=True)
# print("Unique values:", unique_values)
# print("Counts:", counts)
 
# Unique values: [1 2 3 4 5 6]
# Counts: [2 2 1 2 1 1]
# Exercise 28:
# Create a 3x3 matrix with values ranging from 0 to 8.
# import numpy as np
# matrix = np.arange(9).reshape(3, 3)
# print(matrix)
 
# [[0 1 2]
#  [3 4 5]
#  [6 7 8]]
# Exercise 29:
# Calculate the exponential of all elements in a 1D array.
# import numpy as np
# arr = np.array([1, 2, 3, 4, 5])
# exponential_arr = np.exp(arr)
# print(exponential_arr)
 
# [  2.71828183   7.3890561   20.08553692  54.59815003 148.4131591 ]
# Exercise 30:
# Swap two rows in a 2D array.
# import numpy as np
# matrix = np.random.random((3, 4))
# matrix[[0, 1]] = matrix[[1, 0]]
# print(matrix)
 
# [[0.64447186 0.98641154 0.7336092  0.79829912]
#  [0.00753743 0.65414365 0.74147161 0.14819561]
#  [0.53158903 0.89859906 0.75709264 0.49165449]]
# Exercise 31:
# Create a random 3x3 matrix and replace all values greater than 0.5 with 1 and all others with 0.
# import numpy as np
# matrix = np.random.random((3, 3))
# matrix[matrix > 0.5] = 1
# matrix[matrix <= 0.5] = 0
# print(matrix)
 
# [[1. 0. 1.]
#  [0. 0. 0.]
#  [0. 0. 0.]]
# Exercise 32:
# Find the indices of the top N maximum values in a 1D array.
# import numpy as np
# arr = np.array([10, 5, 8, 20, 15])
# top_indices = np.argsort(arr)[-2:]  # Replace 2 with desired top N
# print(top_indices)
 
# [4 3]
# Exercise 33:
# Calculate the mean of each column in a 2D array.
# import numpy as np
# matrix = np.random.random((4, 3))
# column_means = np.mean(matrix, axis=0)
# print(column_means)
 
# [0.54904302 0.4902671  0.42925161]
# Exercise 34:
# Normalize the values in each column of a 2D array.
# import numpy as np
# matrix = np.random.random((4, 3))
# normalized_matrix = (matrix - np.mean(matrix, axis=0)) / np.std(matrix, axis=0)
# print(normalized_matrix)
 
# [[-0.46748521 -0.77417852 -0.84330049]
#  [ 1.0967056   1.71309044  0.71160507]
#  [ 0.7764295  -0.58168559  1.24351291]
#  [-1.4056499  -0.35722632 -1.11181749]]
# Exercise 35:
# Concatenate two 1D arrays.
# import numpy as np
# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])
# concatenated_arr = np.concatenate((arr1, arr2))
# print(concatenated_arr)
 
# [1 2 3 4 5 6]
# Exercise 36:
# Create a 2D array with random values and sort each row.
# import numpy as np
# matrix = np.random.random((3, 4))
# sorted_matrix = np.sort(matrix, axis=1)
# print(sorted_matrix)
 
# [[0.10858953 0.71557663 0.7986983  0.90525131]
#  [0.318373   0.50887498 0.51900254 0.7860126 ]
#  [0.06242782 0.12665803 0.12884579 0.1440853 ]]
# Exercise 37:
# Compute the mean squared error between two arrays.
# import numpy as np
# arr1 = np.array([1, 2, 3, 4])
# arr2 = np.array([2, 3, 4, 5])
# mse = np.mean((arr1 - arr2) ** 2)
# print(mse)
 
# # 1.0
# # Exercise 38:
# # Replace all negative values in an array with 0.
# import numpy as np
# arr = np.array([-1, 2, -3, 4, -5])
# arr[arr < 0] = 0
# print(arr)
 
# [0 2 0 4 0]
# Exercise 39:
# Find the 5th and 95th percentiles of an array.
# import numpy as np
# arr = np.random.random(10)
# percentile_5th = np.percentile(arr, 5)
# percentile_95th = np.percentile(arr, 95)
# print("5th Percentile:", percentile_5th)
# print("95th Percentile:", percentile_95th)
 
# 5th Percentile: 0.04785597751800983
# 95th Percentile: 0.8708086577975086
# Exercise 40:
# Create a random 2x2 matrix and compute its determinant.
# import numpy as np
# matrix = np.random.random((2, 2))
# determinant = np.linalg.det(matrix)
# print(determinant)
 
# # 0.0019446951056262907
# # Exercise 41:
# # Count the number of elements in an array that are greater than the mean.
# import numpy as np
# arr = np.array([1, 2, 3, 4, 5])
# count_above_mean = np.sum(arr > np.mean(arr))
# print(count_above_mean)
 
# 2
# # Exercise 42:
# # Calculate the square root of each element in a 1D array.
# import numpy as np
# arr = np.array([4, 9, 16, 25])
# sqrt_arr = np.sqrt(arr)
# print(sqrt_arr)
 
# # [2. 3. 4. 5.]
# # Exercise 43:
# # Create a 3x3 matrix and compute the matrix square root.
# import numpy as np
# matrix = np.random.random((3, 3))
# matrix_sqrt = np.linalg.matrix_power(matrix, 2)
# print(matrix_sqrt)
 
# # [[0.62607741 0.64326801 0.24778017]
# #  [1.35236384 1.43972006 0.56587005]
# #  [0.617024   0.71519995 0.29469311]]

# # Exercise 44:
# # Convert the data type of an array to float.
# import numpy as np
# arr = np.array([1, 2, 3, 4], dtype=int)
# float_arr = arr.astype(float)
# print(float_arr)
 
# [1. 2. 3. 4.]
# # Exercise 45:
# # Calculate the element-wise absolute values of an array.
# import numpy as np
# arr = np.array([-1, -2, 3, -4])
# abs_values = np.abs(arr)
# print(abs_values)
 
# [1 2 3 4]
# # Exercise 46:
# # Find the indices where elements of two arrays match.
# import numpy as np
# arr1 = np.array([1, 2, 3, 4, 5])
# arr2 = np.array([3, 2, 8, 4, 5])
# matching_indices = np.where(arr1 == arr2)
# print(matching_indices)
 
# (array([1, 3, 4], dtype=int64),)
# Exercise 47:
# Calculate the cumulative sum of elements in a 1D array.
# import numpy as np
# arr = np.array([1, 2, 3, 4, 5])
# cumulative_sum = np.cumsum(arr)
# print(cumulative_sum)
 
# [ 1  3  6 10 15]
# Exercise 48:
# Compute the inverse of a 2x2 matrix.
# import numpy as np
# matrix = np.random.random((2, 2))
# inverse_matrix = np.linalg.inv(matrix)
# print(inverse_matrix)
 
# [[ 1.22685384 -4.14864181]
#  [-0.2704788   6.62123806]]
# Exercise 49:
# Count the number of non-zero elements in a 2D array.
# import numpy as np
# matrix = np.array([[0, 1, 0], [2, 0, 3], [0, 4, 0]])
# non_zero_count = np.count_nonzero(matrix)
# print(non_zero_count)
 
# 4
# Exercise 50:
# Create a 2D array and replace all nan values with 0.
# import numpy as np
# matrix = np.array([[1, np.nan, 3], [4, 5, np.nan], [7, 8, 9]])
# matrix[np.isnan(matrix)] = 0
# print(matrix)
 
# [[1. 0. 3.]
#  [4. 5. 0.]
#  [7. 8. 9.]]
# Exercise 51:
# Find the correlation coefficient between two arrays.
# import numpy as np
# arr1 = np.array([1, 2, 3, 4, 5])
# arr2 = np.array([3, 4, 5, 6, 7])
# correlation_coefficient = np.corrcoef(arr1, arr2)[0, 1]
# print(correlation_coefficient)
 
# 0.9999999999999999
# Exercise 52:
# Create a 1D array and remove all duplicate values.
# import numpy as np
# arr = np.array([1, 2, 3, 2, 4, 5, 1])
# unique_arr = np.unique(arr)
# print(unique_arr)
 
# [1 2 3 4 5]
# Exercise 53:
# Compute the element-wise product of two arrays.
# import numpy as np
# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])
# elementwise_product = np.multiply(arr1, arr2)
# print(elementwise_product)
 
# [ 4 10 18]
# Exercise 54:
# Calculate the standard deviation of each column in a 2D array.
# import numpy as np
# matrix = np.random.random((4, 3))
# column_stddev = np.std(matrix, axis=0)
# print(column_stddev)
 
# [0.22702366 0.27411548 0.25568707]
# Exercise 55:
# Create a 2D array and set all values above a certain threshold to that threshold.
# import numpy as np
# matrix = np.random.random((3, 4))
# threshold = 0.7
# matrix[matrix > threshold] = threshold
# print(matrix)
 
# [[0.7        0.54918234 0.7        0.01893358]
#  [0.09114833 0.00268936 0.13766009 0.28160436]
#  [0.40448374 0.7        0.7        0.30830747]]
# Exercise 56:
# Create a random 5x5 matrix and replace the maximum value by -1.
# import numpy as np
# matrix = np.random.random((5, 5))
# max_value_index = np.unravel_index(np.argmax(matrix), matrix.shape)
# matrix[max_value_index] = -1
# print(matrix)
 
# [[ 0.45916565  0.79856137  0.68998918  0.04439129  0.84814684]
#  [ 0.4442666   0.2661443   0.83980951  0.71727557  0.30334519]
#  [ 0.47332068  0.50437988  0.51222628  0.65334221  0.21664521]
#  [ 0.7511065   0.77837283  0.29019334  0.82695944  0.41608473]
#  [ 0.23775068  0.07539172 -1.          0.14166163  0.56071446]]
# Exercise 57:
# Convert a 1D array of Fahrenheit temperatures to Celsius.
# import numpy as np
# fahrenheit_temps = np.array([32, 68, 100, 212])
# celsius_temps = (fahrenheit_temps - 32) * 5/9
# print(celsius_temps)
 
# [  0.          20.          37.77777778 100.        ]
# Exercise 58:
# Compute the outer product of two arrays.
# import numpy as np
# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])
# outer_product = np.outer(arr1, arr2)
# print(outer_product)
 
# [[ 4  5  6]
#  [ 8 10 12]
#  [12 15 18]]
# Exercise 59:
# Create a 1D array with 10 equidistant values between 0 and 1.
# import numpy as np
# equidistant_arr = np.linspace(0, 1, 10)
# print(equidistant_arr)
 
# [0.         0.11111111 0.22222222 0.33333333 0.44444444 0.55555556
#  0.66666667 0.77777778 0.88888889 1.        ]
# Exercise 60:
# Compute the cross product of two 3D arrays.
# import numpy as np
# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])
# cross_product = np.cross(arr1, arr2)
# print(cross_product)
 
# [-3 6 -3]
# Exercise 61:
# Calculate the percentile along a specific axis of a 2D array.
# import numpy as np
# matrix = np.random.random((3, 4))
# percentiles_axis1 = np.percentile(matrix, 75, axis=1)
# print(percentiles_axis1)
 
# [0.73954718 0.63159296 0.49097014]
# Exercise 62:
# Create a 1D array and add a border of 0s around it.
# import numpy as np
# arr = np.array([1, 2, 3, 4])
# arr_with_border = np.pad(arr, (1, 1), mode='constant', constant_values=0)
# print(arr_with_border)
 
# [0 1 2 3 4 0]
# Exercise 63:
# Compute the histogram of a 1D array.
# import numpy as np
# arr = np.array([1, 1, 2, 2, 2, 3, 3, 3, 3])
# hist, bins = np.histogram(arr, bins=[1, 2, 3, 4])
# print("Histogram:", hist)
# print("Bin edges:", bins)
 
# Histogram: [2 3 4]
# Bin edges: [1 2 3 4]
# Exercise 64:
# Create a 2D array with random values and normalize each row.
# import numpy as np
# matrix = np.random.random((4, 3))
# normalized_rows = matrix / np.linalg.norm(matrix, axis=1, keepdims=True)
# print(normalized_rows)
 
# [[0.61881278 0.58433001 0.52500398]
#  [0.50152886 0.39533452 0.76953195]
#  [0.18399814 0.89840062 0.39877439]
#  [0.76636647 0.25223155 0.59081442]]
# Exercise 65:
# Create a random 2D array and sort it by the second column.
# import numpy as np
# matrix = np.random.random((3, 4))
# sorted_matrix_by_column2 = matrix[matrix[:, 1].argsort()]
# print(sorted_matrix_by_column2)
 
# [[0.28214407 0.30234856 0.56159219 0.34651641]
#  [0.72579465 0.64605243 0.14824549 0.6364958 ]
#  [0.4852539  0.96161675 0.41756529 0.7079494 ]]
# Exercise 66:
# Calculate the determinant of a 3x3 matrix.
# import numpy as np
# matrix = np.random.random((3, 3))
# determinant = np.linalg.det(matrix)
# print(determinant)
 
# 0.09550080558000806
# Exercise 67:
# Calculate the element-wise exponentiation of a 1D array.
# import numpy as np
# arr = np.array([2, 3, 4])
# exponentiated_arr = np.exp(arr)
# print(exponentiated_arr)
 
# [ 7.3890561  20.08553692 54.59815003]
# Exercise 68:
# Calculate the Frobenius norm of a 2D array.
# import numpy as np
# matrix = np.random.random((3, 4))
# frobenius_norm = np.linalg.norm(matrix)
# print(frobenius_norm)
 
# 1.8692600488600242
# Exercise 69:
# Create a 2D array with random values and replace the maximum value with the minimum.
# import numpy as np
# matrix = np.random.random((3, 4))
# max_value_index = np.unravel_index(np.argmax(matrix), matrix.shape)
# min_value = np.min(matrix)
# matrix[max_value_index] = min_value
# print(matrix)
 
# [[0.29383093 0.01637657 0.7794734  0.01637657]
#  [0.76911564 0.22745882 0.32986131 0.84500937]
#  [0.94922056 0.54607467 0.80921816 0.28474546]]
# Exercise 70:
# Compute the matrix multiplication of two 2D arrays.
# import numpy as np
# matrix1 = np.random.random((3, 4))
# matrix2 = np.random.random((4, 5))
# matrix_multiplication = np.dot(matrix1, matrix2)
# print(matrix_multiplication)
 
# [[0.99119942 0.85513185 0.57664501 0.31851386 0.84601174]
#  [1.38306551 1.16773145 0.83001893 0.68922723 1.12666608]
#  [1.72827308 1.44430652 1.03782659 1.28492828 1.24906297]]
# Exercise 71:
# Create a 1D array and set the values between 10 and 20 to 0.
# import numpy as np
# arr = np.array([5, 15, 12, 18, 25])
# arr[(arr >= 10) & (arr <= 20)] = 0
# print(arr)
 
# [ 5  0  0  0 25]
# Exercise 72:
# Compute the inverse hyperbolic sine of each element in a 1D array.
# import numpy as np
# arr = np.array([1, 2, 3, 4])
# inverse_sineh_arr = np.arcsinh(arr)
# print(inverse_sineh_arr)
 
# [0.88137359 1.44363548 1.81844646 2.09471255]
# Exercise 73:
# Compute the Kronecker product of two arrays.
# import numpy as np
# arr1 = np.array([1, 2])
# arr2 = np.array([3, 4])
# kronecker_product = np.kron(arr1, arr2)
# print(kronecker_product)
 
# [3 4 6 8]
# Exercise 74:
# Calculate the mean absolute deviation of a 1D array.
# import numpy as np
# arr = np.array([1, 2, 3, 4, 5])
# mean_absolute_deviation = np.mean(np.abs(arr - np.mean(arr)))
# print(mean_absolute_deviation)
 
# 1.2
# Exercise 75:
# Create a 3x3 matrix and set all values above the main diagonal to zero.
# import numpy as np
# matrix = np.random.random((3, 3))
# matrix[np.triu_indices(3, 1)] = 0
# print(matrix)
 
# [[0.7344708  0.         0.        ]
#  [0.91154103 0.58004909 0.        ]
#  [0.53953411 0.73231191 0.8315308 ]]
# Exercise 76:
# Count the number of occurrences of each unique value in a 1D array.
# import numpy as np
# arr = np.array([2, 2, 1, 3, 3, 3, 4])
# unique_values, counts = np.unique(arr, return_counts=True)
# print("Unique values:", unique_values)
# print("Counts:", counts)
 
# Unique values: [1 2 3 4]
# Counts: [1 2 3 1]
# Exercise 77:
# Compute the cumulative product of elements along a given axis in a 2D array.
# import numpy as np
# matrix = np.random.random((3, 4))
# cumulative_product_axis0 = np.cumprod(matrix, axis=0)
# print(cumulative_product_axis0)
 
# [[0.65005294 0.01951926 0.25636043 0.30961964]
#  [0.28738887 0.00883133 0.24993819 0.06504888]
#  [0.21895124 0.00590692 0.0116853  0.03512077]]
# Exercise 78:
# Round elements of a 1D array to the nearest integer.
# import numpy as np
# arr = np.array([1.2, 2.7, 3.5, 4.9])
# rounded_arr = np.round(arr)
# print(rounded_arr)
 
# [1. 3. 4. 5.]
# Exercise 79:
# Create a 1D array and append a new element to the end.
# import numpy as np
# arr = np.array([1, 2, 3])
# new_element = 4
# arr = np.append(arr, new_element)
# print(arr)
 
# [1 2 3 4]
# Exercise 80:
# Calculate the element-wise absolute difference between two arrays.
# import numpy as np
# arr1 = np.array([3, 7, 1, 10, 4])
# arr2 = np.array([2, 5, 8, 1, 7])
# absolute_difference = np.abs(arr1 - arr2)
# print(absolute_difference)
 
# [1 2 7 9 3]
# Exercise 81:
# Create a 2D array with random values and replace the maximum value in each row with -1.
# import numpy as np
# matrix = np.random.random((3, 4))
# max_values_indices = np.argmax(matrix, axis=1)
# matrix[np.arange(matrix.shape[0]), max_values_indices] = -1
# print(matrix)
 
# [[ 0.14015869  0.13279371 -1.          0.4665563 ]
#  [ 0.73795369  0.311774   -1.          0.05087541]
#  [ 0.6516183  -1.          0.30233177  0.48674956]]
# Exercise 82:
# Normalize the columns of a 2D array to have a sum of 1.
# import numpy as np
# matrix = np.random.random((3, 4))
# normalized_columns = matrix / np.sum(matrix, axis=0, keepdims=True)
# print(normalized_columns)
 
# [[0.00548299 0.49881449 0.16102029 0.23643045]
#  [0.58935257 0.27548946 0.54365728 0.57390056]
#  [0.40516443 0.22569604 0.29532244 0.18966899]]
# Exercise 83:
# Find the indices of the top N minimum values in a 1D array.
# import numpy as np
# arr = np.array([10, 5, 8, 1, 7])
# top_indices = np.argsort(arr)[:2]  # Replace 2 with desired top N
# print(top_indices)
 
# [3 1]
# Exercise 84:
# Convert the elements of a 1D array to strings.
# import numpy as np
# arr = np.array([1, 2, 3, 4])
# string_arr = arr.astype(str)
# print(string_arr)
 
# ['1' '2' '3' '4']
# Exercise 85:
# Compute the percentile rank of each element in a 1D array.
# import numpy as np
# from scipy.stats import percentileofscore
# arr = np.array([1, 2, 3, 4, 5])
# # Calculate percentile rank for each element in arr
# percentile_rank = np.array([percentileofscore(arr, value) for value in arr])
# print(percentile_rank)
 
# [ 20.  40.  60.  80. 100.]
# Exercise 86:
# Create a 1D array and shuffle its elements randomly.
# import numpy as np
# arr = np.array([1, 2, 3, 4, 5])
# np.random.shuffle(arr)
# print(arr)
 
# [4 2 5 1 3]
# Exercise 87:
# Check if all elements in a 1D array are non-zero.
# import numpy as np
# arr = np.array([1, 2, 3, 4, 5])
# all_nonzero = np.all(arr != 0)
# print(all_nonzero)
 
# True
# Exercise 88:
# Find the indices of the maximum value in each row of a 2D array.
# import numpy as np
# matrix = np.random.random((3, 4))
# max_indices_per_row = np.argmax(matrix, axis=1)
# print(max_indices_per_row)
 
# [1 3 2]
# Exercise 89:
# Create a 2D array and replace all nan values with the mean of the array.
# import numpy as np
# matrix = np.array([[1, np.nan, 3], [4, 5, np.nan], [7, 8, 9]])
# nan_mean = np.nanmean(matrix)
# matrix[np.isnan(matrix)] = nan_mean
# print(matrix)
 
# [[1.         5.28571429 3.        ]
#  [4.         5.         5.28571429]
#  [7.         8.         9.        ]]
# Exercise 90:
# Calculate the mean of each row in a 2D array ignoring nan values.
# import numpy as np
# matrix = np.array([[1, 2, np.nan], [4, np.nan, 6], [7, 8, 9]])
# row_means_ignore_nan = np.nanmean(matrix, axis=1)
# print(row_means_ignore_nan)
 
# [1.5 5.  8. ]
# Exercise 91:
# Compute the sum of diagonal elements in a 2D array.
# import numpy as np
# matrix = np.random.random((3, 3))
# diagonal_sum = np.trace(matrix)
# print(diagonal_sum)
 
# 1.375162416021255
# Exercise 92:
# Convert radians to degrees for each element in a 1D array.
# import numpy as np
# arr_in_radians = np.array([np.pi/2, np.pi, 3*np.pi/2])
# arr_in_degrees = np.degrees(arr_in_radians)
# print(arr_in_degrees)
 
# [ 90. 180. 270.]
# Exercise 93:
# Calculate the pairwise Euclidean distance between two arrays.
# import numpy as np
# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])
# euclidean_distance = np.linalg.norm(arr1 - arr2)
# print(euclidean_distance)
 
# 5.196152422706632
# Exercise 94:
# Create a 1D array and set the values between the 25th and 75th percentile to 0.
# import numpy as np
# arr = np.array([10, 20, 30, 40, 50])
# percentile_25th = np.percentile(arr, 25)
# percentile_75th = np.percentile(arr, 75)
# arr[(arr >= percentile_25th) & (arr <= percentile_75th)] = 0
# print(arr)
 
# [10  0  0  0 50]
# Exercise 95:
# Calculate the element-wise square of the difference between two arrays.
# import numpy as np
# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])
# squared_difference = (arr1 - arr2)**2
# print(squared_difference)
 
# [9 9 9]
# Exercise 96:
# Replace all even numbers in a 1D array with the next odd number.
# import numpy as np
# arr = np.array([2, 5, 8, 12, 15])
# arr[arr % 2 == 0] += 1
# print(arr)
 
# [ 3  5  9 13 15]
# Exercise 97:
# Create a 2D array and normalize each column by its range..
# import numpy as np
# matrix = np.random.random((3, 4))
# normalized_columns_range = (matrix - np.min(matrix, axis=0)) / (np.max(matrix, axis=0) - np.min(matrix, axis=0))
# print(normalized_columns_range)
 
# [[0.         1.         0.         1.        ]
#  [0.38748809 0.         1.         0.        ]
#  [1.         0.39378719 0.83348354 0.78448847]]

# Exercise 98:
# Compute the cumulative sum of elements along a given axis in a 2D array.
# import numpy as np
# matrix = np.random.random((3, 4))
# cumulative_sum_axis1 = np.cumsum(matrix, axis=1)
# print(cumulative_sum_axis1)
 
# [[0.23623571 0.76181793 1.40183102 2.02358543]
#  [0.89415619 1.38540147 1.46977913 1.99923603]
#  [0.3626984  0.94484957 1.24671758 2.19056585]]
# Exercise 99:
# Check if any element in a 1D array is non-zero.
# import numpy as np
# arr = np.array([0, 0, 0, 1, 0])
# any_nonzero = np.any(arr != 0)
# print(any_nonzero)
 
# True
# Exercise 100:
# Create a 2D array with random integers and replace all values greater than a certain threshold with that threshold.
# import numpy as np
# matrix = np.random.randint(0, 100, size=(3, 4))
# threshold = 75
# matrix[matrix > threshold] = threshold
# print(matrix)
 
# [[72 55 56 26]
#  [ 8 16 54 75]
#  [13 74 36 75]]

