import numpy as np

arr = np.array([1,5,4,7,2])
x = np.max(arr)
for i in range(len(arr)):
    if x == arr[i]:
        print('The largest number is at', i+1, 'position.')
        break

else:
        print('Bye')

