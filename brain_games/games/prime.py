from random import randint


GAME_RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def data_prime(number):
    if number == 0 or number == 1:
        result = 'no'
    else:
        div = 0
        for i in range(2, number // 2 + 1):
            if number % i == 0:
                div = div + 1
                break
        result = 'yes' if div == 0 else 'no'
    return result


def get_question_and_correct_answer():
    number = randint(0, 100)
    question = str(number)
    result = data_prime(number)
    return question, result
