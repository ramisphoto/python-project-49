from random import randint
from random import choice


GAME_RULE = 'What is the result of the expression?'
OPERATORS = ['+', '-', '*']


def data_calc(number_1, number_2, random_operator):
    if random_operator == OPERATORS[0]:
        result = number_1 + number_2
    elif random_operator == OPERATORS[1]:
        result = number_1 - number_2
    elif random_operator == OPERATORS[2]:
        result = number_1 * number_2
    return result


def get_question_and_correct_answer():
    number_1 = randint(0, 20)
    number_2 = randint(0, 20)
    random_operator = choice(OPERATORS)
    question = f'{number_1} {random_operator} {number_2}'
    result = data_calc(number_1, number_2, random_operator)
    return question, result
