# string starting from index 0 from start, from -1 from the end
# slicing string: [start:stop:step]

text = 'This is a text'

len(text)  # return the length of the text

text[-2]  # return the letter x

text2 = 'mystring'
text2[:3]  # get back 'mys'
text2[3:6]  # get back 'str'
text2[::]  # take the whole string
text2[::3]  # return back 'mtn'
text2[::-1]  # reverse a string

char = 'a'
char*5  # aaaaa


print('abc{}'.format('dfg'))  # result will be abcdfg
print('The {} {} {}'.format('fox', 'brown', 'quick'))  # The fox brown quick
print('The {0} {0} {0}'.format('fox', 'brown', 'quick'))  # The fox fox fox
# The quick brown fox
print('The {q} {b} {f}'.format(f='fox', b='brown', q='quick'))

result = 100/777
# value:width.precision f, result will be 0.129
print("The reuslt is {r:1.3f}".format(r=result))

name = 'jose'
print(f'The name is {name}')  # will print the name is jose
