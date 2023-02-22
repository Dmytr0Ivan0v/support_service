<img src="logo.png">

<h2><i><b>Adjust the application</i></b></h2>

<h3>Create `.env` file based on `.env.default`</h3>

```bash
# Unix
cp .env.default .env
```

<h3>Install deps</h3>

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

<a href=https://www.django-rest-framework.org> Django REST framework 3.14.0</a>

<h2><i>Code quality tools</i></h2>

:mag: <a href="https://flake8.pycqa.org/en/latest/#/" title="documentation"> flake8 6.0.0</a>

:black_nib: <a href="https://black.readthedocs.io/en/stable/" title="documentation"> black 22.12.0</a>

:top: <a href="https://pycqa.github.io/isort//" title="documentation"> isort 5.10.1 </a>


<h2><i>Run using Docker Compose</h2></i>

```bash
docker-compose up -d
```

<h3>Usefull commands</h3>

<h4>Containers</h4>

```bash
:building_construction: Build images
docker-compose build

:arrow_forward: Start containers
docker-compose up -d

:stop_button: Stop containers
docker-compose down

:repeat: Restart containers
docker-compose restart

:grey_question: Check containers status
docker-compose ps
```

<h4>Logs</h4>

```bash
:shopping_cart: get all logs
docker-compose logs

:dart: get specific logs
docker-compose logs app

:game_die: get limited logs
docker-compose logs --tail 10 app

:kite: get flowed logs
docker-compose logs -f app
```

<h2>Application description</h2>

```bash

▾ users

    ├─ apps.py # Django apps configuration
    ├─ urls.py # pre-controller
    ├─ api.py # Endopints / post-controller
    ├─ models.py # Database tables mapper
    └─ admin.py # Database tables mapper
```


<h2>Database</h2>

```mermaid

erDiagram
    Users {
        int id
        string frist_name
        string last_name
        string email
        string password
        bool is_staff
        bool is_active
        string role
        datetime created_at
        datetime updated_at
    }
    Tickets {
        int id
        int customer_id
        int manager_id
        string header
        text body
        datetime created_at
        datetime updated_at
    }
    Comments {
        int id
        int prev_comment_id
        int user_id
        int ticket_id
        text body
        datetime created_at
        datetime updated_at
    }

    Users ||--o{ Tickets : ""
    Tickets ||--o{ Comments : ""
    Comments ||--o{ Comments : ""

```