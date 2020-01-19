import array as array

arr1 = array.array('i', [])
x = int(input('Enter the length of array\t'))
for i in range(x):
    x = int(input('Enter the value\t'))
    arr1.append(x)

print('The entered first array is\t', str(arr1)[10:-1])

arr2 = array.array('i', [])
y = int(input('Enter the length of array\t'))
for j in range(y):
    y = int(input('Enter the value\t'))
    arr2.append(y)

print('The entered second array is\t', str(arr2)[10:-1])

#Addition of the array

arr3 = array.array('i', [])
if x == y:
    for i in range(len(arr1)):
        arr3.append(arr1[i] + arr2[i])
    print('The result is\t', str(arr3)[10:-1])

else:
    print('The length should be same')




