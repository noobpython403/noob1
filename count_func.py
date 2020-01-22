names = []

a = int(input('Enter the value'))

for i in range(a):
    b = input('Enter name')
    names.append(b)

print(names)


def count(names):
    count1 = 0
    count2 = 0
    for i in names:
        if len(i) < 5:
            count1 += 1
        else:
            count2 += 1

    return count1, count2


count1, count2 = count(names)
print("Letter less than 5 : {} and Letter more than 5 = {}".format(count1, count2))
