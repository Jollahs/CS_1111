# Write a program to prompt a user for their age.
user_age = float(input("Enter your age: "))

# Then print out what kind of license they can apply for.
# These are the minimum ages for the following types of licenses:

print("At at", user_age, "you can apply for:")

assert user_age >= 0, "User entered negative value for age"

if user_age >= 18:
    print("Unrestricted Driver’s License")
else:
    if user_age >= 15:
        print("Underage Driver's License")
    else:
        if user_age >= 14.5:
            print("Supervised Instruction Permit")
        else:
            print("NO LICENSE")
