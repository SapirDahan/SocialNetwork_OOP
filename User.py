from Observer import Observer
from PostFactory import PostFactory


class User(Observer):

    # Creating a user
    def __init__(self, username, password):
        self.username = username  # The username
        self.password = password  # The password
        self.log_in = True  # When signing up set that the user is log in
        self.followerSet = set()  # All the users that following this user
        self.num_of_posts = 0  # The number of post that this user had post
        self.information = f"{username}'s notifications:"  # All the notifications that the user got

    # Log the user in only if he logged out
    def log_user_in(self):
        if not self.log_in:
            self.log_in = True
            print(f"{self.username} connected")
        else:
            raise ValueError("User is not logged in")

    # Log the user out only if he logged in
    def log_user_out(self):
        if self.log_in:
            self.log_in = False
            print(f"{self.username} disconnected")
        else:
            raise ValueError("User is not logged in")

    # Follow another user
    def follow(self, follow_user):

        # If you do not follow him. Also, it is legal only if you logged in
        if self not in follow_user.followerSet and self.log_in:

            # Add yourself to the set of users following the user you want to follow
            follow_user.followerSet.add(self)

            # Print that you started to follow this user
            print(f"{self.username} started following {follow_user.username}")

        elif self in follow_user.followerSet:
            print(f"{self.username} is already following {follow_user.username}")

        elif not self.log_in:
            raise ValueError("User is not logged in")

    # Unfollow a user
    def unfollow(self, follow_user):

        # If you do follow him and you logged in
        if self in follow_user.followerSet and self.log_in:

            # Remove yourself from the set of users following this user
            follow_user.followerSet.discard(self)

            # Print that you unfollowed this user
            print(f"{self.username} unfollowed {follow_user.username}")

        elif self not in follow_user.followerSet:
            raise ValueError("User is not following this user")

        elif not self.log_in:
            raise ValueError("User is not logged in")

    # Using the factory pattern to create posts
    def publish_post(self, type_of_post, *args):

        # Only logged-in user can publish a post
        if not self.log_in:
            raise ValueError("User is not logged in")

        # Increase the number of post this user created
        self.num_of_posts += 1

        factory = PostFactory()

        return factory.create_post(self, type_of_post, self.followerSet, *args)


    """ 
    Using the observer pattern in order to update the user about things like:
    Someone he follows posted a new post, he got a likes from someone and if he got a comment
    """
    def update(self, notification):

        # Add the notification to all the notifications
        self.information += f"\n{notification}"

    # Print the user notifications
    def print_notifications(self):
        print(self.information)

    # Create a string that represent the user
    def __str__(self):
        return f"User name: {self.username}, Number of posts: {self.num_of_posts}, Number of followers: {len(self.followerSet)}"




