# open files 
# file = open("exampledata.txt")
file = open("exampledatahash.txt")
# file = open("data.txt")
rows = 0
cols = 0

# init lists
array2d = []

# init array
for line in file:
    whole_line = line.strip()
    list = []
    for char in whole_line:
        list.append(char)
    array2d.append(list)
    # print(list)

# print array to console
print("print input array to console")
for line in array2d:
    print(line)

# get value and position of characters
print("\nlisting positions of chars != . and #")
list_of_pos = []
for i, line in enumerate(array2d):
    for j, char in enumerate(line):
        if (char != "." and char != "#"):
            print(char, i, j)
            list = [char, i, j]
            list_of_pos.append(list)

print("\nlist of pos")
print(list_of_pos)

# TODO: compute distance between elements
# TODO: place # in position with same distance before first element (within bounds)
# TODO: place # in position with same distance after second element (within bounds)
for i, line in enumerate(list_of_pos):
    print(i ,line)




# testing updating
print("\ntesting updating")
print(array2d[7][7]) # one side
print(array2d[10][10]) # other side
array2d[7][7] = "#"
array2d[10][10] = "#"
print(array2d[7][7])
print(array2d[10][10])

# print array to console
print("\nprint array to console")
for line in array2d:
    print(line)


