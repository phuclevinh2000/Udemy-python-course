myfile = open('C:\\Users\\phucl\\Desktop\\Code\\udemy\\python-course\\student\\Section3PythonObjectandDataStructureBasics\\InputOutput\\myfile.txt')

# read
myfile.read()

# set cursor to 0
myfile.seek(0)

# read line
myfile.readline()

# close
myfile.close()

# take data from txt
with open('C:\\Users\\phucl\\Desktop\\Code\\udemy\\python-course\\student\\Section3PythonObjectandDataStructureBasics\\InputOutput\\myfile.txt') as my_new_file:
    contents = my_new_file.read()

# file mode: r = read, w = write , a = append, r+ read and write, w0, writing and reading
with open('C:\\Users\\phucl\\Desktop\\Code\\udemy\\python-course\\student\\Section3PythonObjectandDataStructureBasics\\InputOutput\\myfile.txt', mode='r') as myfile:
    contents = myfile.read()
