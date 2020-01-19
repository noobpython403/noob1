import numpy as np

arr1 = np.array([1, 4, 5, 6, 9, 4])

for i in range(1, len(arr1)):
     if arr1[i-1] >= arr1[i]:
         temp = arr1[i-1]
     else:
         temp = arr1[i]

print(temp)


