food_costs = {
    "apple": 0.99,
    "banana": 0.59,
    "bread": 2.49,
    "milk": 3.19,
    "eggs": 2.79,
    "cheese": 4.49,
    "chicken": 8.99,
    "rice": 1.29,
    "pasta": 1.09,
    "chocolate": 0.99,
    "strawberries": 0.45
}

def print_grocery_list(my_dict):
    for k,v in my_dict.items():
        print(v,k)

item_quantities = {}

# Write a program that loops,
while True:
    print("Current grocery list: ")
    print_grocery_list(item_quantities)

    # allowing the user to select one of three options:
    print("Please select from the following options: ")
    for index, option in enumerate(["Input item", "Remove item", "Check out"]):
        print(str(index) + ". " + option)
    user_choice = int(input("Selection: "))

    # Input item
    if user_choice == 0:
        item = input("Item to add: ")
        # check if item is in the dict
        if item in item_quantities:
            # if it's already in the dictionary, increment (add one) to the current quantity
            old_value = item_quantities[item]
            item_quantities[item] = old_value + 1
            # item_quantities[item] += 1
            # item_quantities[item] = item_quantities[item] + 1
        else:
            # if not, add it with a value of 1
            item_quantities[item] = 1
    # Remove item
    elif user_choice == 1:
        item = input("Item to remove: ")
        if item in item_quantities:
            old_value = item_quantities[item]
            if old_value == 1:
                del item_quantities[item]
            else:
                item_quantities[item] = old_value - 1
        else:
            print(item, "not found")
    # Check out
    elif user_choice == 2:
        break

# Use a dictionary to keep track of scanned items and their quantities

# Use a separate dictionary (as seen on the right) to keep track of the prices of items
# When the user selects checkout,
# print out a receipt with all items,
# their quantities, and the total cost
total_cost = 0.0
for food, quantity in item_quantities.items():
    food_cost = quantity * food_costs[food]
    print(quantity,food,"\t$",food_cost)
    total_cost += food_cost

print("TOTAL COST\t\t$",total_cost)
