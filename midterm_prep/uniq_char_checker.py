def has_all_uniq_chars(string_to_check):
    """Write a function that checks that all characters in a string are unique"""

    # for each character
    for idx in range(len(string_to_check)):
        # look at all subsequent chars for a match
        for subsequent_idx in range(idx + 1, len(string_to_check)):
            # print("Comparing idx", idx, "to idx",subsequent_idx)
            # if there's a
            if string_to_check[idx] == string_to_check[subsequent_idx]:
                # it's not unique
                print("idx", idx, "and idx",subsequent_idx, "are the same:", string_to_check[idx])
                return False

    # if we reach the end without a match
    # it is unique
    return True


# ANOTHER SOLUTION:
# def has_all_uniq_chars(string_to_check):
#     # keep track of chars seen
#     seen_chars = ""
#
#     # at each new char, check if we've seen it
#     for char in string_to_check:
#         if char in seen_chars:
#             print("Found a duplicate char:", char)
#             return False
#         seen_chars += char
#
#     return True


print(has_all_uniq_chars("paul bodily"))
print(has_all_uniq_chars("abcdefhijklmnopqrstuvwxyz"))
