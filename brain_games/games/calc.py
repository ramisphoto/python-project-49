from random import randint
from random import choice


game_rule = 'What is the result of the expression?'
operators = ['+', '-', '*']


def data_calc(number_1, number_2, random_operator):
    if random_operator == operators[0]:
        result = number_1 + number_2
    elif random_operator == operators[1]:
        result = number_1 - number_2
    elif random_operator == operators[2]:
        result = number_1 * number_2
    return result


def get_question_and_right_answer():
    number_1 = randint(0, 20)
    number_2 = randint(0, 20)
    random_operator = choice(operators)
    math_question = f'{number_1} {random_operator} {number_2}'
    result = data_calc(number_1, number_2, random_operator)
    return math_question, result
