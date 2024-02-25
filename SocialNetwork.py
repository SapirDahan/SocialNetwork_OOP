from UserFactory import UserFactory

class SocialNetwork:

    __instance = None
    __all_users = list()  # List of all the users

    # Create only once the instance. This is using the singleton pattern
    def __new__(cls, name):

        # Make sure that the instance is None
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)  # Create the instance
            cls.__instance.name = name  # The name of the social network
            print(f"The social network {name} was created!")  # Declare the social network was created
        return cls.__instance  # Return the instance

    # Using the factory pattern to create users
    def sign_up(self, username, password):

        # Create the factory
        factory = UserFactory()

        # Create and return a new user
        return factory.create_user(username, password, self.__all_users)

    # Log out the user
    def log_out(self, username):
        # Find the user
        for users in self.__all_users:
            if users.username == username:
                users.log_user_out()  # Log the user out

    # Log the user in
    def log_in(self, username, password):
        # Find the user
        for users in self.__all_users:
            if users.username == username and users.password == password:
                users.log_user_in()  # Log the user in

    # Create the string that represent the social network
    def __str__(self):
        string = f"{self.name} social network:"

        for users in self.__all_users:

            # Add the information about users
            string += "\n" + str(users)

        return string + "\n"
