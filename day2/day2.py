file = open("data.txt")

# init lists
list = []
unsafe = 0
total = 0

for line in file:
    whole_line = line.strip()
    list = whole_line.split(" ")
    print("new list")
    print(list)
    print(list[0]) 
    print(list[len(list)-1])
    # ascending
    if (int(list[0]) < int(list[len(list)-1])):
        print("ascending")
        for i in range(1, len(list)):
            #if turning point 
            if (int(list[i-1]) >= int(list[i])):
                print("ascending turning point")
                unsafe += 1
                break
            #if jump bigger than 4
            if (int(list[i-1]) < (int(list[i]) - 3)):
                print("ascending big jump")
                unsafe += 1
                break
            else:
                print("ok")
        total += 1

    # descending
    if (int(list[0]) > int(list[len(list)-1])):
        print("descending")
        for i in range(1, len(list)):
            #if turning point 
            if (int(list[i-1]) <= int(list[i])):
                print("descending turning point")
                unsafe += 1
                break
            #if jump bigger than 4
            if (int(list[i-1]) > (int(list[i]) + 3)):
                print("descending big jump")
                unsafe += 1
                break
            else:
                print("ok")
        total += 1

print(total)
print(unsafe)
print("-----")
print(total - unsafe)
