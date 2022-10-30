import collections
import random

from termcolor import colored, cprint
from noise import pnoise2

def generate_land_function(cols=10, rows=10):
    data = ['.','-','*','$','#','#','$','*','-','.']
    seed = random.randint(0, 100)
    land = ''


    print(f'Generate a landscape [cols: {cols}] [rows: {rows}]')
    for row in range(rows):


        for col in range(cols):
            n = pnoise2(row/rows, col, cols, base=seed)
            n *= 100 # n = n * 100
            n = round(n)
            n = n % len(data)

            land += data[n]
        land += '\n'
        
    print('finished generating landscape')
    return land

def ask_for_number(question):
    tries = 0

    while tries < 3:
        answer = input(colored(question, 'green'))

        if answer == 'quit':
            quit()

        elif answer.isnumeric():
            return int(answer)
        else:
            print(colored("Oops this didn't make sense!", 'yellow'))
            tries += 1
    print(colored("This is NOT funny bitch", 'red'))
    quit()

if __name__ == '__main__':
    cols = ask_for_number("How many cols? ")
    rows = ask_for_number("How many rows? ")
    output = generate_land_function(cols, rows)
    print(output)

