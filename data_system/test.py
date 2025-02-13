data = []
line = []
for i in range(10):
    data.append(str(10+i))
string = ' '.join(data)
for i in range(10):
    line.append(string+'\n')
file = open("test.txt", "w")
file.writelines(line)
file.close()


data = []
line = []
for i in range(10):
    data.append(str(19-i))
string = ' '.join(data)
for i in range(10):
    line.append(string+'\n')
with open('test.txt', 'a') as file:
    file.writelines(line)

data = []
with open('test.txt', 'r') as file:
    for line in file.readlines():
        s = line.split(' ')
        s = ' '.join(s)
        data.append(s)
for i in range(len(data)):
    print(data[i])

# path = 'test.txt'

# with open(path, 'r') as file:
#     content = file.read()
#     print(content)