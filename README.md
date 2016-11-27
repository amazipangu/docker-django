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

1. Run the `docker-compose up` command
```sh
docker-compose up
```

## I wanna improve...
it can't contain static file as js, css, image.
