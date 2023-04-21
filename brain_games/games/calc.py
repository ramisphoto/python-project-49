import prompt
from random import randint
from random import choice
from brain_games.cli import welcome_user


name = welcome_user()


def calc():
    print('What is the result of the expression?')
    operators = ['+', '-', '*']
    question_count = 0
    while question_count != 3:
        number_1 = randint(0, 100)
        number_2 = randint(0, 100)
        number_3 = randint(0, 11)
        random_operators = choice(operators)
        if random_operators == operators[0]:
            math_question = f'{number_1} + {number_2}'
            result = str(number_1 + number_2)
        elif random_operators == operators[1]:
            math_question = f'{number_1} - {number_2}'
            result = str(number_1 - number_2)
        elif random_operators == operators[2]:
            math_question = f'{number_1} * {number_3}'
            result = str(number_1 * number_3)
        print(f'Question: {math_question}')
        answer = prompt.string('Your answer: ')
        if answer == result:
            print('Correct!')
            question_count = question_count + 1
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{result}'. Let's try again, {name}!")
            return answer
    print(f"Congratulation, {name}!")
