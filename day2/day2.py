file = open("data.txt")

# init lists
list = []
unsafe_list = []

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
            list_popped = False 
            #if turning point 
            if (int(list[i-1]) >= int(list[i])):
                print("ascending turning point")
                # if(list_popped == False):
                #     thing = list.pop(i-1)
                #     print(thing)
                #     list_popped = True
                #     break
                unsafe += 1
                unsafe_list.append(list)
                break
            #if jump bigger than 4
            if (int(list[i-1]) < (int(list[i]) - 3)):
                print("ascending big jump")
                # if(list_popped == False):
                #     if (list[i-1] == list[0]):
                #         thing = list.pop(i-1)
                #         print(thing)
                #         list_popped = True
                #         break
                #     # if (list[i] == list[len(list)-1]):
                #     else:
                #         thing = list.pop(i)
                #         print(thing)
                #         list_popped = True
                #         break
                unsafe += 1
                unsafe_list.append(list)
                break
            else:
                print("ok")
        total += 1

    # descending
    if (int(list[0]) > int(list[len(list)-1])):
        print("descending")
        for i in range(1, len(list)):
            list_popped = False
            #if turning point 
            if (int(list[i-1]) <= int(list[i])):
                print("descending turning point")
                # if(list_popped == False):
                #     thing = list.pop(i-1)
                #     print(thing)
                #     list_popped = True
                #     break
                unsafe += 1
                unsafe_list.append(list)
                break
            #if jump bigger than 4
            if (int(list[i-1]) > (int(list[i]) + 3)):
                print("descending big jump")
                unsafe += 1
                unsafe_list.append(list)
                break
            else:
                print("ok")
        total += 1

print(total)
print(unsafe)
print("-----")
print(total - unsafe)

print(unsafe_list)
