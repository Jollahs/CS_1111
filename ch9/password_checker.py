import string

def contains_letter_from(s, candidate_letters):
    for letter in s:
        if letter in candidate_letters:
            return True
    return False

def password_is_strong(s):
    # length >= 12
    if len(s) < 12:
        return False

    # contains both capital and lowercase letters
    # contains a number
    if not contains_letter_from(s, string.ascii_lowercase):
        return False

    if not contains_letter_from(s, string.ascii_uppercase):
        return False

    if not contains_letter_from(s, string.digits):
        return False

    # contains at least one special character (i.e., chars with ascii value [33,47])
    if not contains_letter_from(s, "!@#$%^&*()"):
        return False

    # does not contain the substring "password"
    if "password" in s.lower():
        return False

    return True

# Develop a program that loops checks the strength of a user-entered password.
user_password = input("Password: ")

while not password_is_strong(user_password):
    print("That's terrible, try again...")
    user_password = input("Password: ")

print("STRONG PASSWORD")

# Output whether or not the password is strong. If it is not strong, output a message saying what needs to be improved.
# The program should loop until a strong password is entered.
