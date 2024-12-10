# Cars API

A Django REST Framework application for managing cars and their manufacturers.

## Features
- Car management
- Manufacturer (Firm) management
- RESTful API
- Swagger documentation

## Setup



1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate virtual environment:
```bash
# Windows
venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create superuser:
```bash
python manage.py createsuperuser
```

6. Run the server:
```bash
python manage.py runserver
```

## API Documentation
- Swagger UI: http://localhost:8000/swagger/

- ReDoc: http://localhost:8000/redoc/
