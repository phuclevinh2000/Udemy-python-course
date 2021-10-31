def myfunc(a, b, c=0, d=0, e=0):
    # return 5% of the sum of a and b
    return sum((a, b, c, d, e)) * 0.05


print(myfunc(40, 60))


def myfunc(*args):  # to pass as many as use want
    return sum(args)*0.05


print(myfunc(40, 60, 4, 5, 6, 76))


def myfunc(**kwatgs):  # for dictionary
    if 'fruit' in kwatgs:
        print('My fruit of choice is {}'.format(kwatgs['fruit']))
    else:
        print('I did not find anty')


print(myfunc(fruit='apple', veggie='lettuce'))
