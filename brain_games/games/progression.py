import prompt
from random import randint
from random import choice
from brain_games.cli import welcome_user


name = welcome_user()


def progression():
    print('What number is missing in the progression?')
    question_count = 0
    while question_count != 3:
        number_1 = randint(1, 10)
        number_2 = randint(1, 100)
        for_fun = randint(4, 10)
        list_numbers_1 = range(number_1, number_1 + 10)
        list_numbers_2 = range(number_2, number_2 + (10 * for_fun), for_fun)
        sq = list(map(lambda num: str(num ** 2), list_numbers_1))
        sub = list(map(lambda num: str(num - number_1), reversed(list_numbers_2)))
        summ = list(map(lambda num: str(num + number_1), list_numbers_2))
        div = [number_1]
        previous = 0
        current = number_1
        for index in range(0, 9):
            next_one = current + previous
            div.append(next_one)
            previous = current
            current = next_one
        div = list(map(str, div))
        random_index = randint(0, 9)
        list_progression = [sq, sub, summ, div]
        progression = choice(list_progression)
        result = progression[random_index]
        progression.insert(random_index, '..')
        progression.pop(random_index + 1)
        math_question = ' '.join(progression)
        print(f'Question: {math_question}')
        answer = prompt.string('Your answer: ')
        if answer == str(result):
            print('Correct!')
            question_count = question_count + 1
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{result}'.")
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
