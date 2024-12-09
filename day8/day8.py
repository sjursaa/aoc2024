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
print("\niterating across list of chars: computing distance")
for i, line in enumerate(list_of_pos):
    new_char = False
    if (list_of_pos[i-1][0] != list_of_pos[i][0]):
        print("new char")
        new_char = True
        # print(list_of_pos[i][0])
    # print(i ,line)
    # print(i, line[0], line[1], line[2])
    if (new_char == False):
        print(list_of_pos[i-1])
        print(list_of_pos[i])
        print(list_of_pos[i][1] - list_of_pos[i-1][1])
        print(list_of_pos[i][2] - list_of_pos[i-1][2])
        distance1 = list_of_pos[i][1] - list_of_pos[i-1][1]
        distance2 = list_of_pos[i][2] - list_of_pos[i-1][2]

        # TODO: assign # to following positions
        print(array2d[list_of_pos[i-1][1]-distance1][list_of_pos[i-1][2]-distance2])
        print(array2d[list_of_pos[i][1]+distance1][list_of_pos[i][2]+distance2])
        new_char = False
        # print(list_of_pos[i-1][2])




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


