from random import randint


GAME_RULE = 'What number is missing in the progression?'


def data_progression():
    number = randint(1, 100)
    step = randint(4, 10)
    list_numbers = list(range(number, number + (10 * step), step))
    progression = list(map(str, list_numbers))
    random_index = randint(0, 9)
    return random_index, progression


def get_question_and_correct_answer():
    random_index, progression = data_progression()
    result = progression[random_index]
    progression[random_index] = '..'
    question = ' '.join(progression)
    return question, result
