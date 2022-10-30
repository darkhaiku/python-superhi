from generate_land import ask_for_number, generate_land_function

output = generate_land_function(10,10)

with open('test.txt', 'w') as f:
    f.write(output)
    