import os


class DjangoAdmin(object):

    def start_project(service_name, project_name):
        os.system(
            "docker-compose run {} django-admin.py startproject {} ."
            .format(service_name, project_name)
        )
