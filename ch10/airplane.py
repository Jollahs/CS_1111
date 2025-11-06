# [first_name, last_name, num_bags, [seat_row, seat_col]]

ROW_COUNT = 10
COL_COUNT = 4

passenger_list = [None] * ROW_COUNT * COL_COUNT
passenger_count = 0

while True:
    menu = ("Select from the following options: \n"
            "1. Add passenger\n"
            "2. Print all passengers\n"
            "3. Assign seat\n"
            "Input: ")
    choice = int(input(menu))

    if choice == 1:
        f_name = input("First name? ")
        l_name = input("Last name? ")
        num_bags = int(input("# bags? "))
        passenger_list[passenger_count] = [f_name,l_name,num_bags, None]
        passenger_count += 1
    elif choice == 2:
        print("Printing all passengers:")
        for i in range(len(passenger_list)):
            print(str(i+1) + ". " + str(passenger_list[i]))
    elif choice == 3:
        print("Seat assignment:")
        f_name_query = input("First name? ")
        l_name_query = input("Last name? ")
        for i in range(len(passenger_list)):
            passenger = passenger_list[i]
            if passenger != None and passenger[0] == f_name_query and passenger[1] == l_name_query:
                print("Passenger found")
                seat_row = int(input("Row? ")) - 1
                seat_col = int(input("Col? ")) -1
                passenger[3] = [seat_row, seat_col]
