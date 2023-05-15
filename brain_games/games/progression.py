from random import randint
from random import choice


game_rule = 'What number is missing in the progression?'


def data_progression():
    number_1 = randint(1, 10)
    number_2 = randint(1, 100)
    for_fun = randint(4, 10)
    list_numbers_2 = range(number_2, number_2 + (10 * for_fun), for_fun)
    sub = list(map(lambda num:
               str(num - number_1), reversed(list_numbers_2)))
    summ = list(map(lambda num: str(num + number_1), list_numbers_2))
    random_index = randint(0, 9)
    list_progression = [sub, summ]
    progression = choice(list_progression)
    return random_index, progression


def get_question_and_right_answer():
    random_index, progression = data_progression()
    result = progression[random_index]
    progression[random_index] = '..'
    math_question = ' '.join(progression)
    return math_question, result
