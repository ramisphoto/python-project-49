from random import randint
from random import choice


game_rule = 'What is the result of the expression?'


def calc():
    operators = ['+', '-', '*']
    number_1 = randint(0, 100)
    number_2 = randint(0, 100)
    number_3 = randint(0, 11)
    random_operators = choice(operators)
    if random_operators == operators[0]:
        math_question = f'{number_1} + {number_2}'
        result = number_1 + number_2
    elif random_operators == operators[1]:
        math_question = f'{number_1} - {number_2}'
        result = number_1 - number_2
    elif random_operators == operators[2]:
        math_question = f'{number_1} * {number_3}'
        result = number_1 * number_3
    return math_question, result


def Q_A():
    question, correct_answer = calc()
    return question, correct_answer
