file = open("exampledata.txt")
# file = open("data.txt")

list = []
def open_file():
    for line in file:
        list.append(line.strip())

def print_list():
    for i, item in enumerate(list):
        print(i, item)
    
def assign_towel_patterns():
    patterns = list[0].split(", ")
    sorted_by_length = sorted(patterns, key=len)
    sorted_by_length.reverse()
    return sorted_by_length

def check_if_possible(patterns):
    print(patterns)
    for i, item in enumerate(list):
        if (i >= 2):
            # for char in item:
                # print(char)
            print(i, item)
            # TODO: check longest strings first
            for pattern in patterns:
                if item.startswith(pattern):
                    print(item, pattern)
                # print(pattern)
            

            
        # print(item)

if __name__ == "__main__":
    open_file()
    # print_list()
    patterns = assign_towel_patterns()
    # print(patterns)
    # print_list()
    check_if_possible(patterns)


