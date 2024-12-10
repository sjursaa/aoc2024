# file = open("exampledatahash.txt")
file = open("exampledata.txt")
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
        list.append(int(char))
    array2d.append(list)
    # print(list)

# print array to console
for line in array2d:
    print(line)

# find and list number of trailheads and positions of those
trailhead = 0
for i, line in enumerate(array2d):
    for j, char in enumerate(line):
        if char == 0:
            print(i,j)
            trailhead += 1
print(trailhead)

# find and list number of endpoints & positions (max score)
endpoint = 0
for i, line in enumerate(array2d):
    for j, char in enumerate(line):
        if char == 9:
            print(i,j)
            endpoint += 1
print(endpoint)

# # print array to console
# for line in array2d:
#     print(line)
