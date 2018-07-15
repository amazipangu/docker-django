import os
import sys


class DjangoAdmin(object):
    def start_project(self, service_name, project_name):
        os.system(
            "docker-compose run {} django-admin.py startproject {} ."
            .format(self.service_name, self.project_name)
        )
