import array as array
import numpy as np

arr1 = array.array('i', [])
x = int(input('Enter the length of array\t'))
for i in range(x):
    x = int(input('Enter the value\t'))
    arr1.append(x)

print('The entered array is\t', str(arr1)[10:-1])

y = int(input('Enter the value to be added\t'))

for j in range(x):
    arr1[j] = arr1[j] + y

print('The modified array is\t', str(arr1)[10:-1])
