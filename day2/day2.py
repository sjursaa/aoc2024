file = open("exampledata.txt")

# init lists
list = []

for line in file:
    whole_line = line.strip()
    list = whole_line.split(" ")
    print("new list")
    print(list)
    print(list[0]) 
    print(list[len(list)-1])
    # ascending
    if list[0] < list[len(list)-1]:
        print("ascending")

    # descending
    if list[0] > list[len(list)-1]:
        print("descending")


