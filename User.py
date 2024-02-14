from Post import Post


class User:

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

    # Log the user out only if he logged in
    def log_user_out(self):
        if self.log_in:
            self.log_in = False
            print(f"{self.username} disconnected")

    # Follow another user
    def follow(self, follow_user):

        # If you do not follow him, and you don't try to follow yourself. Also, it is logged only if you logged in
        if self not in follow_user.followerSet and self is not follow_user and self.log_in:

            # Add yourself to the set of users following the user you want to follow
            follow_user.followerSet.add(self)

            # Print that you started to follow this user
            print(f"{self.username} started following {follow_user.username}")

    # Unfollow a user
    def unfollow(self, follow_user):

        # If you do follow him and you logged in
        if self in follow_user.followerSet and self.log_in:

            # Remove yourself from the set of users following this user
            follow_user.followerSet.discard(self)

            # Print that you unfollowed this user
            print(f"{self.username} unfollowed {follow_user.username}")

    # Using the factory pattern to create posts
    def publish_post(self, type_of_post, *args):

        # Only logged-in user can publish a post
        if not self.log_in:
            return

        # Increase the number of post this user created
        self.num_of_posts += 1

        if type_of_post == "Text":
            content = args[0]
            return Post(self, followers=self.followerSet, type_of_post=type_of_post, content=content)

        elif type_of_post == "Image":
            image_path = args[0]
            return Post(self, followers=self.followerSet, type_of_post=type_of_post, image_path=image_path)

        elif type_of_post == "Sale":
            description = args[0]
            price = args[1]
            location = args[2]
            return Post(self, followers=self.followerSet, type_of_post=type_of_post, description=description, price=price, location=location)

    """ 
    Using the observer pattern in order to update the user about things like:
    Someone he follows posted a new post, he got a likes from someone and if he got a comment
    """
    def update_notification(self, notification):

        # Add the notification to all the notifications
        self.information += f"\n{notification}"

    # Print the user notifications
    def print_notifications(self):
        print(self.information)

    # Create a string that represent the user
    def __str__(self):
        return f"User name: {self.username}, Number of posts: {self.num_of_posts}, Number of followers: {len(self.followerSet)}"




