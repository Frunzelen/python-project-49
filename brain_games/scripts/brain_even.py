import random

import prompt

from brain_games.cli import welcome_user
from brain_games.scripts.brain_games import main


def main():
    count_point = 0
    name = welcome_user()
    while count_point <3:
        random_value = random.randint(-1000000000,1000000000)
        print(f'Question: {random_value}')
        answer = prompt.string('Your answer: ')
        if answer.lower() != 'yes' and answer.lower() != 'no':
            print('Uncorrect answer')
        if random_value % 2 == 0 and answer.lower() == 'yes':
            print('Correct')
            count_point += 1
        elif random_value % 2 != 0 and answer.lower() == 'no':
            print('Correct')
            count_point += 1
        elif answer.lower() == 'yes' and random_value % 2 != 0:
            print("'yes' is wrong answer ;(.Correct answer was 'no'.")
            print(f"Let's try again, {name}!")
            break
        elif answer.lower() == 'no' and random_value % 2 == 0:
            print("'no' is wrong answer ;(.Correct answer was 'yes'.")
            print(f"Let's try again, {name}!")
            break
    if count_point == 3:
        print(f'Cogratulations, {name}!')


print("brain-even\n")

if __name__ == "__main__":
    main()
