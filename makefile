run:
	python main.py

migrate:
	poetry run python manage.py migrate

makemigrations:
	poetry run python manage.py makemigrations

path:
	poetry env info --path



