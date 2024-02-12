from user import user

class SocialNetwork:

    instance = None
    all_users = list()

    # Create only once the instance. This is using the singleton pattern
    def __init__(self, name):
        if self.instance is None:
            self.name = name
            print(f"The social network {name} was created!")
            self.return_instance()

    def return_instance(self):
        return self.instance


    @classmethod
    # Using the factory pattern to create users
    def sign_up(self, username, password):

        if username in self.all_users:
            return
        # If the username already exits don't create the object
        # for users in cls.__class__.all_users:
        #     if users.username == username:
        #         return

        # If the password is not in length between 4 and 8 don't create the object
        if len(password) < 4 or len(password) > 8:
            return

        new_user = user(username, password)

        # Add the user to the list
        self.all_users.append(new_user)
        return new_user


    def log_out(self, username):
        # Log the user out
        for users in self.all_users:
            if users.username == username:
                users.log_user_out()

    def log_in(self, username, password):
        for users in self.__class__.all_users:
            if users.username == username and users.password == password:
                users.log_user_in()


    def __str__(self):
        string = f"{self.name} social network:"
        for users in self.all_users:

            #Add the information about users
            string += "\n" + str(users)
        return string
