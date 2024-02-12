import matplotlib.pyplot as plt
import matplotlib.image as mpimg

class post():

    def __init__(self, user, type_of_post, content=None, image_path=None, description=None, price=None, location=None):

        self.observer = user
        self.username = user.username
        self.like_set = set()
        self.comments_list = list()
        self.information = ""

        if type_of_post == "Text":
            self.type = "Text"
            self.content = content
            self.information = f"{self.username} published a post:\n\"{content}\"\n"
            print(self.information)

        if type_of_post == "Image":
            self.type = "Image"
            self.image_path = image_path
            self.information = f"{self.username} posted a picture\n"
            print(self.information)

        if type_of_post == "Sale":
            self.type = "Sale"
            self.description = description
            self.price = price
            self.location = location
            self.is_sold = False
            self.information = f"{self.username} posted a product for sale:\nFor sale! {description}, price: {price}, pickup from: {location}\n"
            print(self.information)
        self.return_post()

    def return_post(self):
        return self

    def discount(self, price_reduction, password):
        if password == self.observer.password and self.type == "Sale":
            self.price = self.price * (1 - price_reduction / 100)
            self.information = f"{self.username} posted a product for sale:\nFor sale! {self.description}, price: {self.price}, pickup from: {self.location}"
            print(f"Discount on {self.username} product! the new price is: {self.price}")

    def like(self, other_user):
        if other_user not in self.like_set:
            self.like_set.add(other_user)
            message = f"{other_user.username} liked your post"
            if other_user != self.observer:
                self.notification(message)

    def comment(self, other_user, text):
        self.comments_list.append((other_user, text))
        message = f"{other_user.username} commented on your post"

        #notifiy only if not the owner of the post had commented
        if other_user != self.observer:
            self.notification(message)
            print(f": {text}")

    def notification(self, text):
        print(f"notification to {self.username}: {text}")
        self.observer.update_notification(text)

    def sold(self, password):
        if password == self.observer.password and self.type == "Sale":
            self.is_sold = True
            self.information = f"{self.username} posted a product for sale:\nSold! {self.description}, price: {self.price}, pickup from: {self.location}"
            print(f"{self.username}'s product is sold")

    def __str__(self):
        return self.information

    def display(self):
        # img = mpimg.imread(self.image_path)
        # plt.imshow(img)
        # plt.axis('off')
        # plt.show()
        print("dont forget to add a picture")
