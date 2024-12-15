file = open("exampledata.txt")
# file = open("data.txt")

# TODO: init w/ 0, update w/ values from exampledata/data 
button_a_x = 0
button_a_y = 0

button_b_x = 0
button_b_y = 0

prize_x = 0
prize_y = 0

cost_button_a = 3
cost_button_b = 1

total_tokens = 0
win = 0
game = 0
remainder_x = 0
remainder_y = 0
list_of_tokens = []

for line in file:
    if line.startswith("Button A:"):
        print("Button A:")
        line.find("Button A: ,")
        first_half = line.split(",")[0]
        second_half = line.split(",")[1]
        button_a_x = int(''.join(filter(str.isdigit, first_half)))
        button_a_y = int(''.join(filter(str.isdigit, second_half)))
        print(button_a_x)
        print(button_a_y)
        # button_a_y = button_a_y_list[0]
    if line.startswith("Button B:"):
        print(line)
        line.find("Button B: ,")
        first_half = line.split(",")[0]
        second_half = line.split(",")[1]
        button_b_x = int(''.join(filter(str.isdigit, first_half)))
        button_b_y = int(''.join(filter(str.isdigit, second_half)))
        print(button_b_x)
        print(button_b_y)
    if line.startswith("Prize:"):
        game += 1
        print("Prize:")
        print(line)
        line.find("Prize: ,")
        first_half = line.split(",")[0]
        second_half = line.split(",")[1]
        prize_x = int(''.join(filter(str.isdigit, first_half)))
        prize_y = int(''.join(filter(str.isdigit, second_half)))
        # pt. 2 tweak:
        # prize_x += 10000000000000
        # prize_y += 10000000000000
        print(prize_x)
        print(prize_y)

        # TODO: find good start and stop values for indexing 
        start_index = 0
        end_index = 100
        for i in range(0, 600):
            print(i)
            remainder_x = prize_x - (button_b_x * i*10) 
            remainder_y = prize_y - (button_b_y * i*10)

            if remainder_x <= 0 or remainder_y <= 0:
                start_index = (i - 1)*10
                end_index = (i)*10
                break

        for i in range(0, 100):
            # print(startingpoints[0], startingpoints[1], startingpoints[2], startingpoints[3])
            remainder_x = prize_x - (button_b_x * i) 
            remainder_y = prize_y - (button_b_y * i)

            print(i)
        
            print("remainder_x", remainder_x)
            print("remainder_y", remainder_y)

            button_ax_presses = (remainder_x / button_a_x) # 80
            button_ay_presses = (remainder_y / button_a_y) # 80 

            # print(button_ax_presses)
            # print(button_ay_presses)

            if button_ax_presses == button_ay_presses:
                print("bingbing")
                print("button_b:", i)
                print("button_a:", int(button_ax_presses))
                tokens = (i + button_ax_presses*3)
                print(tokens)
                list_of_tokens.append(tokens)
                total_tokens += tokens
                win += 1
                break
            if (remainder_x < 0 or remainder_y < 0 ) :
                break
    if line == "\n":
        print("empty line")

print(int(total_tokens))
print(win, "/", game)

# for token in list_of_tokens:
#     print(int(token))


