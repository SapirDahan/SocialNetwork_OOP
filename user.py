from post import post

class user:

    # Creating a user
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.log_in = True
        self.followSet = set()
        self.num_of_posts = 0
        self.information = f"{username} 's notifications:"
        self.return_user()

    def return_user(self):
        return self

    def log_user_in(self):
        self.log_in = True
        print(f"{self.username} connected")

    def log_user_out(self):
        self.log_in = False
        print(f"{self.username} disconnected")

    def follow(self, follow_user):
        if(not follow_user in self.followSet):
            self.followSet.add(follow_user)
            print(f"{self.username} started following {follow_user.username}")

    def unfollow(self, follow_user):
        if follow_user in self.followSet:
            self.followSet.discard(follow_user)
            print(f"{self.username} unfollowed {follow_user.username}")

    # Using the factory pattern to create posts
    def publish_post(self, type, *args):
        self.num_of_posts += 1
        if type == "Text":
            content = args[0]
            return post(self, type, content=content)

        elif type == "Image":
            image_path = args[0]
            return post(self, type, image_path=image_path)

        elif type == "Sale":
            description = args[0]
            price = args[1]
            location = args[2]
            return post(self, type, description=description, price=price, location=location)


    def update_notification(self, notification):
        self.information += f"\n{notification}"


    def __str__(self):
        return f"User name: {self.username}, Number of posts: {self.num_of_posts}, Number of followers: {len(self.followSet)}"

    def print_notifications(self):
        print(self.information)


