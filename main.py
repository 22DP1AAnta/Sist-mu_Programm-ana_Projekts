from customers import Customers
from workouts import Work_out
from coach import Coach


def default_index_check(choice):
    global index
    a = ("Customers") if choice == 1 else ("Coach") if choice == 3 else ("Work-out")
    # short-hand if else that check what to delete
    while True:
        index = input(f"Input the {a} index you want to delete: ")
        try:
            index = int(index)
            break
        except ValueError:
            print("Invalid choice. Please enter a valid integer value for choice.")
def default_try_except():
    global choice2
    while True:
        choice2 = input("Input your second choice: ")
        try:
            choice2 = int(choice2)
            break
        except ValueError:
            print("Invalid choice. Please enter a valid integer value for choice.")
def q_continue():
    while True:
        q_continue = input("Do you want to leave to main menu? Yes / No\nYour choice: ").lower()
        try:
            if q_continue in ["yes", "no"]:
                break
            else:
                print("Invalid input. Please enter a valid choice.")
        except ValueError:
            print("Invalid input. Please enter a valid choice.")
    if q_continue == "yes":
        main_menu()
    else:
        print("Exiting the program.")
        exit()
def delete_data():
    print("""Choose the file you want to delete certain data in:\n
            1. Customers\n
            2. Workout\n
            3. Coach\n""")

    default_try_except()

    if choice2 == 1:
        default_index_check(choice2)
        customer = Customers("", "", 0, "", "")
        customer.delete_data_from_customers("customer.json", index)
        q_continue()

    if choice2 == 2:
        default_index_check(choice2)
        work_out = Work_out("", "", 0, "", "")
        work_out.delete_data_from_workouts("workout.json", index)
        q_continue()

    elif choice2 == 3:
        default_index_check(choice2)
        coach = Coach("", "", 0, "", "", 0)
        coach.delete_data_from_coach("coach.json", index )
        q_continue()


def search_data():
    print("""Choose the file you want to search / filter data in:\n
        1. Customers\n
        2. Workout\n
        3. Coach\n""")

    default_try_except()

    if choice2 == 1:
        search_query = input("Input the search query: ")
        customer = Customers("", "", 0, "", "")
        customer.search_filter_customers_data('customer.json', search_query)
        q_continue()

    elif choice2 == 2:
        search_query = input("Input the search query: ")
        workout = Work_out("", "", "", "", "")
        workout.search_filter_coach_data('workout.json', search_query)
        q_continue()

    elif choice2 == 3:
        search_query = input("Input the search query: ")
        coach = Coach("", "", 0, "", "", 0)
        coach.search_filter_coach_data('coach.json', search_query)
        q_continue()


def add_data():
    print("""Choose the file you want to add data to:\n
    1. Customers\n
    2. Workout\n
    3. Coach\n""")

    default_try_except()

    if choice2 == 1:
        name = input("Input your name: ")
        surname = input("Input your surname: ")
        while True:
            age = input("Input your age: ")
            try:
                age = int(age)
                break
            except ValueError:
                print("Invalid age format. Please enter a valid integer value for age.")

        phone = input("Input your phone: ")
        address = input("Input your address: ")
        customer = Customers(name, surname, age, phone, address)

        while True:
            customer.append_data_to_customer('customer.json', name, surname, age, phone, address)
            q_continue = input("\nDo you want to add something more to the file? Yes / No\nYour choice: ").lower()
            if q_continue == "no":
                main_menu()
            else:
                name = input("Input your name: ")
                surname = input("Input your surname: ")
                while True:
                    age = input("Input your age: ")
                    try:
                        age = int(age)
                        break
                    except ValueError:
                        print("Invalid age format. Please enter a valid integer value for age.")

                phone = input("Input your phone: ")
                address = input("Input your address: ")
    elif choice2 == 2:
        exercise = input("Input your exercise: ")
        while True:
            sets = input("Input your sets: ")
            try:
                sets = int(sets)
                break
            except ValueError:
                print("Incorrect set format. Please input again")
        while True:
            reps = input("Input your reps: ")
            try:
                reps = int(reps)
                break
            except ValueError:
                print("Incorrect reps format. Please input again")
        description = input("Input your description: ")
        while True:
            weight = input("Input your weight(kg): ")
            try:
                weight = float(weight)
                break
            except ValueError:
                print("Incorrect reps format. Please input again")

        workout = Work_out(exercise, sets, reps, description, weight)
        while True:
            workout.append_data_to_workouts('workout.json', exercise, sets, reps, description, weight)
            q_continue = input("Do you want to add something more to the file? Yes / No\nYour choice: ").lower()
            if q_continue == "no":
                main_menu()
            else:
                exercise = input("Input your exercise: ")
                while True:
                    sets = input("Input your sets: ")
                    try:
                        sets = int(sets)
                        break
                    except ValueError:
                        print("Incorrect set format. Please input again")
                while True:
                    reps = input("Input your reps: ")
                    try:
                        reps = int(reps)
                        break
                    except ValueError:
                        print("Incorrect reps format. Please input again")
                description = input("Input your description: ")
                while True:
                    weight = input("Input your weight(kg): ")
                    try:
                        weight = float(weight)
                        break
                    except ValueError:
                        print("Incorrect reps format. Please input again")

    elif choice2 == 3:
        name = input("Input your name: ")
        surname = input("Input your surname: ")

        while True:
            age_input = input("Input your age: ")
            try:
                age = int(age_input)
                break
            except ValueError:
                print("Invalid age format. Please enter a valid integer value for age.")

        phone = input("Input your phone: ")
        address = input("Input your address: ")

        while True:
            work_stasis = input("Input your work stasis: ")
            try:
                work_stasis = int(work_stasis)
                break
            except ValueError:
                print("Invalid work stasis format. Please enter a valid integer value for stasis.")
        coach = Coach(name, surname, age, phone, address, work_stasis)
        while True:
            coach.append_data_to_coach('coach.json', name, surname, age, phone, address, work_stasis)
            q_continue = input("Do you want to add something more to the file? Yes / No\nYour choice: ").lower()
            if q_continue == "no":
                main_menu()
            else:
                name = input("Input your name: ")
                surname = input("Input your surname: ")
                while True:
                    age = input("Input your age: ")
                    try:
                        age = int(age)
                        break
                    except ValueError:
                        print("Invalid age format. Please enter a valid integer value for age.")
                phone = input("Input your phone: ")
                address = input("Input your address: ")
                while True:
                    work_stasis = input("Input your work stasis: ")
                    try:
                        work_stasis = int(work_stasis)
                        break
                    except:
                        print("Invalid work stasis format. Please enter a valid integer value for stasis.")
                coach = Coach(name, surname, age, phone, address, work_stasis)



def print_data():
    print("""Choose the file you want to print data of:\n
        1. Customers\n
        2. Workout\n
        3. Coach\n""")

    default_try_except()

    if choice2 == 1:
        customer = Customers("", "", 0, "", "")
        customer.print_data_of_customer('customer.json')
        q_continue()

    elif choice2 == 2:
        work_out = Work_out("", "", "", "", "")
        work_out.print_data_of_workouts('workout.json')
        q_continue()

    elif choice2 == 3:
        coach = Coach("", "", 0, "", "", 0)
        coach.print_data_of_coach('coach.json')
        q_continue()



def main_menu():
    print("""Choose what to do:\n
    1. Add data\n
    2. Print data\n
    3. Delete data\n
    4. Search data\n
    5. Calculate whatever you need\n
    6. Filter data\n   
    7. Exit\n
    """)

    while True:
        choice = input("Input your choice: ")
        try:
            choice = int(choice)  # Convert the input to an integer
            if choice in [1, 2, 3, 4, 5, 6, 7]:
                break
            else:
                print("Invalid choice. Please enter a valid integer value for choice.")
        except ValueError:
            print("Invalid choice. Please enter a valid integer value for choice.")

    if choice == 1:
        add_data()
    elif choice == 2:
        print_data()
    elif choice == 3:
        delete_data()
    elif choice == 4:
        search_data()
    elif choice == 7:
        print("Thanks for using our program. Good bye!")
        quit()


main_menu()
