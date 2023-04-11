import prompt
from random import randint


def even():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    question_count = 0
    while question_count != 3:
        number = randint(0, 1000)
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')
        if (number % 2 == 0 and answer == 'yes') or (
                number % 2 == 1 and answer == 'no'):
            print('Correct!')
            question_count = question_count + 1
        elif number % 2 == 1 and answer != 'no':
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was 'no'. Let's try again, {name}!")
            question_count = 0
        elif number % 2 == 0 and answer != 'yes':
            question_count = 0
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was 'yes'. Let's try again, {name}!")
    print(f'Congratulations, {name}!')
