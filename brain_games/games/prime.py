import prompt
from random import randint
from brain_games.cli import welcome_user

name = welcome_user()


def prime():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    question_count = 0
    while question_count != 3:
        number = randint(0, 100)
        div = range(2, number)
        math_question = f'{number}'
#        if number == 2:
#            result = 'yes'
        if number == 0 or number == 1:
            result = 'no'
        else:
            for i in div:
                if number % i != 0:
                    result = 'yes'
                else:
                    result = 'no'
                    break
        print(f'Question: {math_question}')
        answer = prompt.string('Your answer: ')
        if answer == str(result):
            print('Correct!')
            question_count = question_count + 1
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{result}'. Let's try again, {name}!")
            return answer
    print(f'Congratulations, {name}!')
