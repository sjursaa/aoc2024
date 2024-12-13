file = open("exampledata.txt")

# TODO: init w/ 0, update w/ values from exampledata/data 
button_a_x = 17
button_a_y = 86

button_b_x = 84
button_b_y = 37

prize_x = 7870
prize_y = 6450

cost_button_a = 3
cost_button_b = 1

"""
# TODO: sketchy solution find modulus of smallest value divided normally
print("result: ")
print((button_a_x * 80) + (button_b_x * 40))
print((button_a_y * 80) + (button_b_y * 40))

print("divide: ")
print(prize_x / button_a_x)
print(prize_y / button_a_y)
print(prize_x / button_b_x)
print(prize_y / button_b_y) # yields lowest number of the four tests

print("modulus: ")
print(prize_x % button_a_x) 
print(prize_y % button_a_y)
print(prize_x % button_b_x)
print(prize_y % button_b_y) # modulus of lowest value, number of times button B must be pressed
"""
# compute remainder for other button to be pressed
# TODO: loop for each number 1-100
remainder_x = 0
remainder_y = 0

for i in range(1,100):
    # print("hello")
    remainder_x = prize_x - (button_b_x * i) 
    remainder_y = prize_y - (button_b_y * i)

    print(remainder_x)
    print(remainder_y)

    button_ax_presses = (remainder_x / button_a_x) # 80
    button_ay_presses = (remainder_y / button_a_y) # 80 

    print(button_ax_presses)
    print(button_ay_presses)

    if button_ax_presses == button_ay_presses:
        print("bingbing")
        print("button_b:", i)
        print("button_a:", int(button_ax_presses))
        tokens = (i + button_ax_presses*3)
        print(tokens)
        # break
    print("nu")


"""
for line in file:
    print(line.strip())
    if line.startswith("Button A:"):
        print("Button A:")
        # TODO: get X and Y coords for button A
    if line.startswith("Button B:"):
        print("Button B:")
        # TODO: get X and Y coords for button B
    if line.startswith("Prize:"):
        print("Prize:")
        # TODO: get X and Y coords for prize
    if line == "\n":
        print("empty line")
        # TODO: put computations here
"""
