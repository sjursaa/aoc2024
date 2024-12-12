# file = open("data.txt")
# file = open("exampledata.txt")
file = open("exampledata2.txt")

# init lists
array2d = []

# init array
for line in file:
    whole_line = line.strip()
    list = []
    for char in whole_line:
        list.append(char)
    array2d.append(list)

for line in array2d:
    print(line)
