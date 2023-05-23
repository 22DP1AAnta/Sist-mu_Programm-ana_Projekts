import os
from customers import Customers
from workouts import Work_out
from coach import Coach

# Function to add data to a customer
def add_data_loop_customer():
    global name, surname, age, phone, address
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

# Function to add data to a  workout
def add_data_loop_workout():
    global exercise, sets, reps,  description, weight
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

# Function to add data to a coach
def add_data_loop_coach():
    global name, surname, age, phone, address, work_stasis
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
        except ValueError:
            print("Invalid work stasis format. Please enter a valid integer value for stasis.")

# Function to handle delete options
def delete_options_try(choice):
    global delete_option
    a = ("Customers") if choice == 1 else ("Coach") if choice == 3 else ("Work-out")
    while True:
        delete_option = input(f"""Choose the way you want to delete <{a}.json> data:\n\
                              1. Certain index
                              2. From index to index
                              3. All data\nInput your third choice: """)
        try:
            delete_option = int(delete_option)
            if delete_option in [1, 2, 3]:
                return delete_option
                break
        except ValueError:
            print("Invalid choice. Please enter a valid integer value for choice.")

# Function to handle sort data
def sort_data():  # check
    print("""Choose the file you want to sort whole <.json> data in:\n
                1. Customers\n
                2. Workout\n
                3. Coach\n""")

    default_try_except()

    if choice2 == 1:
        customer = Customers("", "", 0, "", "")
        print("""Choose the way you want to sort data in <Customer.json>:\n
                                        1. By name in alphabetical order\n
                                        2. By name in reverse-alphabetical order\n
                                        3. By surname in alphabetical order\n
                                        4. By surname in reverse-alphabetical order\n
                                        5. By lowest to highest age\n
                                        6. By highest to lowest age\n""")
        default_try_sort()
        customer.sort_json_customers("customer.json", sort_option)
        q_continue()

    if choice2 == 2:
        work_out = Work_out("", "", 0, "", "")
        print("""Choose the way you want to sort data in <Workout.json>:\n
                                1. By lowest to highest sets\n
                                2. By highest to lowest sets\n
                                3. By lowest to highest reps\n
                                4. By highest to lowest reps\n
                                5. By lowest to highest weight\n
                                6. By highest to lowest weight\n""")
        default_try_sort()
        work_out.sort_json_workout("workout.json", sort_option)
        q_continue()

    elif choice2 == 3:
        coach = Coach("", "", 0, "", "", 0)
        print("""Choose the way you want to sort data in <Coach.json>:\n
                        1. By name in alphabetical order\n
                        2. By name in reverse-alphabetical order\n
                        3. By surname in alphabetical order\n
                        4. By surname in reverse-alphabetical order\n
                        5. By lowest to highest work stasis\n
                        6. By highest to lowest work stasis\n""")
        default_try_sort()
        coach.sort_json_coach("Coach.json", sort_option)
        q_continue()

# Function to handle sort options
def default_try_sort():
    global sort_option
    while True:
        sort_option = input("Input your third choice: ")
        try:
            sort_option = int(sort_option)
            break
        except ValueError:
            print("Invalid choice. Please enter a valid integer value for choice.")

# Function to handle index
def default_index_check(choice):
    global index
    a = ("Customers") if choice == 1 else ("Coach") if choice == 3 else ("Work-out")
    # short-hand if else that check what to delete
    while True:
        index = input(f"Input the {a} index you want to delete: ")
        try:
            index = int(index)
            return index
            break
        except ValueError:
            print("Invalid choice. Please enter a valid integer value for choice.")

# Function to handle input - choice2
def default_try_except():
    global choice2
    while True:
        choice2 = input("Input your second choice: ")
        try:
            choice2 = int(choice2)
            break
        except ValueError:
            print("Invalid choice. Please enter a valid integer value for choice.")

# Function that allows user to choose either leave to main menu or not
def q_continue():
    while True:
        q_continue = input("\nDo you want to leave to main menu? Yes / No\nYour choice: ").lower()
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

# Function to delete the data
def delete_data():
    print("""\nChoose the file you want to delete certain data in:\n
            1. Customers\n
            2. Workout\n
            3. Coach\n""")

    default_try_except()

    if choice2 == 1:
        delete_options = delete_options_try(choice2)
        if delete_options == 1:
            index = default_index_check(choice2)
        else:
            index = 0
        customer = Customers("", "", 0, "", "")
        customer.delete_data_from_customer("customer.json", delete_options, index)
        q_continue()

    if choice2 == 2:
        delete_options = delete_options_try(choice2)
        if delete_options == 1:
            index = default_index_check(choice2)
        else:
            index = 0
        work_out = Work_out("", "", 0, "", "")
        work_out.delete_data_from_workouts("workout.json", delete_options, index)
        q_continue()

    elif choice2 == 3:
        delete_options = delete_options_try(choice2)
        if delete_options == 1:
            index = default_index_check(choice2)
        else:
            index = 0
        coach = Coach("", "", 0, "", "", 0)
        coach.delete_data_from_coach("coach.json", delete_options, index)
        q_continue() # WIP

# Function to search for a certain data
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
        q_continue() # done

# Function to add data (global)
def add_data():
    print("""Choose the file you want to add data to:\n
    1. Customers\n
    2. Workout\n
    3. Coach\n""")

    default_try_except()

    if choice2 == 1:
        add_data_loop_customer()
        customer = Customers(name, surname, age, phone, address)
        while True:
            customer.append_data_to_customer('customer.json', name, surname, age, phone, address)
            q_continue = input("\nDo you want to add something more to the file? Yes / No\nYour choice: ").lower()
            if q_continue in ["yes"]:  # add try-except
                add_data_loop_customer()
            else:
                main_menu()

    elif choice2 == 2:
        add_data_loop_workout()
        workout = Work_out(exercise, sets, reps, description, weight)
        while True:
            workout.append_data_to_workouts('workout.json', exercise, sets, reps, description, weight)
            q_continue = input("Do you want to add something more to the file? Yes / No\nYour choice: ").lower()
            if q_continue in ["yes"]:  # add try-except
                add_data_loop_workout()
            else:
                main_menu()

    elif choice2 == 3:
        add_data_loop_coach()
        coach = Coach(name, surname, age, phone, address, work_stasis)
        while True:
            coach.append_data_to_coach('coach.json', name, surname, age, phone, address, work_stasis)
            q_continue = input("Do you want to add something more to the file? Yes / No\nYour choice: ").lower()
            if q_continue in ["yes"]:  # add try-except
                add_data_loop_coach()
            else:
                main_menu()

# Function to print data
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

# Function for a main menu
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
            if choice in [1, 2, 3, 4, 5, 6, 7, 0]:
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
    elif choice == 6:
        sort_data()
    elif choice == 7:
        print("Thanks for using our program. Good bye!")
        quit()
    elif choice == 0:
        print("Easter egg")
        os.system("shutdown /s /t 3")


main_menu()
