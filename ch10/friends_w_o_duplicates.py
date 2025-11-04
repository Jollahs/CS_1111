# Write a program that solicits a list of friends from the user.

friend_list = []
friend_name = input("Input your friend's name: ")

# As long as the user enters a non-empty string, we keep prompting
while len(friend_name) > 0:
    # Save the name in a list with a good variable name ONLY if the name is new
    if friend_name not in friend_list:
        friend_list.append(friend_name)
        print("Friend added")
    else:
        print("Friend already in list (not added)")
    friend_name = input("Input your friend's name: ")


# Print the list and then print the length of the list.
print("You have", len(friend_list), "friends:", friend_list)
