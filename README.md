
# Django REST API Project

This is a Django-based REST API project with multiple integrated apps and features like JWT authentication, Algolia search, and CORS support. I made this project to sum up my knowledge in Django Rest Framework. This project was made according to  youtube channel called "CodingEntrepreneurs".

## Features

- JWT Authentication using `rest_framework_simplejwt`
- Session and Token-based authentication
- Pagination enabled (LimitOffsetPagination)
- Algolia search integration
- Environment variable support using `python-dotenv`
- CORS support for local development
- Modular app structure: `api`, `products`, `search`

## Installed Apps

- Django Admin
- Django Auth
- Django ContentTypes, Sessions, Messages, Staticfiles
- Django REST Framework
- Algolia Django Integration
- CORS Headers
- Custom apps: `api`, `products`, `search`

## API Endpoints

- `/api/` – base API routes
- `/api/search/` – search-related endpoints
- `/api/products/` – product-related endpoints
- `/api/v2/` – routes handled by a custom router module

## Environment Variables

Use a `.env` file to store sensitive information:

```
SECRET_KEY=your_secret_key_here
APPLICATION_ID=your_algolia_app_id
API_KEY=your_algolia_api_key
```

## JWT Settings

- Access token lifetime: 30 minutes
- Refresh token lifetime: 30 minutes
- Authorization header type: `Bearer`

## CORS Settings

For development:

```
http://localhost:8111
https://localhost:8111
```

## Database

Default is SQLite for development. Change `DATABASES` in `settings.py` to configure PostgreSQL or other databases.

## Static Files

Static files are served from `/static/`.

---

## Running the Project

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```



