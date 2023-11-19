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
    print("----------------------------------------------------------------------")
    # Version 3: (more guests)
    invitations = ["ali", "ahmad", "mahdi"]
    print("***Welcome to invite to our dinner!***")
    for x in invitations:
        print(f"*Hello {x.title()}, you're invited to our dinner*")

    moreGuests = ["mohammad", "amir", "parsa"]
    for x in moreGuests:
        print(f"Attention! {x.title()} informed that he wants to be invited to dinner.")

    for i in range(len(moreGuests)):
        if i == 0:
            invitations.insert(0, moreGuests[i])
        elif i == 1:
            invitations.insert(1, moreGuests[i])
            # invitations.insert(2, moreGuests[i])
        else:
            invitations.append(moreGuests[i])

    for x in invitations:
        print(f"*Hello {x.title()}, you're invited to our dinner*")

    print("----------------------------------------------------------------------")
    # Version 4: (special guests)
    print("***Welcome to invite to our dinner!***")
    print(invitations)
    print(f"Sorry everyone, I can invite only two people {invitations[1].title()} and {invitations[3].title()} "
          f"for dinner")
    s1 = invitations[1]
    s2 = invitations[3]
    for i in range(len(invitations)):
        p = invitations.pop(0)
        if p == s1 or p == s2:
            print(f"*Welcome {p.title()}, you’re still invited to dinner*")
        else:
            print(f"I'm sorry {p.title()} that I can’t invite you to dinner!")

    # print(f"invitations = {invitations}")
    # for x in invitations:
    #     del x
    #
    # print(invitations)
