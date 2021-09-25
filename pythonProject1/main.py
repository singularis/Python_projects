from random import randint
start = 1
end = 10
generated_num = randint(start, end)


def run_quess(guess, answer):
    if start <= guess <= end:
        if guess == answer:
            print('you are a genius!')
            return True
        else:
            print('Try again')
            return False


if __name__ == '__main__':
    while True:
        try:
            guess_num = int(input(f'Please give a number in range {start}, {end} '))
            if run_quess(guess_num, generated_num):
                break
        except ValueError:
            print('Please enter a number')
            continue
