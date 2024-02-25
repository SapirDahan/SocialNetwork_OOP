from User import User


class UserFactory:
    def create_user(self, username, password, all_users):

        # If the username already exits don't create the object
        for users in all_users:
            if users.username == username:
                raise ValueError("Username is already taken")

        # If the password is not in length between 4 and 8 don't create the object
        if len(password) < 4 or len(password) > 8:
            raise ValueError("Password must be at least 4 characters long and at most 8 characters long")

        # Create the new user
        new_user = User(username, password)

        # Add the user to the list
        all_users.append(new_user)

        return new_user

