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
    non_ok_updates = []
    for rule in rules:
        first = rule.split("|")[0]
        last = rule.split("|")[1]
        # print(first, last)
        for update in updates:
            update_list = update.split(",")
            if first in update_list and last in update_list:
                pos_first = update_list.index(first)
                pos_last = update_list.index(last)
                if pos_first > pos_last:
                    updates.remove(update)
                    non_ok_updates.append(update)
    return updates, non_ok_updates

# TODO: rearrange incorrect updates
def rearrange_updates(rules, updates):
    rearranged_updates = []
    for rule in rules:
        first = rule.split("|")[0]
        last = rule.split("|")[1]
        print(first, last)
        for i, update in enumerate(updates):
            update_list = update.split(",")
            if first in update_list and last in update_list:
                pos_first = update_list.index(first)
                pos_last = update_list.index(last)
                if pos_first > pos_last:
                    print("not ok")
                    print(update_list)
                    update_list[pos_first] = str(last)
                    update_list[pos_last] = str(first)
                    print(i, update_list)
                    string = str(i) + ":" + str(update_list)
                    rearranged_updates.append(string)
                    # print(rearranged_updates)
                    # updates.remove(update)
    # print(rearranged_updates)
    # TODO: remove duplicate entries of the same update (partially sorted/return same number of updates)
    # TODO: ensure full sorting of updates update 1 doesn't sort fully
    return rearranged_updates
                    
def find_middle_value(list):
    sum = 0
    for line in list:
        line_list = line.split(",")
        middle = int(len(line_list) / 2)
        sum += int(line_list[middle])
    return sum

if __name__ == "__main__":
    rules, updates = open_file("exampledata.txt")
    # rules, updates = open_file("data.txt")
    # print_contents(rules)
    # print_contents(updates)
    ok_list, not_ok_list = check_order(rules, updates)
    print_contents(ok_list)
    print_contents(not_ok_list)
    rearranged_list = rearrange_updates(rules, not_ok_list)
    print_contents(rearranged_list)
    sum_ok = find_middle_value(ok_list)
    print("Sum of OK middle values", sum_ok)


