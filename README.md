# Dockerize Django Environment

## Specification

* WSGI
  * gunicorn
* webserver
    * nginx
* database
    * postgres

## How to use

1. Build your docker environment

  ```sh
  docker-compose build
  ```

1. Create the Django project using the docker-compose command.

  ```sh
  docker-compose exec web django-admin.py startproject yourproject .
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

1. In `web/app/settings.py`, add the line at the bottom of it.

  ```python
   STATIC_ROOT = STATIC_ROOT = os.path.join(BASE_DIR, 'static')
  ```

1. Install Admin app. In `web/app/settings.py`, add line `django.contrib.admin`

  ```python
  INSTALLED_APPS = [
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

1. Go ahead, create your app!

  ```sh
  docker-compose exec web python manage.py startapp yourapp
  ```

1. Initilize your database

  ```sh
  docker-compose exec web python manage.py migrate
  ```

1. Enable `Model`

  - Define your model class in `yourapps/models.py`
  - Add line `yourapps.apps.YourappsConfig` in `web/app/settings.py` of `INSTALLED_APPS`

    ```python
      INSTALLED_APPS = [
        'yourapps.apps.YourappsConfig',
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
    ]
    ```
  - do migrations
    ```python
    docker exec web python manage.py makemigrations yourapps
    ```

1. Initilize Django admin

  ```sh
  docker-compose exec -it web python manage.py createsuperuser
  ```

1. Collecting staticfiles

  ```sh
  docker-compose run web python manage.py collectstatic --noinput
  ```
