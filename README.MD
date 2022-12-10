# <span style='color:blue' >Support servise application</span>

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

```bash
Django 4.1.4
```


## Code quality tools

```bash
flake8 5.0.4
black 22.10.0
isort 5.10.1
```