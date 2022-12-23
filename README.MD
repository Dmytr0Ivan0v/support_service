<img src="logo.png">

<h2><i><b>Adjust the application</i></b></h2>

<h3>Install deps<h3>

```bash
# Install pipenv
pip install pipenv

# Activate virtual env
pipenv shell

# Install deps
pipenv sync --dev
```

<h3>Additional</h3>

```bash
# Regenerate Pipfile.lock file
pipenv lock

# pipenv lock & pipenv sync
pipenv update
```

<h2><i>Framework</i></h2>

<a href="https://docs.djangoproject.com/en/4.1/" title="documentation"> Django 4.1.4</a>

<h2><i>Code quality tools</i></h2>

:mag: <a href="https://flake8.pycqa.org/en/latest/#/" title="documentation"> flake8 6.0.0</a>

:black_nib: <a href="https://black.readthedocs.io/en/stable/" title="documentation"> black 22.12.0</a>

:top: <a href="https://pycqa.github.io/isort//" title="documentation"> isort 5.10.1 </a>


<h2>Application description</h2>

```bash

▾ users

    ├─ apps.py # Django apps configuration
    ├─ urls.py # pre-controller
    # ├─ views.py # Endopints / post-controller
    ├─ models.py # Database tables mapper
    └─ admin.py # Database tables mapper
```