import random

from brain_games.cli import welcome_user


def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def main():
    count_point = 0
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    while True:
        num = random.randint(1, 100)
        answer = input(f'Question: {num}\nYour answer: ')
        if (is_prime(num) and answer.lower() == 'yes') or \
                (not is_prime(num) and answer.lower() == 'no'):
            count_point += 1
            print('Correct!')
            if count_point >= 3:
                print(f'Congratulations, {name}!')
                break
        elif is_prime(num) and answer.lower() == 'no':
            print(f'{answer} is wrong answer ;(.Correct answer was "yes"')
            print(f'Let\'s try again, {name}!')
            break
        elif not is_prime(num) and answer.lower() == 'yes':
            print(f'{answer} is wrong answer ;(.Correct answer was "no"')
            print(f'Let\'s try again, {name}!')
            break


print('brain-prime\n')


if __name__ == "__main__":
    main()
