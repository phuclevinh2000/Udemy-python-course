# set are unordered collection of unique element in py
# ex
myset = set()
myset.add(1)
print(myset)  # print {1}
myset.add(1)
print(myset)  # print {1}

list = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
set(list)  # {1,2,3,4,5}

test = set([1, 1, 2, 3])
print(test)
