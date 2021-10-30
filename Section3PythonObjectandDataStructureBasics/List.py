my_list = [1, 2, 3]

print(my_list[1:])  # output: 2, 3

# add element into a list: .append
# example
my_list.append(4)  # add 4 into the list¨at the end of the list
print(my_list)  # will show 1,2,3,4

# pop off the last element of the list
my_list.pop()  # pop off 4 and remove that from the list, in the () is the index of the array
my_list.pop(0)  # pop off the first element of the list

new_list = ['a', 'e', 'x', 'b', 'c']
num_list = [4, 1, 3, 5]

new_list.sort()  # does not return anything
print(new_list)

# .reverse to reverse the array
newArraY = [1, 2, 3, 4]
newArraY.reverse()
print(newArraY)
