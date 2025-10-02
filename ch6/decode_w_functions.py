def get_nonnegative_integer(prompt):
    # Converts the user's input into an int type
    user_input = int(input(prompt))

    # Uses an assert statement to ensure the integer is non-negative (how can we do this only using the '==' operator?)
    assert user_input == abs(user_input), "Input is not non-negative"

    return user_input


# Solicit the user for an integer for the number 𝑛 of characters to decode
num_chars = get_nonnegative_integer("How many characters? ")

# initialize the accumulation variable
full_code = ""

# For 𝑛 non-negative integer codes,
for i in range(num_chars):
    # Solicit the user for an integer for the next code
    next_code = get_nonnegative_integer("Next code? ")

    # Decode each character using the chr() function to convert from an integer to its ASCII equivalent
    decoded_char = chr(next_code)

    # print(chr(next_code))
    # Concatenates the characters into a single string
    full_code = full_code + decoded_char

# Prints out the user's decoded message (accumulation variable)
print(full_code)
