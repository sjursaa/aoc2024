file = open("exampledata.txt")

array2d = []

def import_file():
    for line in file:
        list = []
        for char in line.strip():
            list.append(char)
        array2d.append(list)

def print_whole_array():
    for line in array2d:
        print(line)

if __name__ == "__main__":
    import_file()
    print_whole_array()

