file = open("data.txt")

# init lists
left_list = []
right_list = []

for line in file:
    whole_line = line.strip()
    left = whole_line.split("   ")[0]
    right = whole_line.split("   ")[1]
    left_list.append(int(left))
    right_list.append(int(right))

# sort numbers ascending
left_list.sort()
right_list.sort()

# print(left_list)
# print(right_list)

# compute difference
total_difference = 0
i = 0
for item in left_list:
    if left_list[i] > right_list[i]:
        difference = left_list[i] - right_list[i]
    elif left_list[i] < right_list[i]:
        difference = right_list[i] - left_list[i]
    else:
        difference = 0
    total_difference += difference
    i += 1

# compute similarity
total_similarity = 0
similarity = 0
for item in range(len(left_list)):
    for item2 in range(len(right_list)):
        if left_list[item] == right_list[item2]:
            similarity = left_list[item];
            # print(similarity)
            total_similarity += similarity

print(total_difference)
print(total_similarity)
print(total_similarity)
