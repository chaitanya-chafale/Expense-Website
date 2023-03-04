# TracX

This is an expense and income tracking website created using Django web framework with PostgreSQL as a database. The website allows users to track their expenses and incomes, as well as provides intuitive visual graphs for the expenses and income categories.

## Features

* User registration and authentication
* Add, edit and delete expenses
* Add, edit and delete incomes
* Categorize expenses and incomes
* View expenses and incomes by category or date range 
* View expense and income history and statistics
* Intuitive visual graphs for expense and income categories

## Technology Stack

* Frontend: HTML/CSS, JavaScript, Bootstrap
* Backend: Python
* Web Framework: Django
* Database: PostgreSQL

## Getting Started

1. Clone the repository

```

git clone https://github.com/chaitanya-chafale/Expense-Website.git

```

2. Create a virtual environment and activate it

```

python -m venv env
source env/bin/activate

```

3. Install dependencies mention in th pipfile


4. Create a PostgreSQL database and add the database credentials to settings.py


5. Run database migrations

```

python manage.py makemigrations
python manage.py migrate

```

6. Start the development server

```

python manage.py runserver

```

7. Open the website in your browser at http://localhost:8000

Note:- The category need to be inserted manually in the expense and income db using the http://localhost:8000/admin (Login using superuser, create using the command python manage.py createsuperuser) or using the shell. [Working on Adding this in the next release]

## Screenshots



