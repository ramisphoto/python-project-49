import prompt
from random import randint
from brain_games.cli import welcome_user


name = welcome_user()


def find_divider(number_1, number_2):
    if number_1 >= number_2:
        divider = number_2
        rest = number_1 % divider
    else:
        divider = number_1
        rest = number_2 % divider
    if rest == 0:
        result = divider
    while divider and rest != 0:
        divider = divider % rest
        if divider == 0:
            result = rest
            break
        rest = rest % divider
        if rest == 0:
            result = divider
            break
    return result


def gcd():
    print('Find the greatest common divisor of given numbers.')
    question_count = 0
    while question_count != 3:
        number_1 = randint(1, 100)
        number_2 = randint(1, 100)
        math_question = f'{number_1} {number_2}'
        result = find_divider(number_1, number_2)
        print(f'Question: {math_question}')
        answer = prompt.string('Your answer: ')
        if answer == str(result):
            print('Correct!')
            question_count = question_count + 1
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{result}'. Let's try again, {name}!")
            return answer
    print(f'Congratulations, {name}!')
