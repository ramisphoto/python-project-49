from random import randint


GAME_RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_and_correct_answer():
    number = randint(0, 1000)
    question = str(number)
    result = 'yes' if number % 2 == 0 else 'no'
    return question, result
