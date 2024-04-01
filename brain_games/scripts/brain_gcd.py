import random

import prompt

from brain_games.cli import welcome_user


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def main():
    count_point = 0
    name = welcome_user()
    print("Find the greatest common divisor of given numbers.")
    while True:
        random_value1 = random.randint(1, 100)
        random_value2 = random.randint(1, 100)
        print(f'Question: {random_value1} {random_value2}')
        answer = int(input('Your answer: '))
        res = gcd(random_value1, random_value2)
        if answer == res:
            print('Correct!')
            count_point += 1
            if count_point >= 3:
                print(f'Congratulations, {name}!')
                break
        else:
            print(f'{answer} is wrong answer ;(.Correct answer was {res}')
            print(f'Let\'s try again, {name}!')
            break


print('brain-gcd\n')


if __name__ == "__main__":
    main()
