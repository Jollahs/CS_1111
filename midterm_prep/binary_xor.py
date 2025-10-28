def xor(x, y):
    """Write a function to compute the XOR of two binary strings"""
    assert len(x) == len(y), "Inputs are not the same length"

    xor_string = ""

    for idx in range(len(x)):
        character = x[idx]
        character2 = y[idx]
        if character == character2:
            xor_string = xor_string + "0"
        else:
            # Otherwise, concatenate a 1
            xor_string = xor_string + "1"

    return xor_string

string_1 = "101110"
string_2 = "100101"

print("The XOR of", string_1, "and", string_2, "is",xor(string_1,string_2))
