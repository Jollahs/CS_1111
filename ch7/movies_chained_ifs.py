# Write a program to prompt a user for their age.
user_age = float(input("Enter your age: "))

# Then print out what kind of license they can apply for.
# These are the minimum ages for the following types of licenses:
assert user_age >= 0, "User entered negative value for age"

print("Cost of a ticket for a person age ", user_age, "is")

if user_age <= 3:
    print("FREE DOLLARS")
elif user_age <= 12:
    print("$8.00")
elif user_age >= 60:
    print("$7.50 (senior discount)")
else:
    print("$10.00")
