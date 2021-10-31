
from random import randint
from random import shuffle

index_count = 0
for letter in 'abcde':
    print(f'At inded {index_count} the letter is {letter}')
    index_count += 1

# enum
word = 'abcde'
for index, letter in enumerate(word):
    print(letter)
    print(index)

# zip function
mylist1 = [1, 2, 3]
mylist2 = ['a', 'b', 'c']
for item in zip(mylist1, mylist2):
    print(item)

# in, will return true or false
'x' in [1, 2, 3]  # False

# import
#from random import shuffle
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
random_list = shuffle(mylist)
print(mylist)

# random from to
ran = randint(0, 100)  # from 0 to 100
print(ran)

# input
print("Enter your name:")
x = input()
print("Hello, " + x)
