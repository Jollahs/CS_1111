import os

contact_file_path = "contacts.csv"

contacts = {}

# read in contacts file
if os.path.exists(contact_file_path):
    infile = open(contact_file_path, "r")

    for line in infile:
        items = line.strip().split(",")
        name = items[0]
        phone = items[1]
        contacts[name] = phone

while True:
    for k,v in contacts.items():
        print(k, "p:", v)

    name = input("Enter contact to add (or QUIT): ")
    if name == "QUIT":
        break
    phone = input("Enter phone number for contact: ")
    contacts[name] = phone

# write contacts to file
outfile = open(contact_file_path, "w")

print_new_line = False
for name, phone in contacts.items():
    if print_new_line:
        outfile.write("\n")
    else:
        print_new_line = True
    outfile.write(name + "," + phone)
outfile.close()
