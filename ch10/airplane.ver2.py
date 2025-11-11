# [[first_name, last_name], num_bags, [seat_row, seat_col]]

def create_new_passenger():
    f_name = input("First name? ")
    l_name = input("Last name? ")
    num_bags = int(input("# bags? "))
    return [[f_name,l_name],num_bags, None]


def get_passenger_idx(name, _passenger_list):
    for i in range(len(_passenger_list)):
        passenger = _passenger_list[i]
        if passenger != None and passenger[0][0] == name[0] and passenger[0][1] == name[1]:
            return i

    return -1


def get_passenger_name():
    f_name_query = input("First name? ")
    l_name_query = input("Last name? ")
    return [f_name_query, l_name_query]


def get_seat():
    seat = [None, None]
    seat_row = int(input("Row? ")) - 1
    seat_col = int(input("Col? ")) - 1
    seat[0] = seat_row
    seat[1] = seat_col
    return seat


def update_seat_assignment(_passenger_list):
    name = get_passenger_name()
    idx = get_passenger_idx(name, _passenger_list)

    if idx == -1:
        print("Passenger not found")
    else:
        passenger = _passenger_list[idx]
        print("Passenger found: ", passenger)
        seat = get_seat()
        passenger[2] = seat


def main():
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
            print("ADDING NEW PASSENGER:")
            passenger_list[passenger_count] = create_new_passenger()
            passenger_count += 1
        elif choice == 2:
            print("PRINTING ALL PASSENGERS:")
            for i in range(len(passenger_list)):
                print(str(i + 1) + ". " + str(passenger_list[i]))
        elif choice == 3:
            print("SEAT ASSIGNMENT:")
            update_seat_assignment(passenger_list)


if __name__ == "__main__":
    main()
