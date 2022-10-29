import random

def generate_land(cols=10, rows=10):
    data = ['a', 'b', 'c', 'd', 'e', 'f']
    print(f'Generate a landscape [cols: {cols}] [rows: {rows}]')
    for row in range(rows):
        row_string = ''
        for col in range(cols):
            r = random.choice(data)
            row_string += r
        print(row_string)
    print('finished generating landscape')

def ask_for_number(question):
    tries = 0

    while tries < 3:
        answer = input(question)

        if answer == 'quit':
            quit()
            
        if answer.isnumeric():
            return int(answer)
        else:
            print("Oops this didn't make sense!")
            tries += 1
    print("This is NOT funny bitch")
    quit()

cols = ask_for_number("How many cols? ")
rows = ask_for_number("How many rows? ")
generate_land(cols, rows)
