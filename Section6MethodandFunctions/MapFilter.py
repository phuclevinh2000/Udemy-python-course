def square(num):
    return num**2


my_nums = [1, 2, 3, 4, 5]

for item in map(square, my_nums):
    print(item)

list(map(square, my_nums))

# with lambda keyword instead of def => dung 1 lan roi cut
