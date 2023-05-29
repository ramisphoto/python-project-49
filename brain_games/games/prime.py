from random import randint


GAME_RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    divisors = 0
    if number == 0 or number == 1:
        divisors = 1
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            divisors += 1
            break
    return divisors == 0


def get_question_and_correct_answer():
    number = randint(0, 100)
    question = str(number)
    result = 'yes' if is_prime(number) else 'no'
    return question, result
