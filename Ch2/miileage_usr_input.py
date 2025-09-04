# Live Coding demonstration—Write a program with
# variables representing the miles driven on 3
# different days. Create
# a 4th variable that is updated to reflect the
# total count of all 3 variables. Print out all four variables.
# the 3 daily mileage variables are set by user input

day_1_miles = float(input("How many miles on day 1? "))
day_2_miles = float(input("How many miles on day 2? "))
day_3_miles = float(input("How many miles on day 3? "))
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
