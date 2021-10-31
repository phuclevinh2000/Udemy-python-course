# if somecondition:
#   execute some code
# elif:
#   do something else
# else:
#   do something else

# short form
a, b = 5, 7
x = a > b if 10 else 11
print(x)

# normal form
hungry = True
if hungry:
    print('Feed me')
else:
    print("Im full")

# more
loc = 'bank'
if loc == 'auto shop':
    print('Car are cool')
elif loc == 'bank':
    print('I do not know much')
else:
    print('Hi')
