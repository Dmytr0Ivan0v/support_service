![logo](/logo.png)

## Adjust the application

### Install deps

```bash
# Install pipenv
pip install pipenv

# Activate virtual env
pipenv shell

# Install deps
pipenv sync --dev
```

#### Additional
```bash
# Regenerate Pipfile.lock file
pipenv lock

# pipenv lock & pipenv sync
pipenv update
```

## Used framefork

[Django 4.1.4](https://docs.djangoproject.com/en/4.1/ "documentation")

## Code quality tools

:mag: [flake8 6.0.0](https://flake8.pycqa.org/en/latest/#/ "documentation")\
:black_nib: [black 22.12.0](https://black.readthedocs.io/en/stable/ "documentation")\
:top: [isort 5.10.1](https://pycqa.github.io/isort// "documentation")
