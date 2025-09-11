# gas_station_input.py—Problem-Solving:
# “You are at the gas station filling up. You pump the gas.
# You observe the price per gallon. You also buy a slurpee.
# You pay with a single bill.” Copy and adapt your previous program
# to let the user input all of the values.

# SLURPEE PRICES
SMALL_SLURPEE_PRICE = 0.80
MEDIUM_SLURPEE_PRICE = 1.10
LARGE_SLURPEE_PRICE = 1.30
PRICE_PER_GALLON = 1.50

# solicit price per gallon from the user
# print(price_per_gallon)

# solicit number of gallons from the user
num_gallons = float(input("How many gallons did you use? "))
# print(num_gallons)

# solicit number of slurpees of each size
num_small_slurpees = int(input("How many small slurpees did you purchase? "))
num_medium_slurpees = int(input("How many medium slurpees did you purchase? "))
num_large_slurpees = int(input("How many large slurpees did you purchase? "))

# solicit bill denomination from user
bill_denomination = int(input("Which bill are you paying with (e.g., $1, $5, $20)? $"))

# print out total cost
small_slurpees_total_cost = num_small_slurpees * SMALL_SLURPEE_PRICE
medium_slurpees_total_cost = num_medium_slurpees * MEDIUM_SLURPEE_PRICE
large_slurpees_total_cost = num_large_slurpees * LARGE_SLURPEE_PRICE
gas_total_cost = num_gallons * PRICE_PER_GALLON

total_cost = small_slurpees_total_cost + medium_slurpees_total_cost + \
             large_slurpees_total_cost + gas_total_cost

print("Your total cost is $" + str(total_cost))

# print out change
change_due = bill_denomination - total_cost
print("Your change is $" + str(change_due))
