import prompt
from random import randint
from brain_games.cli import welcome_user

name = welcome_user()


def even():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    question_count = 0
    while question_count != 3:
        number = randint(0, 1000)
        math_question = f'{number}'
        if number % 2 == 0:
            result = 'yes'
        else:
            result = 'no'
        print(f'Question: {math_question}')
        answer = prompt.string('Your answer: ')
        if answer == result:
            print('Correct!')
            question_count = question_count + 1
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{result}'. Let's try again, {name}!")
            return answer
    print(f'Congratulations, {name}!')
