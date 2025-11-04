# Write a program that solicits a list of friends from the user.

friend_list = []
friend_name = input("Input your friend's name: ")

# As long as the user enters a non-empty string, we keep prompting
while len(friend_name) > 0:
    # Save the list in a variable with a good variable name.
    friend_list.append(friend_name)
    friend_name = input("Input your friend's name: ")

# Print the list and then print the length of the list.
print("You have", len(friend_list), "friends:", friend_list)
