#!/bin/bash
docker-compose run web django-admin.py startproject $1 .
docker-compose rm -s