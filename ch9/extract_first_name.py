# Write a program that prompts the user for their full name
# (e.g., "John Jacob Jingleheimer")
full_name = input("Full name please: ")

full_name = full_name.strip()

# Then, using white space, isolate the first name and issue a greeting: "Nice to meet you, John!"
print(full_name)

# start at the leftmost index and find the first whitespace character
idx_of_1st_ws = full_name.find(" ")
print("idx of first space is", idx_of_1st_ws)

# Your program should not fail if the user has extra space at the beginning

if idx_of_1st_ws == -1:
    # They only put in one word
    first_name = full_name
else:
    first_name = full_name[:idx_of_1st_ws]

print("Hello,", first_name)

