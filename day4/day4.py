# file = open("exampledata.txt")
# file = open("exampledata2.txt")
# file = open("exampledata3.txt")
file = open("data.txt")

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

# for line in array2d:
#     print(line)

xmas = 0
for i, line in enumerate(array2d):
    for j, char in enumerate(line):
        if char == 'X':
            try:
                # print(char, i, j)
                # check horizontal forwards
                if array2d[i][j+1] == 'M' and array2d[i][j+2] == 'A' and array2d[i][j+3] == 'S':
                    print("xmas for")
                    xmas += 1
            except IndexError as e:
                print(e, i, j)
                # check diagonal forwards/down 
            try:
                if array2d[i+1][j+1] == 'M' and array2d[i+2][j+2] == 'A' and array2d[i+3][j+3] == 'S':
                    print("xmas for/down")
                    xmas += 1
            except IndexError as e:
                print(e, i, j)
                # check vertical down 
            try:
                if array2d[i+1][j] == 'M' and array2d[i+2][j] == 'A' and array2d[i+3][j] == 'S':
                    print("xmas down")
                    xmas += 1
            except IndexError as e:
                print(e, i, j)
                # check diagonal backwards/down
            try:
                if array2d[i+1][j-1] == 'M' and array2d[i+2][j-2] == 'A' and array2d[i+3][j-3] == 'S' and j-3 >= 0 and j-2 >= 0 and j-1 >= 0:
                    print("xmas back/down")
                    xmas += 1
            except IndexError as e:
                print(e, i, j)

        if char == 'S':
            try:
                # print(char, i, j)
                if array2d[i][j+1] == 'A' and array2d[i][j+2] == 'M' and array2d[i][j+3] == 'X':
                    print("samx for")
                    xmas += 1
            except IndexError as e:
                print(e, i, j)
            try:
                # check diagonal forwards/down 
                if array2d[i+1][j+1] == 'A' and array2d[i+2][j+2] == 'M' and array2d[i+3][j+3] == 'X':
                    print("samx for/down")
                    xmas += 1
            except IndexError as e:
                print(e, i, j)
            try:
                # check vertical down 
                if array2d[i+1][j] == 'A' and array2d[i+2][j] == 'M' and array2d[i+3][j] == 'X':
                    print("samx down")
                    xmas += 1
            except IndexError as e:
                print(e, i, j)
            try:
                # check diagonal backwards/down
                if array2d[i+1][j-1] == 'A' and array2d[i+2][j-2] == 'M' and array2d[i+3][j-3] == 'X' and j-3 >= 0 and j-2 >= 0 and j-1 >= 0:
                    print(i, j)
                    print("samx back/down")
                    xmas += 1
            except IndexError as e:
                print(e, i, j)

print(xmas)

xmas2 = 0
for i, line in enumerate(array2d):
    for j, char in enumerate(line):
        if char == 'A':
            try:
                # both M's on top
                if array2d[i-1][j-1] == 'M' and array2d[i+1][j+1] == 'S' and array2d[i-1][j+1] == 'M' and array2d[i+1][j-1] == 'S' and j-1 >= 0 and i-1 >= 0:
                    print("xmas for")
                    xmas2 += 1
            except IndexError as e:
                print(e, i, j)
            try:
                # both M's on left
                if array2d[i-1][j-1] == 'M' and array2d[i+1][j+1] == 'S' and array2d[i-1][j+1] == 'S' and array2d[i+1][j-1] == 'M' and j-1 >= 0 and i-1 >= 0:
                    print("xmas for")
                    xmas2 += 1
            except IndexError as e:
                print(e, i, j)
            try:
                # both M's on bottom
                if array2d[i-1][j-1] == 'S' and array2d[i+1][j+1] == 'M' and array2d[i-1][j+1] == 'S' and array2d[i+1][j-1] == 'M' and j-1 >= 0 and i-1 >= 0:
                    print("xmas for")
                    xmas2 += 1
            except IndexError as e:
                print(e, i, j)
            try:
                # both M's on right
                if array2d[i-1][j-1] == 'S' and array2d[i+1][j+1] == 'M' and array2d[i-1][j+1] == 'M' and array2d[i+1][j-1] == 'S' and j-1 >= 0 and i-1 >= 0:
                    print("xmas for")
                    xmas2 += 1
            except IndexError as e:
                print(e, i, j)

print(xmas2)
