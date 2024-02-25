import matplotlib.pyplot as plt
import matplotlib.image as mpimg


class Post:

    # Create a post
    def __init__(self, user, followers, type_of_post, content=None, image_path=None, description=None, price=None, location=None):

        self.user = user  # The user who created the post
        self.username = user.username  # The user username
        self.followers = followers  # Users how follow the user that publish the post
        self.like_set = set()  # Set of users the liked the post
        self.comments_list = list()  # List of users who commented on the post
        self.information = ""  # Information about the post

        if type_of_post == "Text":
            self.type = type_of_post  # The type of the post
            self.content = content  # The content of the post
            self.information = f"{self.username} published a post:\n\"{content}\"\n"

        if type_of_post == "Image":
            self.type = type_of_post  # The type of the post
            self.image_path = image_path  # The path to the image
            self.information = f"{self.username} posted a picture\n"

        if type_of_post == "Sale":
            self.type = type_of_post  # The type of the post
            self.description = description  # The description about the product
            self.price = price  # The price of the product
            self.location = location  # The location to pick from
            self.is_sold = False  # Is the product sold
            self.information = f"{self.username} posted a product for sale:\nFor sale! {description}, price: {price}, pickup from: {location}\n"

        # Print the information
        print(self.information)

        # Update the followers that a new post was published. This is using the observer pattern
        self.notify_followers()

    # Make a discount on the product
    def discount(self, price_reduction, password):

        # Make sure it is legal to make a discount
        if password == self.user.password and self.type == "Sale" and self.user.log_in:
            self.price = self.price * (1 - price_reduction / 100)  # The new price
            self.information = f"{self.username} posted a product for sale:\nFor sale! {self.description}, price: {self.price}, pickup from: {self.location}"
            print(f"Discount on {self.username} product! the new price is: {self.price}")

        elif password != self.user.password:
            raise ValueError("Invalid password")

        elif self.type != "Sale":
            raise ValueError("Invalid operation")

        elif not self.user.log_in:
            raise ValueError("User is not logged in")

    # Like the post
    def like(self, other_user):

        # Make sure it is legal to do a like
        if other_user not in self.like_set and self.user.log_in:
            self.like_set.add(other_user)  # Add the user to the set
            message = f"{other_user.username} liked your post"

            # Notify the owner of the post that someone liked his post
            if other_user is not self.user:
                self.notification(message)
                print(f"notification to {self.username}: {message}")

        elif other_user in self.like_set:
            raise ValueError("User already liked this post")

        elif not self.user.log_in:
            raise ValueError("User is not logged in")

    # Comment a post
    def comment(self, other_user, text):

        # Make sure it is legal to comment
        if self.user.log_in:

            # Add the comment to the list of comments
            self.comments_list.append((other_user, text))

            message = f"{other_user.username} commented on your post"

            # Notify only if not the owner of the post had commented
            if other_user is not self.user:
                self.notification(message)
                print(f"notification to {self.username}: {message}: {text}")

        else:
            raise ValueError("User is not logged in")

    # Notify the owner of the post. This is using the observer pattern
    def notification(self, text):
        self.user.update(text)

    # Notify the followers of the owner of the post that the owner posted a new post. This is using the observer pattern
    def notify_followers(self):
        for follower in self.followers:
            follower.update(f"{self.username} has a new post")

    # Change this product to sold
    def sold(self, password):

        # Make sure it is legal to sell the product
        if password == self.user.password and self.type == "Sale" and self.user.log_in:
            self.is_sold = True  # Change status
            self.information = f"{self.username} posted a product for sale:\nSold! {self.description}, price: {self.price}, pickup from: {self.location}\n"
            print(f"{self.username}'s product is sold")

        elif password != self.user.password:
            raise ValueError("Invalid password")

        elif not self.type != "Sale":
            raise ValueError("Invalid operation")

        elif not self.user.log_in:
            raise ValueError("User is not logged in")

    # Make a string that represent the post
    def __str__(self):
        return self.information

    # Display the image only if the post is Image
    def display(self):
        if self.type == "Image":
            img = mpimg.imread(self.image_path)
            plt.imshow(img)
            plt.axis('off')
            plt.show()
            print("Shows picture")

        elif self.type != "Image":
            raise ValueError("Invalid operation")
