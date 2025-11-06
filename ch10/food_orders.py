food_orders = [[1,9],[10],[2,2],None, None]

order_1 = food_orders[1]
print("Customer 1 ordered", order_1)

for customer_number in range(len(food_orders)):
	print(food_orders[customer_number])

food_orders[3] = [6,1,4,8,3]
food_orders[3][4] = 8
print(food_orders[3][0])
