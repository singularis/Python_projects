import sys
from random import randint
start = int(sys.argv[1])
end = int(sys.argv[2])

generated_num = randint(start, end)

while True:
    try:
        guess_num = int(input(f'Please give a number in range {start}, {end} '))
        if guess_num < start or guess_num > end:
            print('Out of range')
            continue
        if guess_num == generated_num:
            print('You are genius')
            break
        else:
            print('Try again')
    except ValueError:
        print('Please enter a number')
