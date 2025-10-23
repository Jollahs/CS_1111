# msg: attack at dawn
# shift: 2
import string


def encode_msg(msg, shift):
    encoded_msg = ""

    # for each letter
    for char in msg:
        if char not in string.ascii_uppercase:
            encoded_msg = encoded_msg + char
        else:
            # "add" 2 to the letter
            # METHOD 1
            char_idx = string.ascii_uppercase.find(char)  # find index of the character
            encoded_char_idx = char_idx + shift # add two
            encoded_char = string.ascii_uppercase[encoded_char_idx % 26] # get the character at the new index

            # and add it to the encoded message
            encoded_msg = encoded_msg + encoded_char

    return encoded_msg

print(encode_msg("ATTACK AT DAWN, PLZ", 2))
print(encode_msg("CVVCEM CV FCYP, RNB", -2))
