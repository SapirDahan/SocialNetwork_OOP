from SocialNetwork import SocialNetwork


def main():
    # Creating the network
    network = SocialNetwork("Twitter")
    print()

    # Creating users
    u1 = network.sign_up("Alice", "pass1")
    u2 = network.sign_up("Bob", "pass2")
    u3 = network.sign_up("Charlie", "pass3")
    u4 = network.sign_up("David", "pass4")
    u5 = network.sign_up("Eve", "pass5")

    # Creating followers
    u1.follow(u2)
    u1.follow(u5)
    u2.follow(u5)
    u2.follow(u1)
    u3.follow(u1)
    u3.follow(u2)
    u4.follow(u3)
    u4.follow(u1)
    u5.follow(u2)
    u5.follow(u4)
    print()

    # Creating text post
    p1 = u1.publish_post("Text", "In 1492, Christopher Columbus set sail,\n"
                                 "hoping to find a westward route to Asia, but instead,\n"
                                 "he discovered the Americas, changing the course of history forever.")
    # Creating image post
    p2 = u4.publish_post("Image", 'image1.jpg')

    # Creating sale post
    p3 = u3.publish_post("Sale", "Toyota prius 2012", 42000, "Haifa")

    # Creating likes and comments
    p2.like(u4)
    p1.like(u4)
    p1.like(u2)
    p1.comment(u3, "Columbus's bold journey!")
    p2.comment(u1, "So beautiful!")
    p2.like(u1)
    p2.like(u2)
    p2.like(u5)
    p1.comment(u5, "A pivotal moment")
    p3.comment(u2, "Exorbitant price")
    print()

    # Price reduction of the product for sale
    p3.discount(10, "pass3")
    print()

    # more likes and comments
    p3.like(u2)
    p3.comment(u2, "Can you give me your phone number?")
    p3.comment(u4, "+97255576433")
    print()

    # Defining the product as sold
    p3.sold("pass3")
    print()

    print(p3)

    # Displaying the image of the post
    p2.display()
    print()

    p2.comment(u5, "Amazing picture!")
    print()

    # Using unfollow
    u2.unfollow(u1)
    u3.unfollow(u2)
    print()

    # Using log_in & log_out
    network.log_out("Charlie")
    network.log_in("Charlie", "pass3")
    print()

    # User printing
    print(u1)
    print()

    # Post printing
    print(p1)
    print(p2)

    # Printing all notifications received by a certain user
    u4.print_notifications()
    print()

    # Network printing
    print(network, end='')


if __name__ == '__main__':
    main()