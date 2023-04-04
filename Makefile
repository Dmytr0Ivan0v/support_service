run:
	python src/manage.py runserver

# cq == Code Quality
cq:
	flake8 ./ && black ./ && isort ./ && mypy ./