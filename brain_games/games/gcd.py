from random import randint


GAME_RULE = 'Find the greatest common divisor of given numbers.'


def gcd(number_1, number_2):
    remainder = number_1 % number_2
    if not remainder:
        return number_2
    return gcd(number_2, remainder)


def get_question_and_correct_answer():
    number_1 = randint(1, 100)
    number_2 = randint(1, 100)
    question = f'{number_1} {number_2}'
    result = gcd(number_1, number_2)
    return question, result
