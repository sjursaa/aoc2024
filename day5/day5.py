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
            update_list = update.split(",")
            # print(update_list)
            if first in update_list and last in update_list:
                # print("they both be in here mon", update_list)
                pos_first = update_list.index(first)
                pos_last = update_list.index(last)
                # if pos_first < pos_last:
                #     print("ok")
                    # print("they both be in here mon", update_list)
                if pos_first > pos_last:
                    # print("not ok")
                    # print("not ok", update_list)
                    updates.remove(update)
    # print(updates)
    return updates
                    
def find_middle_value(list):
    sum = 0
    for line in list:
        line_list = line.split(",")
        middle = int(len(line_list) / 2)
        print("middle item in list", line_list[middle])
        sum += int(line_list[middle])
    print(sum)
    return sum

if __name__ == "__main__":
    rules, updates = open_file("exampledata.txt")
    # print_contents(rules)
    # print_contents(updates)
    ok_list = check_order(rules, updates)
    print_contents(ok_list)
    find_middle_value(ok_list)


