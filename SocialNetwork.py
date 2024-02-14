from User import User


class SocialNetwork:

    instance = None
    all_users = list()  # List of all the users

    # Create only once the instance. This is using the singleton pattern
    def __init__(self, name):

        # Creating the instance only if it had not created before
        if self.instance is None:
            self.name = name  # The name of the social network
            print(f"The social network {name} was created!")  # Declare the social network was created

    # Using the factory pattern to create users
    def sign_up(self, username, password):

        # If the username already exits don't create the object
        for users in self.all_users:
            if users.username == username:
                return

        # If the password is not in length between 4 and 8 don't create the object
        if len(password) < 4 or len(password) > 8:
            return

        # Create the new user
        new_user = User(username, password)

        # Add the user to the list
        self.all_users.append(new_user)

        # Return the user we created
        return new_user

    # log out the user
    def log_out(self, username):
        # Find the user
        for users in self.all_users:
            if users.username == username:
                users.log_user_out()  # Log the user out

    def log_in(self, username, password):
        # Find the user
        for users in self.all_users:
            if users.username == username and users.password == password:
                users.log_user_in()  # Log the user in

    # Create the string that represent the social network
    def __str__(self):
        string = f"{self.name} social network:"

        for users in self.all_users:

            # Add the information about users
            string += "\n" + str(users)

        return string
