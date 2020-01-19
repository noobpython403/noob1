x = int(input('user1 '))
y = int(input('user2 '))
z = int(input('user3 '))

if (x > y) and (x > z):
    print('x is largest')

elif (y > x) and (y > z):
    print('y is largest')

elif (z > y) and (z > x):
    print('z is largest')

else:
    if (x == y):
        print('x and y are largest')

    elif (x == z):
        print('x and z are largest')

    else:
        print('y and z are largest')