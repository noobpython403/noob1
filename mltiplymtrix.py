import numpy as np

arr1 = np.matrix('1,2,3 ; 4,5,6')
arr2 = np.matrix('1,2 ; 3,4 ; 5,6')

print('The first matrix is')
print(arr1)
print('The seconde matrix is')
print(arr2)

print('Multiplication matrix using in built function')
arr3 = arr1 * arr2
print(arr3)


a = 0                                       #for first term
for i in range(3):
    temp1 = arr1[0,i] * arr2[i,0]
    a = a + temp1

b = 0                                       #for seconde term
for i in range(3):
    temp2 = arr1[0,i] * arr2[i,1]
    b = b + temp2

c = 0                                       #for third term
for i in range(3):
    temp3 = arr1[1,i] * arr2[i,0]
    c = c + temp3

d = 0                                       #for fourth term
for i in range(3):
    temp4 = arr1[1,i] * arr2[i,1]
    d = d + temp4

print('the new matrix using for loop')

arr4 = np.array([[a,b],[c,d]])
print(arr4)




