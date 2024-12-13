file = open("exampledata.txt")

# TODO: init w/ 0, update w/ values from exampledata/data 
button_a_x = 94
button_a_y = 34

button_b_x = 22
button_b_y = 67

prize_x = 8400
prize_y = 5400

cost_button_a = 3
cost_button_b = 1

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

# compute remainder for other button to be pressed
remainder_x = prize_x - (button_b_x * 40) 
remainder_y = prize_y - (button_b_y * 40)

print(remainder_x)
print(remainder_y)

print(7520 / button_a_x) # 80
print(2720 / button_a_y) # 80 


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
