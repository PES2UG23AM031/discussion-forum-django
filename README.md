# Discussion Forum

A beginner-friendly Django mini-project where users can register, create discussion topics, ask questions, reply to questions, search posts, and manage only their own content.

## Complete Folder Structure

```text
Discussion Forum/
|-- manage.py
|-- requirements.txt
|-- README.md
|-- discussion_forum/
|   |-- __init__.py
|   |-- settings.py
|   |-- urls.py
|   |-- wsgi.py
|   `-- asgi.py
|-- forum_app/
|   |-- __init__.py
|   |-- admin.py
|   |-- apps.py
|   |-- forms.py
|   |-- models.py
|   |-- urls.py
|   |-- views.py
|   `-- migrations/
|       `-- __init__.py
|-- templates/
|   |-- base.html
|   |-- forum_app/
|   |   |-- home.html
|   |   |-- topic_detail.html
|   |   |-- question_detail.html
|   |   |-- question_form.html
|   |   |-- reply_form.html
|   |   |-- confirm_delete.html
|   |   |-- profile.html
|   |   `-- search_results.html
|   `-- registration/
|       |-- login.html
|       `-- register.html
`-- static/
    |-- css/
    |   `-- style.css
    |-- js/
    |   `-- main.js
    `-- images/
        `-- .gitkeep
```

## Setup Instructions

1. Open a terminal in the project folder:

   ```bash
   cd "Discussion Forum"
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create database tables:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Create an admin user:

   ```bash
   python manage.py createsuperuser
   ```

6. Start the development server:

   ```bash
   python manage.py runserver
   ```

7. Visit:

   ```text
   http://127.0.0.1:8000/
   ```

## Main Features

- Registration, login, logout, and password hashing through Django authentication.
- Topic creation and topic list with question counts.
- Questions with title, description, author, timestamp, edit, and delete permissions.
- Replies with author, content, timestamp, edit, and delete permissions.
- Search by question title or description.
- User profile with username, email, join date, question count, and reply count.
- Bootstrap 5 responsive interface with reusable template inheritance.
