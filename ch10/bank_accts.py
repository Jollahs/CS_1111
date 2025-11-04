# Pretend that everyone has single-digit bank account numbers

# Write a program that has a list of bank balances
# (for security make sure some bank account numbers are invalid)
balances = [None, 55.24, None, None, None, 351.90, None, 1900.00, None, 0.00]

while True:
    # Prompt the user for a bank account number
    acct_no = int(input("Please enter a bank account number: "))

    # Check if the number is valid (it isn’t None)
    if  (acct_no < 0) or (acct_no >= len(balances)) or (balances[acct_no] is None): # if it's invalid
        # print an error if it is invalid
        print("ERROR: the bank account number", acct_no, "is invalid")
    # Otherwise print the account number and account balance
    else:
        print("Account #" + str(acct_no) + " has balance $" + str(balances[acct_no]))
