# Day 3 Task - NumPy Basics

import numpy as np

# Create 5x5 random array

arr = np.random.randn(5,5)

print("Original Array:")
print(arr)

#Row-wise mean

row_mean = np.mean(arr, axis=1)

print("Row wise mean:")
print(row_mean)

#Column-wise mean

column_mean = np.mean(arr, axis=0)

print("Column wise mean:")
print(column_mean)

#Normalize array (0 to 1)

normalized = (arr - arr.min())/(arr.max()-arr.min())

print("Normalized Array:")
print(normalized)

#Replace negative values with 0 using np.where()

new_array = np.where(arr < 0, 0, arr)

print("Negative replaced with 0:")
print(new_array)



#1D array 1 to 20 and even index elements
a = np.arange(1,21)

print(a)

print("Even index elements:")
print(a[::2])

#Create 3x3 array sum, mean, std
b = np.array([
[1,2,3],
[4,5,6],
[7,8,9]
])

print("Sum:", np.sum(b))
print("Mean:", np.mean(b))
print("Std:", np.std(b))

#Reshape 12 elements into 3x4
c = np.arange(1,13)

reshape_array = c.reshape(3,4)

print(reshape_array)

#Broadcasting
d = np.array([
[1,2,3],
[4,5,6]
])


print("Add scalar:")
print(d+10)


x = np.array([1,2,3])

print("Add 1D array:")
print(d+x)

#Addition, subtraction, multiplication
a1 = np.array([10,20,30])
a2 = np.array([5,10,15])


print("Addition:")
print(a1+a2)

print("Subtraction:")
print(a1-a2)

print("Multiplication:")
print(a1*a2)

#np.where threshold
values = np.array([10,25,15,40])

result = np.where(values>20,"High","Low")

print(result)


#Find max/min and positions
data = np.array([5,10,2,50,7])

print("Maximum:")
print(data.max())

print("Minimum:")
print(data.min())


print("Max position:")
print(np.argmax(data))

print("Min position:")
print(np.argmin(data))