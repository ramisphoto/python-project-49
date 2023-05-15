from random import randint


game_rule = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question_and_right_answer():
    number = randint(0, 100)
    div = 0
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            div = div + 1
            break
    result = 'yes' if div == 0 else 'no'
    return number, result
