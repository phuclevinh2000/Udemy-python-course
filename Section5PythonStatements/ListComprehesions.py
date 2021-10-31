mystring = 'Hello'

mylist = [letter for letter in mystring]
print(mylist)  # ['h','e','l','l','o']

mylist = [num**2 for num in range(0, 11, 2)]
print(mylist)

mylist = [x for x in range(0, 11) if x % 2 == 0]
print(mylist)

celcius = [0, 10, 20, 34.5]
fah = [((9/5) * temp + 32) for temp in celcius]
print(fah)

mylist = []
for x in [2, 4, 6]:
    for y in [100, 200, 300]:
        mylist.append(x*y)

print(mylist)
