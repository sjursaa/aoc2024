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
left_char = ""
list_of_things = []

area = 1
perimeter = 4
k = 0
for i, line in enumerate(array2d):
    for j, char in enumerate(line):
        if i >= 1:
            above_char = array2d[i-1][j]
        if char == left_char:
            area += 1
            perimeter += 2
            tuple = (char, i, j, area, perimeter)
            list_of_things.append(tuple)
            # print(tuple)
        if char == above_char:
            # TODO: get latest area and perimeter values corresponding to above char
            # print(i, j, k)
            print(list_of_things[k-(len(line))])
            
            # list_of_things[][]
            # TODO: implement merging with area and perimeter from above
            print(char, "same char as above")
        # TODO: implement and different from above_char
        if char != left_char: # and char != above_char:
            # reinit values
            area = 1
            perimeter = 4
            tuple = (char, i, j, area, perimeter)
            list_of_things.append(tuple)

        left_char = char
        k += 1 


for i, line in enumerate(list_of_things):
    print(i, line)
        

'''
area * perimeter

area = number of times character is consecutive

'''
