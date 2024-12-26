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

def check_order(rules, updates):
    for rule in rules:
        first = rule.split("|")[0]
        last = rule.split("|")[1]
        print(first, last)
        for update in updates:
            if first in update and last in update:
                print("they both be in here mon", update)
                # TODO: check if first appears before last in update
                

if __name__ == "__main__":
    rules, updates = open_file("exampledata.txt")
    print_contents(rules)
    print_contents(updates)
    check_order(rules, updates)


