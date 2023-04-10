install: #создание вирт.окружения, установка пакета
	poetry install

brain-games: #запуск приложения
	poetry run brain-games

build: #сборка пакета
	poetry build

publish: #отладка публикации
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

lint: #запуск линтера
	poetry run flake8 brain_games 
