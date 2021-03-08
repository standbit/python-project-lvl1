import prompt
import random

int_begin = 1
int_end = 100
try_for_win = 3


def take_random_val(begin, end):
    random_num = random.randint(begin, end)
    return random_num


def even(random_num):
    if random_num % 2 == 0:
        return 'yes'
    return 'no'


def even_check():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print("Hello, {}!".format(name))
    print('Answer "yes" if the number is even, otherwise answer "no".')
    num_of_try = 0
    while num_of_try != try_for_win:
        random_num = take_random_val(int_begin, int_end)
        print("Question: {}".format(random_num))
        answer = prompt.string('Your answer: ')
        if answer == even(random_num):
            print('Correct!')
            num_of_try += 1
        else:
            print(answer + ' is wrong answer ;(.', end='')
            print('Correct answer was ' + even(random_num))
            print("Let's try again, {}!".format(name))
            break
    if num_of_try == 3:
        print('Congratulations, {}!'.format(name))
