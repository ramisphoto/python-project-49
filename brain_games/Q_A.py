import prompt
from brain_games.games.even import even, result
from brain_games.cli import welcome_user
#from brain_games.games.calc import calc

name = welcome_user()


result = even()


def Q_A():
    print(f'Question:{math_question}')
    answer = prompt.string('Your answer: ')
    if answer == result:
        print ('Correct!')
        question_count = question_count + 1
    else:
        question_count = 0
        print(f"'{answer}' is wrong answer ;(. "
              f"Correct answer was '{result}'. Let's try again, {name}!")
    print(f'Congratulations, {name}!')


#games = ['brain-even', 'brain-calc']
#print(f"{name}, choose a game: " + ', '.join(games))
#chosen_game = prompt.string('Yout choice: ')
#if chosen_game == games[0]:
#result = even()
#elif chosen_game == games[1]:
#result = calc()
