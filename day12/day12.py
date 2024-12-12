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

above_char = ""
prev_char = ""
list_of_things = []

area = 1
perimeter = 4
for i, line in enumerate(array2d):
    for j, char in enumerate(line):
        if char == prev_char:
            area += 1
            perimeter += 2
            tuple = (char, area, perimeter)
            list_of_things.append(tuple)
            print(tuple)
        if char != prev_char:
            # reinit values
            area = 1
            perimeter = 4
            tuple = (char, area, perimeter)
            list_of_things.append(tuple)

        prev_char = char


for i, line in enumerate(list_of_things):
    print(i, line)
        

'''
area * perimeter

area = number of times character is consecutive

'''
