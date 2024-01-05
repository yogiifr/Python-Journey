file = open("python_basics/demo.txt", 'w')
file.write("this line is added from python")
file.close()


file = open("python_basics/demo.txt", 'r')
content = file.read()
print(content)
file.close()