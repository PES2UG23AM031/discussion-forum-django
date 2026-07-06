# Discussion Forum using Django

A web-based discussion forum developed using **Python**, **Django**, **HTML**, **CSS**, **Bootstrap**, and **SQLite**. The application allows users to create discussion topics, post questions, reply to discussions, search content, and manage their own posts through a secure authentication system.

---

## Features

- User Registration and Login
- User Authentication using Django Authentication System
- Create and Manage Discussion Topics
- Post Questions
- Reply to Questions
- Edit and Delete Own Posts
- Search Questions
- User Profile Management
- Responsive Bootstrap 5 Interface

---

## Tech Stack

- Python
- Django
- HTML5
- CSS3
- Bootstrap 5
- SQLite

---

## Project Structure

```text
Discussion Forum/
│── manage.py
│── requirements.txt
│── README.md
│
├── discussion_forum/
├── forum_app/
├── templates/
├── static/
```

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/PES2UG23AM031/discussion-forum-django.git
cd discussion-forum-django
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Environment

Windows

```bash
.venv\Scripts\activate
```

Linux/Mac

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Create Superuser

```bash
python manage.py createsuperuser
```

### Run Server

```bash
python manage.py runserver
```

Open:

```
http://127.0.0.1:8000/
```

---

## Future Enhancements

- Email Notifications
- Image Upload Support
- Like and Comment System
- Rich Text Editor
- Pagination
- Dark Mode

---

## Author

**Devi Sai Sanjana N**

GitHub:
https://github.com/PES2UG23AM031

LinkedIn:
https://linkedin.com/in/sanjana-n-8267a6340
