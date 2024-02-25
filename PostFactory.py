from Post import Post


class PostFactory:
    def create_post(self, user, type_of_post, follower_set, *args):

        # Create text post
        if type_of_post == "Text":
            content = args[0]
            return Post(user, followers=follower_set, type_of_post=type_of_post, content=content)

        # Create image post
        elif type_of_post == "Image":
            image_path = args[0]
            return Post(user, followers=follower_set, type_of_post=type_of_post, image_path=image_path)

        # Create sale post
        elif type_of_post == "Sale":
            description = args[0]
            price = args[1]
            location = args[2]
            return Post(user, followers=follower_set, type_of_post=type_of_post, description=description,
                        price=price, location=location)
