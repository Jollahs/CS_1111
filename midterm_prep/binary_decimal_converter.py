
def binary_to_decimal(binary_string):
    """write a function to convert a binary string to a decimal value"""

    decimal_string = ""
    total = 0

    # From right to left
    for idx in range(len(binary_string)):
        character_at_idx = binary_string[len(binary_string) - (idx+1)]
        assert character_at_idx == "0" or character_at_idx == "1"

        # add the bit value times 2^index power
        total = total + 2**idx * int(character_at_idx)

    return str(total)


b_string = "10000"
d_string = binary_to_decimal(b_string)

print(b_string,"in decimal is",d_string)
