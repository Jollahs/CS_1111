str_to_print = "Go Spot Go"

print("\n***ITERATION METHOD 1***\n")
for achar in str_to_print:
    print(achar)

print("\n***ITERATION METHOD 2***\n")
for idx in range(len(str_to_print)):
    print(str_to_print[idx])

print("\n***ITERATION METHOD 3***\n")
idx = 0
while idx < len(str_to_print):
    print(str_to_print[idx])
    idx = idx +1
