def open_file(filename):
    rules = []
    updates = []
    file = open(filename)
    for line in file:
        if line.__contains__("|"):
            rules.append(line.strip())
        if line.__contains__(","):
            updates.append(line.strip())
    return rules, updates

def print_contents(list):
    for item in list:
        print(item)

if __name__ == "__main__":
    rules, updates = open_file("exampledata.txt")
    print_contents(rules)
    print_contents(updates)


