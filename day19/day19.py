file = open("exampledata.txt")

list = []
def open_file():
    for line in file:
        list.append(line.strip())
        # print(line.strip())

def print_list():
    for i, item in enumerate(list):
        print(i, item)
    
def assign_towel_patterns():
    patterns = list[0].split(",")
    return patterns

if __name__ == "__main__":
    open_file()
    # print_list()
    patterns = assign_towel_patterns()
    print(patterns)
    print_list()

