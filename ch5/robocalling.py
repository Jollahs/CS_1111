#  NXX-XXXX is the seven-digit subscriber number.
#  The place holder N stands for the digits 2-9, as the subscriber
#  number may not begin with the digits 0 and 1.

#  Robocaller! Write a program to generate 10 random Idaho phone numbers to call.
import random

phone_number = ""

# Step 1: add area code
phone_number = phone_number + "(208) "

# Step 2: add N (2-9)
N = random.randint(2, 9)
# N = random.randrange(2, 10)
phone_number = phone_number + str(N)

# Step 3: add X's
for i in range(2):
    X = random.randint(0, 9)
    phone_number = phone_number + str(X)

phone_number = phone_number + "-"

# tack on the last four X'
for i in range(4):
    X = random.randint(0, 9)
    phone_number = phone_number + str(X)

print(phone_number)
