# Dockerize Django Environment

## Specification

* WSGI
  * gunicorn
* webserver
    * nginx
* database
    * postgres

## How to use

1. Create the Django project using the docker-compose command.
```sh
docker-compose run web django-admin.py startproject composeexample .
```

1. In your project directory, edit the composeexample/settings.py file.
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}
```

1. In `web/app/settings.py`, add the line `STATIC_ROOT = STATIC_ROOT = os.path.join(BASE_DIR, 'static')`

1. Install Admin app.
  - In `web/app/settings.py`, add line `django.contrib.admin`

  ```python
  INSTALLED_APPS = [
      'users.apps.UsersConfig',
      'django.contrib.admin',
      'django.contrib.auth',
      'django.contrib.contenttypes',
      'django.contrib.sessions',
      'django.contrib.messages',
      'django.contrib.staticfiles',
  ]
  ```

1. Run the `docker-compose up` command again

```sh
docker-compose up
```
1. Initilize your database

```sh
docker-compose run web python manage.py migrate
```

1. Collecting staticfiles

```sh
docker-compose run web python manage.py collectstatic --noinput
```
