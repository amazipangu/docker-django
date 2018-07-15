import sys
from django_admin import DjangoAdmin
from util import Utility


def main():
    _create(Utility.input_service_name(), Utility.input_project_name())


# Private Method
def _create(service_name, project_name):
    print("Confirm your Django project name.")
    print("Is your Django Project name {}?".format(project_name))
    print("Type yes or no...")
    if input() == "yes" or "y":
        print("Now, create your Django project!!")
        DjangoAdmin.start_project(service_name, project_name)
    else:
        print("""
            Try to create your Django project.
            Excute this script again.
        """)
        sys.exit(1)


if __name__ == "__main__":
    main()
