install: #создание вирт.окружения, установка пакета
	poetry install

brain-games: #запуск приложения (только приветствие)
	poetry run brain-games

build: #сборка пакета
	poetry build

publish: #отладка публикации
	poetry publish --dry-run

package-install: #установка пакета
	python3 -m pip install --user dist/*.whl

package-reinstall: #удаление и переустановка пакета
	python3 -m pip install --user --force-reinstall dist/*.whl

lint: #запуск линтера
	poetry run flake8 brain_games

brain-even: #запуск игры на четность
	poetry run brain-even

brain-calc: #запуск игры на вычисления
	poetry run brain-calc

brain-gcd: #запуск игры на НОД
	poetry run brain-gcd
