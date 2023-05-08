from random import randint


game_rule = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_and_right_answer():
    number = randint(0, 1000)
    if number % 2 == 0:
        result = 'yes'
    else:
        result = 'no'
    return number, result
