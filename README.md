# TracX

This is an expense and income tracking website created using Django web framework with PostgreSQL as a database. The website allows users to track their expenses and incomes, as well as provides intuitive visual graphs for the expenses and income categories.

## Features

* User registration and authentication
* Add, edit and delete expenses
* Add, edit and delete incomes
* Categorize expenses and incomes
* View expenses and incomes by category or date 
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

3. Install dependencies mention in the pipfile


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
<img width="1278" alt="1" src="https://user-images.githubusercontent.com/72565305/222901401-7f4847cc-9c1e-42ef-b3fb-8a03d134ea22.png">
<img width="1278" alt="Screenshot 2023-03-04 at 5 59 54 PM" src="https://user-images.githubusercontent.com/72565305/222901414-b6854c2c-8e37-434a-a13b-4b9a15b1d205.png">
<img width="1278" alt="Screenshot 2023-03-04 at 6 00 29 PM" src="https://user-images.githubusercontent.com/72565305/222901420-69f3d2e6-f0a2-4812-a72b-bce334d4ebda.png">
<img width="1278" alt="Screenshot 2023-03-04 at 6 00 54 PM" src="https://user-images.githubusercontent.com/72565305/222901432-4881cb73-72db-41c7-9251-d874cb788cc1.png">
<img width="1278" alt="Screenshot 2023-03-04 at 6 01 02 PM" src="https://user-images.githubusercontent.com/72565305/222901438-4897d668-e1c7-4256-9e4d-9d4e83a4dbd4.png">
<img width="1278" alt="Screenshot 2023-03-04 at 6 01 23 PM" src="https://user-images.githubusercontent.com/72565305/222901440-d2045284-add5-414e-bacf-f3610a95cf0c.png">
<img width="1278" alt="Screenshot 2023-03-04 at 6 01 33 PM" src="https://user-images.githubusercontent.com/72565305/222901444-754c94d7-614c-4c69-8596-6e058e836c5e.png">
