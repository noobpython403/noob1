import numpy as np
m = int(input('Enter the rows'))
n = int(input('Enter the columns'))
a = []

for i in range(m):
    b = []
    for j in range(n):
        b.append(int(input()))
    a.append(b)

arr1 = np.array(a)
print(arr1)


