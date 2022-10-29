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


generate_land(5,5)

#calling function with default values 
generate_land()
