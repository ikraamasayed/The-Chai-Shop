# The Chai Shop

A Django learning project for managing chai varieties and exploring relational database modelling through the Django ORM.

## Overview

The Chai Shop is a server-rendered Django application that displays chai varieties, provides individual detail pages, and allows users to find stores offering a selected chai variety.

The project explores Django models, relationships, migrations, views, templates, media handling, and Django Admin.

## Tech Stack

- Python
- Django 5.2.6
- SQLite
- Django ORM
- Django Templates
- Tailwind CSS 4
- Node.js and npm

## Features

- Browse chai varieties.
- View individual chai details.
- Store and display chai images.
- Search stores by chai variety.
- Manage chai data through Django Admin.
- Demonstrate one-to-one, one-to-many, and many-to-many relationships.

## Database Models

| Model | Purpose |
|---|---|
| ChaiVariety | Stores chai details and images |
| ChaiReview | Stores user reviews and ratings |
| Store | Stores locations and available chai varieties |
| ChaiCertificate | Stores certificate information |

## Project Structure

```text
The-Chai-Shop/
├── chaiaurdjango/
│   ├── chai/
│   │   ├── migrations/
│   │   ├── templates/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── forms.py
│   │   └── admin.py
│   ├── chaiaurdjango/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── templates/
│   ├── media/
│   ├── static/
│   └── manage.py
└── README.md
```

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/ikraamasayed/The-Chai-Shop.git
cd The-Chai-Shop/chaiaurdjango
```

### 2. Create a virtual environment

```bash
uv venv
```

Activate on Windows:

```powershell
.venv\Scripts\activate
```

### 3. Install dependencies

Install Django, Pillow, django-tailwind, and django-browser-reload, along with the compatible versions of their dependencies.

A dependency manifest should be added to this repository to make installation reproducible.

### 4. Apply migrations

```bash
python manage.py migrate
```

### 5. Create an administrator

```bash
python manage.py createsuperuser
```

### 6. Run the development server

```bash
python manage.py runserver
```

Open `http://127.0.0.1:8000/`.

**Note:** The committed migration/model inconsistencies should be resolved before treating this setup as verified.

## Learning Outcomes

- Defining Django models and fields.
- Implementing ForeignKey, OneToOneField, and ManyToManyField relationships.
- Using Django ORM queries.
- Creating views and URL configurations.
- Rendering database records through Django templates.
- Handling media files and image fields.
- Managing application data through Django Admin.
- Integrating Tailwind CSS into a Django project.

## Limitations

- No REST API.
- No shopping cart or checkout.
- Review and certificate workflows are not implemented.
- No automated application tests.
- Development configuration requires cleanup.

## Future Improvements

- Implement user reviews with rating validation.
- Add authentication and authorization.
- Add CRUD operations for chai varieties and stores.
- Build a REST API using Django REST Framework.
- Add automated tests.
- Improve responsive UI and filtering.
- Add reproducible dependency management.

## Project Status

Learning project demonstrating Django fundamentals and relational database modelling. Not a production-ready commerce application.
