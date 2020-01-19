from array import *

arr = array('i',[])
y = int(input('Enter the value\t'))
for i in range(y):
    a = int(input('enter the value\t'))
    arr.append(a)

print(str(arr)[10:-1])

#To sort an array
for i in range(0,y):
    for j in range(i+1,y):
        if arr[i] > arr[j]:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

print(str(arr)[10:-1])

#To reverse an array
arr = arr[::-1]

print(str(arr)[10:-1])