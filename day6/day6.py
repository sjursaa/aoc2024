def open_map(filename):
    map = []
    file = open(filename)
    for line in file:
        line_list = []
        for char in line.strip():
            line_list.append(char)
        # print(line.strip())
        map.append(line_list)
    return map

def print_map(map):
    for line in map:
        print(line)

def move(map):
    # print("Moving")
    for i, line in enumerate(map):
        for j, char in enumerate(line):
            if char == "^" and map[i-1][j] == ".":
                print("guard moving up from:", i, j)
                map[i][j] = "."
                map[i-1][j] = "."
            if char == "v":
                print("guard moving down from:", i, j)
            if char == ">":
                print("guard moving right from:", i, j)
            if char == "<":
                print("guard moving right from:", i, j)

if __name__ == "__main__":
    # print("hello world")
    map = open_map("exampledata.txt")
    print_map(map)
    move(map)
    
