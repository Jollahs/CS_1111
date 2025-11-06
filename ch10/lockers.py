locker_nums_list = []

# while True:
for i in range(2):
    name = input("Name? ")
    locker_combo_string = input("Provide 3 int combo for locker: ")
    locker_combo_strings_list = locker_combo_string.split()
    locker_combo = []
    for l in locker_combo_strings_list:
        locker_combo.append(int(l))

    locker_nums_list.append([name, locker_combo])

print(locker_nums_list)
