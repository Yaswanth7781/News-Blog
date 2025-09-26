# News-Blog
This project is developed using Django and PostgreSQL. It provides role-based access control where  Admin can Add, update, delete news posts., Users can Register, login, and view news. The system ensures secure authentication and an easy way to manage and share news content.

Django News Platform
A dynamic, full-featured news website built with Django and backed by a PostgreSQL database. This platform allows administrators to manage news content, while a robust, group-based authentication system controls who can create, edit, and delete articles.

Features
Dynamic Content: Add, update, and delete news articles seamlessly.

User Authentication: Secure user signup, login, and logout functionality.

Role-Based Permissions: A flexible system where only users in a specific "Authors" group can post news.

Author-Specific Control: Authors can only edit or delete their own articles.

Admin Panel: A powerful backend interface to manage users, groups, and all news content.

Responsive Design: A clean and modern user interface that works on both desktop and mobile devices.

Tech Stack
Backend: Django

Database: PostgreSQL

Frontend: HTML, CSS, JavaScript

Python Packages: psycopg2-binary

Installation and Setup
Follow these steps to get a local copy of the project up and running.

1. Prerequisites
Python (3.8+)

PostgreSQL

Git

2. Clone the Repository
git clone [https://github.com/your-username/your-repository-name.git](https://github.com/your-username/your-repository-name.git)
cd your-repository-name

3. Set Up a Virtual Environment
It's highly recommended to use a virtual environment to manage project dependencies.

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate

# For Windows
python -m venv venv
.\venv\Scripts\activate

4. Install Dependencies
Install Django and the required PostgreSQL database driver.

pip install -r requirements.txt

(Note: You will need to create a requirements.txt file by running pip freeze > requirements.txt in your project.)

5. Set Up the PostgreSQL Database
Open the PostgreSQL command line (psql).

Create a database for the project:

CREATE DATABASE news_db;

Create a dedicated user for the database:

CREATE USER news_user WITH PASSWORD 'your_secure_password';

Grant the new user full privileges on the database:

GRANT ALL PRIVILEGES ON DATABASE news_db TO news_user;

6. Configure Django Settings
Open the news_project/settings.py file.

Update the DATABASES configuration with your credentials from the previous step.

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'news_db',
        'USER': 'news_user',
        'PASSWORD': 'your_secure_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

7. Run Database Migrations
Apply the database schema and create the necessary tables.

python manage.py makemigrations
python manage.py migrate

8. Create a Superuser
This account will be used to access the Django admin panel.

python manage.py createsuperuser

Follow the prompts to set up your username, email, and password.

9. Start the Server
python manage.py runserver

The website is now running at https://www.google.com/search?q=http://127.0.0.1:8000/.

Admin Usage: Managing Authors
To control who can post news, you must add users to the "Authors" group.

1. Create the "Authors" Group
Navigate to the admin panel: http://127.0.0.1:8000/admin/

Log in with your superuser account.

Go to Home › Authentication and Authorization › Groups and click "+ Add group".

Set the "Name" to Authors (capitalization is important).

Click SAVE.

2. Assign a User to the "Authors" Group
In the admin panel, click on Users.

Select the user you want to grant posting rights to.

In the "Permissions" section, select Authors from the "Available groups" and move it to the "Chosen groups" box using the arrow.

Click SAVE.

The selected user will now see the "New Post" button and will be able to create, edit, and delete their own articles.

Contributing
Contributions are welcome! If you have suggestions for improving the project, please fork the repository and create a pull request, or open an issue with the "enhancement" tag.
View in code so you will get clear structure
File Structure
.
├── manage.py                 # Django's main command-line utility.
├── README.md                 # Your setup and installation guide.
|
├── news_project/             # The main Django project folder.
│   ├── __init__.py
│   ├── settings.py           # Project settings (database, apps, etc.).
│   ├── urls.py               # Main URL router for the project.
│   └── wsgi.py               # WSGI entry-point for the web server.
│
├── news/                     # The 'news' app folder.
│   ├── __init__.py
│   ├── admin.py              # Registers models with the Django admin site.
│   ├── models.py             # Defines the database structure (Article model).
│   ├── urls.py               # URL routing specific to the news app.
│   └── views.py              # Contains the logic for handling requests (e.g., displaying articles).
│
├── templates/                # Contains all HTML templates for the site.
│   ├── base.html             # The main template that others extend.
│   ├── home.html             # The homepage template.
│   ├── article_detail.html   # Template for a single article view.
│   ├── article_form.html     # Template for creating/editing articles.
│   ├── article_confirm_delete.html # Confirmation page for deleting.
│   └── registration/         # Templates related to user authentication.
│       ├── login.html
│       └── signup.html
│
└── static/                   # Contains static files like CSS and JS.
    ├── css/
    │   └── style.css         # The main stylesheet.
    └── js/
        └── script.js         # JavaScript file.
