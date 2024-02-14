from post import post

class user:

    # Creating a user
    def __init__(self, username, password):
        self.username = username  # The username
        self.password = password  # The password
        self.log_in = True  # When signing up set that the user is log in
        self.followerSet = set()  # All the users that following this user
        self.num_of_posts = 0  # The number of post that this user had post
        self.information = f"{username}'s notifications:"  # All the notifications that the user got

    # Log the user in only if he
    def log_user_in(self):
        if not self.log_in:
            self.log_in = True
            print(f"{self.username} connected")

    def log_user_out(self):
        if self.log_in:
            self.log_in = False
            print(f"{self.username} disconnected")

    def follow(self, follow_user):
        if self not in follow_user.followerSet and self is not follow_user and self.log_in:
            follow_user.followerSet.add(self)
            print(f"{self.username} started following {follow_user.username}")

    def unfollow(self, follow_user):
        if self in follow_user.followerSet and self.log_in:
            follow_user.followerSet.discard(self)
            print(f"{self.username} unfollowed {follow_user.username}")

    # Using the factory pattern to create posts
    def publish_post(self, type, *args):

        if not self.log_in:
            return

        self.num_of_posts += 1

        if type == "Text":
            content = args[0]
            return post(self, followers=self.followerSet, type_of_post=type, content=content)

        elif type == "Image":
            image_path = args[0]
            return post(self, followers=self.followerSet, type_of_post=type, image_path=image_path)

        elif type == "Sale":
            description = args[0]
            price = args[1]
            location = args[2]
            return post(self, followers=self.followerSet, type_of_post=type, description=description, price=price, location=location)


    def update_notification(self, notification):
        self.information += f"\n{notification}"


    def __str__(self):
        return f"User name: {self.username}, Number of posts: {self.num_of_posts}, Number of followers: {len(self.followerSet)}"

    def print_notifications(self):
        print(self.information)


