import random
cols = 12
rows = 20
total = cols * rows

data = ['a', 'b', 'c', 'd', 'e', 'f']

print(f'Generate a landscape which is {cols} by {rows}')

for col in range(cols):
    r = random.choice(data)
    print(f'message {r}')

print('finished generating landscape')