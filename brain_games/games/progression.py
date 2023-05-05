from random import randint
from random import choice


game_rule = 'What number is missing in the progression?'


def progression():
    number_1 = randint(1, 10)
    number_2 = randint(1, 100)
    for_fun = randint(4, 10)
#   list_numbers_1 = range(number_1, number_1 + 10)
    list_numbers_2 = range(number_2, number_2 + (10 * for_fun), for_fun)
#   sq = list(map(lambda num: str(num ** 2), list_numbers_1))
    sub = list(map(lambda num:
               str(num - number_1), reversed(list_numbers_2)))
    summ = list(map(lambda num: str(num + number_1), list_numbers_2))
#   div = [number_1]
#   previous = 0
#   current = number_1
#   for index in range(0, 9):
#       next_one = current + previous
#       div.append(next_one)
#       previous = current
#       current = next_one
#   div = list(map(str, div))
    random_index = randint(0, 9)
    list_progression = [sub, summ]
    progression = choice(list_progression)
    result = progression[random_index]
    progression.insert(random_index, '..')
    progression.pop(random_index + 1)
    math_question = ' '.join(progression)
    return math_question, result


def Q_A():
    question, correct_answer = progression()
    return question, correct_answer
