import collections
import random

from termcolor import colored, cprint
from noise import pnoise2

def generate_land(cols=10, rows=10):
    data = ['a', 'b', 'c', 'd', 'e', 'f']
    print(f'Generate a landscape [cols: {cols}] [rows: {rows}]')
    for row in range(rows):
        row_string = ''


        for col in range(cols):
            n = pnoise2(row/rows, col, cols)
            n *= 100 # n = n * 100 
            n = round(n)
            n = n % len(data)
            print(n)
            r = random.choice(data)
            row_string += r
        print(row_string)
    print('finished generating landscape')

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

cols = ask_for_number("How many cols? ")
rows = ask_for_number("How many rows? ")
generate_land(cols, rows)
