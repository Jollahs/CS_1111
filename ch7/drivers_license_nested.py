# Write a program to prompt a user for their age.
user_age = float(input("Enter your age: "))

# Then print out what kind of license they can apply for.
# These are the minimum ages for the following types of licenses:

print("At at", user_age, "you can apply for:")

assert user_age >= 0, "User entered negative value for age"

if user_age < 14.5:
# 0 — No license
    print("NO LICENSE")
else: # user_age is >= 14.5
    if user_age < 15:
        # 14.5 — Supervised Instruction Permit
        print("Supervised Instruction Permit")
    else: # user_age is >= 15
        if user_age < 18:
            # 15 — Underage Driver’s License
            print("Underage Driver's License")
        else: # user_age is >= 18
            # 18 — Unrestricted Driver’s License
            print("Unrestricted Driver’s License")
