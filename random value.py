import random
name = 'bob'
random_value = random.randint()
print(f'Question: {random_value}')
Answer = input("Введите ответ)"
               "_value % 2 !=0 and Answer.lower == 'no'):
            print('Correct')
            count_point +=1
            if count_point == 3:
                print(f'Cogratulations {name}!')
                break
    else:
        if Answer.lower == 'yes':
            print("'yes' is wrong answer ;(.Correct answer was 'no'.")
            print(f"Let's try again, {name}!")
        else:
            print("'no' is wrong answer ;(.Correct answer was 'yes'.")
            print(f"Let's try again, {name}!")