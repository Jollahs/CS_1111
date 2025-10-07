# drivers_license.py—Write a program that creates variables
# for 1) your name, 2) your state and 3) your driver’s license number
# (if you don’t have one, put None).

def print_if_not_none(var_to_check, label):
    if var_to_check != None:
        print(label, var_to_check)

name = "Paul"
state = "Idaho"
license_number = "ABCDEFG"

# Then print each variable, checking first to see if it is None.
# if name != None:
#     print("Name:", name)
print_if_not_none(name, "Name:")
print_if_not_none(state, "State:")
print_if_not_none(license_number, "License:")

# Assign these variables directly rather than using the input(…) function.
