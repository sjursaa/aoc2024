def open_map(filename):
    map = []
    file = open(filename)
    for line in file:
        # print(line.strip())
        map.append(line.strip())
    return map

def print_map(map):
    for line in map:
        print(line)

if __name__ == "__main__":
    # print("hello world")
    map = open_map("exampledata.txt")
    print_map(map)
    
