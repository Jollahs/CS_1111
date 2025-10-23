import string


def count(text, aChar):
    lettercount = 0
    for c in text:
        if c == aChar:
            lettercount = lettercount + 1
    return lettercount

# Write a program that takes an input string from the user,
usr_input = input("Please enter a string: ")

# converts the string to lower case, and
usr_input = usr_input.lower()
print(usr_input)

# uses the function above to report a histogram (i.e., letter count)
# for each of the letters a to z
for letter in string.ascii_lowercase + string.ascii_uppercase:
    print(letter,":", count(usr_input, letter))
