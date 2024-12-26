file = open("exampledata.txt")

array2d = []

def import_file():
    start_pos = []
    end_pos = []
    for i, line in enumerate(file):
        list = []
        for j, char in enumerate(line.strip()):
            list.append(char)
            if char == "E":
                end_pos = [i, j]  
            if char == "S":
                start_pos = [i, j]

        array2d.append(list)
    return start_pos, end_pos

def print_whole_array():
    for line in array2d:
        print(line)

if __name__ == "__main__":
    vals = import_file()
    # print(vals)
    print_whole_array()
    print(vals)
    # print(start_pos)
    # print(end_pos)

