mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
myname = 'Phuc'

for num in mylist:
    print(num)

# from 2 to 30, increase 3
for x in range(2, 30, 3):
    print(x)

# print even number in a mylist
for num in mylist:
    if(num % 2 == 0):
        print(num)
    else:
        print(f'Odd number: {num}')

# example
list_sum = 0
for num in mylist:
    list_sum += num

print(list_sum)

# tuple
mylist = [(1, 2), (3, 4), (5, 6)]
for(a, b) in mylist:
    print(a)
    print(b)

# dictionary
d = {'k1': 1, 'k2': 2, 'k3': 3}

for key, value in d.items():
    print(value)

# continue
x = [1, 2, 3]
for item in x:
    if(item == 2):
        continue
    print(item)
