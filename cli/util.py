class Utility:

    def input_service_name():
        """
        Input service name whitch defined on docker-compose.yml.
        """
        print("Type your service name which executed Django below.")
        service_name = input()
        print(
            "Your service name which has run Django: {}".format(service_name)
        )
        return service_name

    def input_project_name():
        """
        Input Django project name
        """
        print("Type your Django project name below.")
        project_name = input()
        print(
            "your project name: {}".format(project_name)
        )
        return project_name
