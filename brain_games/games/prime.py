from random import randint


game_rule = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question_and_right_answer():
    number = randint(0, 100)
    div = range(2, number)
    if number == 0 or number == 1:
        result = 'no'
    elif number == 2:
        result = 'yes'
    else:
        for i in div:
            if number % i != 0:
                result = 'yes'
            else:
                result = 'no'
                break
    return number, result
