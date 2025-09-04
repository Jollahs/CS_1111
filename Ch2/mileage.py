# Live Coding demonstration—Write a program with
# variables representing the miles driven on 3
# different days (you choose the miles). Create
# a 4th variable that is updated to reflect the
# total count of all 3 variables. Print out all four variables.

day_1_miles = 25.1
day_2_miles = 35.0
day_3_miles = 100.0
total_miles_so_far = 0.0

print("On day 1, you drove", day_1_miles, "miles")
total_miles_so_far = total_miles_so_far + day_1_miles

print("You have driven", total_miles_so_far, "miles so far")

print()

print("On day 2, you drove", day_2_miles, "miles")
total_miles_so_far = total_miles_so_far + day_2_miles

print("You have driven", total_miles_so_far, "miles so far")

print()

print("On day 3, you drove", day_3_miles, "miles")
total_miles_so_far = total_miles_so_far + day_3_miles

print("You have driven", total_miles_so_far, "miles so far")
