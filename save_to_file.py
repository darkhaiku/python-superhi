from generate_land import ask_for_number, generate_land_function
import os



os.makedirs('outputs_folder', exist_ok=True)

for i in range(1,10):
    output = generate_land_function(10,10)
    filename = os.path.join('outputs_folder', f'test-{i}.txt')

    with open(filename , 'w') as f:
        f.write(output)
