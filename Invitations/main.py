import random
if __name__ == "__main__":
    # Version 1:
    invitations = ["ali", "ahmad", "mahdi"]
    print("***Welcome to invite to our dinner!***")
    for x in invitations:
        print(f"*Hello {x.title()}, you're invited to our dinner*")
    print("----------------------------------------------------------------------")
    # Version 2:
    invitations = ["ali", "ahmad", "mahdi"]
    print("***Welcome to invite to our dinner!***")
    for x in invitations:
        print(f"*Hello {x.title()}, you're invited to our dinner*")

    rand = random.choice(invitations)
    print(f"Hi, I'm {rand.title()}, Sorry I can't make the dinner.")
    for i in range(len(invitations)):
        if invitations[i] == rand:
            invitations[i] = "mohammad"
            break
    print(f"Invitations: {invitations}")