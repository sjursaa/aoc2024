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
    keepgoing = True
    for i, line in enumerate(map):
        for j, char in enumerate(line):
            try: 
                if char == "^" and map[i-1][j] != "#":
                    print("guard moving up from:", i, j)
                    map[i][j] = "X"
                    map[i-1][j] = "^"
                if char == "^" and map[i-1][j] == "#":
                    print("guard turning right at:", i, j)
                    map[i][j] = ">"
                if char == "v" and map[i+1][j] != "#":
                    print("guard moving down from:", i, j)
                    map[i][j] = "X"
                    map[i+1][j] = "v"
                if char == "v" and map[i+1][j] == "#":
                    print("guard turning left at:", i, j)
                    map[i][j] = "<"
                if char == ">" and map[i][j+1] != "#":
                    print("guard moving right from:", i, j)
                    map[i][j] = "X"
                    map[i][j+1] = ">"
                if char == ">" and map[i][j+1] == "#":
                    print("guard turning down at:", i, j)
                    map[i][j] = "v"
                if char == "<" and map[i][j-1] != "#":
                    print("guard moving left from:", i, j)
                    map[i][j] = "X"
                    map[i][j-1] = "<"
                if char == "<" and map[i][j-1] == "#":
                    print("guard turning up at:", i, j)
                    map[i][j] = "^"
            except Exception as e:
                map[i][j] = "X"
                print(e)
                keepgoing = False
    return map, keepgoing

def count_x(map):
    count = 0
    for line in map:
        for char in line:
            if char == "X":
                count += 1
    return count

if __name__ == "__main__":
    # print("hello world")
    map = open_map("data.txt")
    print_map(map)
    running = True
    while running == True:
        map1, keepgoing = move(map)
        print_map(map1)
        running = keepgoing
        print(count_x(map1))
    
