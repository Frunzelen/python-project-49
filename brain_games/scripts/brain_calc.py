import random

import prompt

from brain_games.cli import welcome_user
from brain_games.scripts.brain_games import main


def conditions():
    random_value1 = random.randint(-10, 10)
    random_value2 = random.randint(-10, 10)
    math_operand = ['+', '-', '*']
    random_math_operation = random.choice(math_operand)
    print(f'Question: {random_value1} {random_math_operation} {random_value2}')
    if random_math_operation == '+':
        result = random_value1 + random_value2
    if random_math_operation == '-':
        result = random_value1 - random_value2
    if random_math_operation == '*':
        result = random_value1 * random_value2
    return result


def main():
    count_point = 0
    name = welcome_user()
    while count_point < 3:
        res = int(conditions())
        answer = int(input('Your answer: '))
        if res == answer:
            print('Correct')
            count_point += 1
        else:
            print(f'{answer} is wrong answer ;(.Correct answer was {res}')
            print(f'Let\'s try again, {name}!')
            break
    if count_point == 3:
        print(f'Cogratulations, {name}!')


print('brain-calc\n')

if __name__ == "__main__":
    main()
