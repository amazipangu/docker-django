# Dockerize Django Environment

## Specification

* WSGI
  * [Gunicorn](https://gunicorn.org/)
* HTTP server
    * [nginx](https://nginx.org/en/)
* Database
    * [PostgreSQL](https://www.postgresql.org/)

## How to use

1. Build your Docker environment

  ```sh
  docker-compose build
  ```

2. Create the Django project using the docker-compose command.

  ```sh
  docker-compose run web django-admin.py startproject yourproject .
  ```

3. In your project directory, edit the yourproject/settings.py file.

  ```python
  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.postgresql',
          'NAME': 'your_db_name',
          'USER': 'your_db_user',
          'PASSWORD': 'your_db_password',
          'HOST': 'db',
          'PORT': 5432,
      }
  }
  ```

4. In `web/yourproject/settings.py`, add the line at the bottom of it.

  ```python
   STATIC_ROOT = STATIC_ROOT = os.path.join(BASE_DIR, 'static')
  ```

5. Install Admin app. In `web/yourproject/settings.py`, add line `django.contrib.admin`

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

6. Run the `docker-compose up` command again

  ```sh
  sh bin/container_start.sh
  ```

7. Go ahead, create your app!

  ```sh
  docker-compose exec web python manage.py startapp yourapp
  ```

8. Initilize your database

  ```sh
  docker-compose exec web python manage.py migrate
  ```

9. Enable `Model`

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

10. Initilize Django admin

  ```sh
  docker-compose exec -it web python manage.py createsuperuser
  ```

11. Collecting staticfiles

  ```sh
  docker-compose run web python manage.py collectstatic --noinput
  ```
