import sys, os
from util import Utility

class Pipenv(object):

    def lock(service_name):
        """
        Create Pipenv.lock
        """
        os.system("docker-compose exec {} pipenv lock".format(service_name))


def main():
    Pipenv.lock(Utility.input_service_name())

if __name__ == "__main__":
    main()