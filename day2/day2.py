file = open("exampledata.txt")

# init lists
list = []

for line in file:
    whole_line = line.strip()
    list = whole_line.split(" ")
    print(list)

for line in list:
    print(line)
