biggest_num_so_far = None

list_of_nums = [1,2,3,4,5]

for num in list_of_nums:
    if biggest_num_so_far is None or num > biggest_num_so_far:
        biggest_num_so_far = num

print("max is: ", biggest_num_so_far)

print("max is: ", max(list_of_nums))


string = "1 2 3 4 5"

print(string.split())

nums = string.split()

for i in nums:
    print(i)

