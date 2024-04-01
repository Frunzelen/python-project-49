import random

import prompt

from brain_games.cli import welcome_user
from brain_games.scripts.brain_games import main


def main():
    count_point = 0
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while count_point < 3:
        random_value = random.randint(-1000, 1000)
        print(f'Question: {random_value}')
        answer = input('Your answer: ')
        if answer.lower() == "yes" and random_value % 2 == 0:
            print('Correct!')
            count_point += 1
        elif answer.lower() == "no" and random_value % 2 != 0:
            print('Correct!')
            count_point += 1
        else:
            print("'yes' is wrong answer ;(. "
                  "Correct answer was 'no'.\nLet's try again, " + name + "!")
            break
    else:
        print(f'Congratulations, {name}!')

print('brain-even\n')

if __name__ == "__main__":
    main()
