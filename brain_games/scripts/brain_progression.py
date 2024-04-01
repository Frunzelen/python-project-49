import random

import prompt

from brain_games.cli import welcome_user


def generate_progression():
    length_int = random.randrange(5, 10)
    random_int = random.randrange(length_int)
    start = random.randrange(1, 100)
    step = random.randrange(1, 5)
    progression = [start + i * step for i in range(length_int)]
    progression[random_int] = '..'
    return (progression, progression[random_int]
            == '..', start + step * random_int)


def main():
    count_point = 0
    name = welcome_user()
    print('What number is missing in the progression?')
    while True:
        progression, is_hidden, res = generate_progression()
        print('Question:', end=' ')
        print(' '.join(map(str, progression)))
        answer = int(prompt.string('Your answer: '))
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


print('brain-progression\n')

if __name__ == "__main__":
    main()
