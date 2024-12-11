init_arrangement = [0, 125, 1172]

init_arrangement_prop = [3, 386358, 86195, 85, 1267, 3752457, 0, 741]
# file = open("data.txt")

# One blink
print(init_arrangement)
# TODO: wrap code into function blink(list)
justinserted = False
for i, stone in enumerate(init_arrangement):
    if stone != 0 and len(str(stone)) % 2 != 0: 
        init_arrangement[i] *= 2024
    elif stone == 0:
        init_arrangement[i] = 1
    elif len(str(stone)) % 2 == 0 and justinserted == False: # not optimized at all
        halfway = int(len(str(stone)) / 2 )
        end = int(len(str(stone)))
        first_half = str(stone)[0:halfway]
        second_half = str(stone)[halfway:end]
        init_arrangement[i] = int(first_half)
        init_arrangement.insert(i+1, int(second_half))
        justinserted = True

print(init_arrangement)

# len(str(12))

# print(str(init_arrangement[2])[(len(str(init_arrangement[2]))/2)])
