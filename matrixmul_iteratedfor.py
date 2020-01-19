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

arr4 = np.array([[0,0],[0,0]])


for i in range(2):
    for j in range(2):
        for k in range(3):
            arr4[i,j] += arr1[i,k] * arr2[k,j]

print('the new matrix using for loop')
print(arr4)




