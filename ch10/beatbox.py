# Write a program that solicits the form from the user.
form = input("Form: ")

song = []

# Then write a beat-box "song" (as a list of strings) from the
for x in form:
    # given form (i.e., accumulation list variable), where
    # 'A' = 4 repetitions of "boom tick-kah ticka ticka boom-kah"
    if x == 'A':
        song = song + ["boots and cats and"] * 2
    # 'B' = 2 repetitions of "boots and cats and"
    elif x == 'B':
        song = song + ["boom tick-kah ticka ticka boom-kah"] * 4


for line in song:
    print(line)
