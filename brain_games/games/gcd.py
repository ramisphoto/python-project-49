from random import randint


game_rule = 'Find the greatest common divisor of given numbers.'


def gcd():
    number_1 = randint(1, 100)
    number_2 = randint(1, 100)
    math_question = f'{number_1} {number_2}'
    if number_1 >= number_2:
        divider = number_2
        rest = number_1 % divider
    else:
        divider = number_1
        rest = number_2 % divider
    if rest == 0:
        result = divider
    while divider and rest != 0:
        divider = divider % rest
        if divider == 0:
            result = rest
            break
        rest = rest % divider
        if rest == 0:
            result = divider
            break
    return math_question, result


def Q_A():
    question, correct_answer = gcd()
    return question, correct_answer
