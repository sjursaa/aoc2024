from re import findall


file = open("data.txt")

# init lists
# list = []

total = 0
for line in file:
    whole_line = line.strip()
    print(whole_line)

    
    # print((findall(".mul\([0-9],[0-9]\)", whole_line)))
    
    # list.append(findall("mul\([0-9]\d*,[0-9]\d*\)", whole_line))
    list = findall("mul\([0-9]\d*,[0-9]\d*\)", whole_line)
    # print(string)
    for string in list:
        # print(type(i))
        # print(string)
        number1 = string.split(",")[0]
        number2 = string.split(",")[1]

        remove_chars1 = ''.join((ch if ch in '0123456789.-e' else ' ') for ch in number1)
        return_number1 = [int(i) for i in remove_chars1.split()]
        remove_chars2 = ''.join((ch if ch in '0123456789.-e' else ' ') for ch in number2)
        return_number2 = [int(i) for i in remove_chars2.split()]

        # print(remove_chars1)
        # print(return_number1)
        # print(remove_chars2)
        # print(return_number2)

        sum = return_number1[0] * return_number2[0]
        total += sum
        
        print(sum)
        # print(number1)
        # print(number2)

print(total)
# proper_list = []
# for string in list:
#     # proper_list.append(string.split(","))
#     print(string)

# multiply function(string) {
#
#     hello
# }
    # left = whole_line.split("   ")[0]
    # list.append((line))

