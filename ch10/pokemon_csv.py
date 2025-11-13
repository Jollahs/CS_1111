lines = [
    "Pikachu,35,55,40",
    "Charmander,39,52,43",
    "Bulbasaur,45,49,49"
]

table = []
for line in lines:
    parts = line.split(",")
    row = [parts[0], int(parts[1]), int(parts[2]), int(parts[3])]
    table.append(row)

print(table)

for row in table:
    print("\t".join([str(x) for x in row]))

