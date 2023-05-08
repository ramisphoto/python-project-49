from random import randint
from random import choice


game_rule = 'What is the result of the expression?'


def data_calc():
    operators = ['+', '-', '*']
    number_1 = randint(0, 100)
    number_2 = randint(0, 100)
    number_3 = randint(0, 11)
    random_operators = choice(['+', '-', '*'])
    return number_1, number_2, number_3, operators, random_operators


def get_question_and_right_answer():
    number_1, number_2, number_3, operators, random_operators = data_calc()
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
