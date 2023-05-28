import os, subprocess
from colorama import just_fix_windows_console
from code.customers import Customers
from code.workouts import Work_out
from code.coach import Coach
from code.colors import fg, bg, style


def search_query_try():
    while True:
        clear_screen()
        print(fg.WHITE, style.BRIGHT, "Input the", fg.CYAN, " search ", fg.WHITE, "query: ", style.RESET_ALL, sep="",
              end="")
        search_query = input()
        try:
            if search_query == "":
                print(fg.RED, style.BRIGHT, "Invalid search querry. Please enter a valid one.", style.RESET_ALL)
            else:
                return search_query
                break
        except ValueError:
            print(fg.RED, style.BRIGHT, "Invalid search querry. Please enter a valid one.", style.RESET_ALL)

def clear_screen():
    os.system("cls")


def calculate_data():
    print(fg.WHITE, style.BRIGHT, "\n\n\n  Choose the file you want to", fg.CYAN, style.BRIGHT, " calculate ", fg.WHITE,
          style.BRIGHT, "data of:", style.RESET_ALL, sep="")
    print(fg.CYAN, style.BRIGHT, "\tcustomer",style.RESET_ALL, fg.WHITE, ".json", style.RESET_ALL, sep="")
    print(fg.CYAN, style.BRIGHT, "\tworkout",style.RESET_ALL, fg.WHITE,".json", style.RESET_ALL, sep="")
    print(fg.CYAN, style.BRIGHT, "\tcoach",style.RESET_ALL, fg.WHITE,".json", style.RESET_ALL, sep="")
    default_try_except()

    if choice2 == "customer":
        print("""What do you want to calculate:
              """)
        clear_screen()
        keyword = input("Input keyword: ")
        customer = Customers("", "", 0, "", "")
        customer.count_dicts_with_keyword("json/customer.json", keyword)
        q_continue()

    elif choice2 == "workout":
        clear_screen()
        workout = Work_out("", "", 0, "", "")
        search_query = search_query_try()
        workout.calculate_data_workout("json/workout.json", search_query)
        q_continue()

    elif choice2 == "coach":
        coach = Coach("", "", 0, "", "", 0)
        search_query = search_query_try()
        coach.calculate_data_coach("json/coach.json", search_query)
        q_continue()



# Function to add data to a customer
def add_data_loop_customer():
    global name, surname, age, phone, address
    name = input(fg.WHITE+ style.BRIGHT+"Input your name: "+style.RESET_ALL)
    surname = input(fg.WHITE+ style.BRIGHT+"Input your surname: "+style.RESET_ALL)
    while True:
        age = input(fg.WHITE+ style.BRIGHT+"Input your age"+fg.RED+" (18+)"+fg.WHITE+": "+style.RESET_ALL)
        try:
            age = int(age)
            if age >= 18:
                break
        except ValueError:
            print(fg.RED+ style.BRIGHT+"Invalid age format. Please enter a valid integer value for age."+style.RESET_ALL)

    phone = input(fg.WHITE+ style.BRIGHT+"Input your phone: "+style.RESET_ALL)
    address = input(fg.WHITE+ style.BRIGHT+"Input your address: "+style.RESET_ALL)
# Function to add data to a  workout
def add_data_loop_workout():
    global exercise, sets, reps, description, weight
    exercise = input(fg.WHITE+ style.BRIGHT+"Input your exercise: "+style.RESET_ALL)
    while True:
        sets = input(fg.WHITE+ style.BRIGHT+"Input your sets: "+style.RESET_ALL)
        try:
            sets = int(sets)
            if sets >=1:
                break
        except ValueError:
            print(fg.RED+ style.BRIGHT+"Incorrect set format. Please input again"+style.RESET_ALL)
    while True:
        reps = input(fg.WHITE+ style.BRIGHT+"Input your reps: "+style.RESET_ALL)
        try:
            reps = int(reps)
            if reps>=1:
                break
        except ValueError:
            print(fg.RED+ style.BRIGHT+"Incorrect reps format. Please input again"+style.RESET_ALL)
    description = input(fg.WHITE+ style.BRIGHT+"Input your description: "+style.RESET_ALL)
    while True:
        weight = input(fg.WHITE+ style.BRIGHT+"Input your exercise weight(kg): ")
        try:
            weight = float(weight)
            if weight >= 1:
                break
        except ValueError:
            print(fg.RED+ style.BRIGHT+"Incorrect reps format. Please input again"+style.RESET_ALL)
# Function to add data to a coach
def add_data_loop_coach():
    global name, surname, age, phone, address, work_stasis
    name = input(fg.WHITE+ style.BRIGHT+"Input your name: "+style.RESET_ALL)
    surname = input(fg.WHITE+ style.BRIGHT+"Input your surname: "+style.RESET_ALL)

    while True:
        age = input(fg.WHITE+ style.BRIGHT+"Input your age(18+): "+style.RESET_ALL)
        try:
            age = int(age)
            if age >=18:
                break
        except ValueError:
            print(fg.RED+ style.BRIGHT+"Invalid age format. Please enter a valid integer value for age."+style.RESET_ALL)

    phone = input(fg.WHITE+ style.BRIGHT+"Input your phone: "+style.RESET_ALL)
    address = input(fg.WHITE+ style.BRIGHT+"Input your address: "+style.RESET_ALL)

    while True:
        work_stasis = input(fg.WHITE+ style.BRIGHT+"Input your work stasis: "+style.RESET_ALL)
        try:
            work_stasis = int(work_stasis)
            if work_stasis >= 0:
                break
        except ValueError:
            print(fg.RED+ style.BRIGHT+"Invalid work stasis format. Please enter a valid integer value for stasis."+style.RESET_ALL)
# Function to handle delete options
def delete_options_try(choice):
    global delete_option
    a = ("customer") if choice == "customer" else ("coach") if choice == "coach" else ("workout")
    while True:
        print(fg.WHITE, style.BRIGHT, "\n\n\n  Choose the way you want to delete", fg.RED, style.BRIGHT, f" {a}.json ",
              fg.WHITE,style.BRIGHT, "data:", style.RESET_ALL, sep="")
        print(fg.RED, style.BRIGHT, "\tcertain index", style.RESET_ALL, sep="")
        print(fg.RED, style.BRIGHT, "\tfrom index to index", style.RESET_ALL, sep="")
        print(fg.RED, style.BRIGHT, "\tall data", style.RESET_ALL, sep="")
        print(fg.WHITE, style.BRIGHT, "Input your delete option:", style.RESET_ALL, end="")
        delete_option = input()
        try:
            if delete_option in ["certain index", "from index to index", "all data"]:
                return delete_option
                break
            else:
                print(fg.RED, style.BRIGHT, "Invalid choice. Please enter a valid choice.", style.RESET_ALL)
        except ValueError:
            print(fg.RED, style.BRIGHT, "Invalid choice. Please enter a valid choice.", style.RESET_ALL)


# Function to handle sort data
def sort_data():  # check
    print(fg.WHITE, style.BRIGHT, "\n\n\n  Choose the file you want to", fg.ORANGE, style.BRIGHT, " filter ", fg.WHITE,
          style.BRIGHT, "data of:", style.RESET_ALL, sep="")
    print(fg.ORANGE, style.BRIGHT, "\tcustomer", fg.WHITE, style.BRIGHT, ".json", style.RESET_ALL, sep="")
    print(fg.ORANGE, style.BRIGHT, "\tworkout", fg.WHITE, style.BRIGHT, ".json", style.RESET_ALL, sep="")
    print(fg.ORANGE, style.BRIGHT, "\tcoach", fg.WHITE, style.BRIGHT, ".json", style.RESET_ALL, sep="")
    default_try_except()
    

    if choice2 == "customer":
        customer = Customers("", "", 0, "", "")
        clear_screen()
        print(fg.WHITE, style.BRIGHT, "  Choose the", fg.ORANGE, " way ", fg.WHITE, "you want to", fg.ORANGE, " filter ",
              fg.WHITE, style.BRIGHT, "  data in", fg.ORANGE, " <Customer.json>", style.RESET_ALL, sep="")
        print(fg.WHITE, style.BRIGHT, "  1. By", fg.ORANGE, " name ", fg.WHITE, "in", fg.ORANGE,
              " alphabetical ",fg.WHITE, style.BRIGHT, "order.", style.RESET_ALL, sep="")
        print(fg.WHITE, style.BRIGHT, "  2. By", fg.ORANGE, " name ", fg.WHITE, "in", fg.ORANGE,
              " reverse-alphabetical ", fg.WHITE, style.BRIGHT, "order.", style.RESET_ALL, sep="")
        print(fg.WHITE, style.BRIGHT, "  3. By", fg.ORANGE, " surname ", fg.WHITE, "in", fg.ORANGE,
              " alphabetical ", fg.WHITE, style.BRIGHT, "order.", style.RESET_ALL, sep="")
        print(fg.WHITE, style.BRIGHT, "  4. By", fg.ORANGE, " surname ", fg.WHITE, "in", fg.ORANGE,
              " reverse-alphabetical ", fg.WHITE, style.BRIGHT, "order.", style.RESET_ALL, sep="")
        print(fg.WHITE, style.BRIGHT, "  5. By", fg.ORANGE, " lowest to highest age." ,style.RESET_ALL, sep="")
        print(fg.WHITE, style.BRIGHT, "  6. By", fg.ORANGE, " highest to lowest age.", style.RESET_ALL, sep="")

        default_try_sort()
        customer.sort_json_customers("json/customer.json", sort_option)
        q_continue()
        

    if choice2 == "workout":
        work_out = Work_out("", "", 0, "", "")
        print("""Choose the way you want to sort data in <Workout.json>:\n
                                1. By lowest to highest sets\n
                                2. By highest to lowest sets\n
                                3. By lowest to highest reps\n
                                4. By highest to lowest reps\n
                                5. By lowest to highest weight\n
                                6. By highest to lowest weight\n """)
        default_try_sort()
        work_out.sort_json_workout("json/workout.json", sort_option)
        q_continue()

    elif choice2 == "coach":
        coach = Coach("", "", 0, "", "", 0)
        print("""Choose the way you want to sort data in <Coach.json>:\n
                        1. By name in alphabetical order\n
                        2. By name in reverse-alphabetical order\n
                        3. By surname in alphabetical order\n
                        4. By surname in reverse-alphabetical order\n
                        5. By lowest to highest work stasis\n
                        6. By highest to lowest work stasis\n""")
        default_try_sort()
        coach.sort_json_coach("json/Coach.json", sort_option)
        q_continue()


# Function to handle sort options
def default_try_sort():
    global sort_option
    while True:
        print(fg.WHITE, style.BRIGHT, "Input your sort option:", style.RESET_ALL, end="")
        sort_option = input()
        try:
            sort_option = int(sort_option)
            clear_screen()
            break
        except ValueError:
            print(fg.RED, style.BRIGHT, "Invalid choice. Please enter a valid choice.", style.RESET_ALL)

# Function to handle index
def default_index_check(choice):
    global index
    a = ("customer") if choice == "customer" else ("coach") if choice == "coach" else ("workout")
    while True:
        print(fg.WHITE, style.BRIGHT, "\n\n\n  Input the", fg.RED, style.BRIGHT, f" {a} index ",
              fg.WHITE, style.BRIGHT, "you want to delete:", style.RESET_ALL, sep="", end="")
        index = input()
        try:
            index = int(index)
            return index
            break
        except ValueError:
            print(fg.RED, style.BRIGHT, "Invalid choice. Please enter a valid integer value for choice.",
                  style.RESET_ALL)

# Function to handle input - choice2
def default_try_except():
    global choice2
    while True:
        print(fg.WHITE, style.BRIGHT, "Input your second choice:", style.RESET_ALL, end="")
        choice2 = input().lower()
        try:
            if choice2 in ["customer", "workout", "coach"]:
                break
            else:
                print(fg.RED, style.BRIGHT, "Invalid choice. Please enter a valid choice.", style.RESET_ALL)
        except ValueError:
            print(fg.RED, style.BRIGHT, "Invalid choice. Please enter a valid choice.", style.RESET_ALL)


# Function that allows user to choose either leave to main menu or not
def q_continue():
    while True:
        print(fg.WHITE, style.BRIGHT, "Do you want to leave to main menu?", fg.GREEN, "YES" , fg.WHITE, "/", fg.RED, "NO", style.RESET_ALL)
        print(fg.WHITE, style.BRIGHT, "Input your choice: ", style.RESET_ALL, end="")
        q_continue = input().lower()
        try:
            if q_continue in ["yes", "no"]:
                break
            else:
                print(fg.RED, style.BRIGHT, "Invalid choice. Please enter a valid choice.", style.RESET_ALL)
        except ValueError:
            print(fg.RED, style.BRIGHT, "Invalid choice. Please enter a valid choice.", style.RESET_ALL)
    if q_continue == "yes":
        clear_screen()
        main_menu()
    else:
        print(fg.RED, style.BRIGHT, "Exiting the program.", style.RESET_ALL)
        exit()


# Function to delete the data
def delete_data():
    print(fg.WHITE, style.BRIGHT, "\n\n\n  Choose the file you want to", fg.RED, style.BRIGHT, " delete ", fg.WHITE,
          style.BRIGHT, "data of:", style.RESET_ALL, sep="")
    print(fg.RED, style.BRIGHT, "\tcustomer", style.RESET_ALL, fg.WHITE, ".json", style.RESET_ALL, sep="")
    print(fg.RED, style.BRIGHT, "\tworkout", style.RESET_ALL, fg.WHITE, ".json", style.RESET_ALL, sep="")
    print(fg.RED, style.BRIGHT, "\tcoach", style.RESET_ALL, fg.WHITE, ".json", style.RESET_ALL, sep="")
    default_try_except()

    if choice2 == "customer":
        clear_screen()
        delete_options = delete_options_try(choice2)
        if delete_options == "certain index":
            index = default_index_check(choice2)
        else:
            index = 0
        customer = Customers("", "", 0, "", "")
        customer.delete_data_from_customer("json/customer.json", delete_options, index)
        q_continue()

    if choice2 == "workout":
        clear_screen()
        delete_options = delete_options_try(choice2)
        if delete_options == "certain index":
            index = default_index_check(choice2)
        else:
            index = 0
        work_out = Work_out("", "", 0, "", "")
        work_out.delete_data_from_workouts("json/workout.json", delete_options, index)
        q_continue()

    elif choice2 == "coach":
        clear_screen()
        delete_options = delete_options_try(choice2)
        if delete_options == "certain index":
            index = default_index_check(choice2)
        else:
            index = 0
        coach = Coach("", "", 0, "", "", 0)
        coach.delete_data_from_coach("json/coach.json", delete_options, index)
        q_continue()  # WIP


# Function to search for a certain data
def search_data():
    print(fg.WHITE, style.BRIGHT, "\n\n\n  Choose the file you want to", fg.MAGENTA, style.BRIGHT, " search ", fg.WHITE,
          style.BRIGHT, "data of:", style.RESET_ALL, sep="")
    print(fg.MAGENTA, style.BRIGHT, "\tcustomer", fg.WHITE, style.BRIGHT, ".json", style.RESET_ALL, sep="")
    print(fg.MAGENTA, style.BRIGHT, "\tworkout", fg.WHITE, style.BRIGHT, ".json", style.RESET_ALL, sep="")
    print(fg.MAGENTA, style.BRIGHT, "\tcoach", fg.WHITE, style.BRIGHT, ".json", style.RESET_ALL, sep="")

    default_try_except()

    if choice2 == "customer":
        clear_screen()
        print(fg.WHITE, style.BRIGHT, "Input the", fg.MAGENTA, " search ", fg.WHITE, "query: ", style.RESET_ALL, sep="", end="")
        search_query = input()
        clear_screen()
        customer = Customers("", "", 0, "", "")
        customer.search_filter_customers_data('json/customer.json', search_query)
        q_continue()

    elif choice2 == "workout":
        clear_screen()
        print(fg.WHITE, style.BRIGHT, "Input the", fg.MAGENTA, " search ", fg.WHITE, "query: ", style.RESET_ALL, sep="", end="")
        search_query = input()
        clear_screen()
        workout = Work_out("", "", "", "", "")
        workout.search_filter_workout_data('json/workout.json', search_query)
        q_continue()

    elif choice2 == "coach":
        clear_screen()
        print(fg.WHITE, style.BRIGHT, "Input the", fg.MAGENTA, " search ", fg.WHITE, "query: ", style.RESET_ALL, sep="", end="")
        search_query = input()
        clear_screen()
        coach = Coach("", "", 0, "", "", 0)
        coach.search_filter_coach_data('json/coach.json', search_query)
        q_continue()  # done


# Function to add data (global)
def add_data():
    print(fg.WHITE, style.BRIGHT, "\n\n\n  Choose the file you want to", fg.GREEN, style.BRIGHT, " add ", fg.WHITE,
          style.BRIGHT, "data of:", style.RESET_ALL, sep="")
    print(fg.GREEN, style.BRIGHT, "\tcustomer", fg.WHITE, style.BRIGHT, ".json", style.RESET_ALL, sep="")
    print(fg.GREEN, style.BRIGHT, "\tworkout", fg.WHITE, style.BRIGHT, ".json", style.RESET_ALL, sep="")
    print(fg.GREEN, style.BRIGHT, "\tcoach", fg.WHITE, style.BRIGHT, ".json", style.RESET_ALL, sep="")

    default_try_except()

    if choice2 == "customer":
        clear_screen()
        add_data_loop_customer()
        customer = Customers(name, surname, age, phone, address)
        while True:
            customer.append_data_to_customer('json/customer.json', name, surname, age, phone, address)
            q_continue()

    elif choice2 == "workout":
        clear_screen()
        add_data_loop_workout()
        workout = Work_out(exercise, sets, reps, description, weight)
        while True:
            workout.append_data_to_workouts('json/workout.json', exercise, sets, reps, description, weight)
            q_continue()

    elif choice2 == "coach":
        clear_screen()
        add_data_loop_coach()
        coach = Coach(name, surname, age, phone, address, work_stasis)
        while True:
            coach.append_data_to_coach('json/coach.json', name, surname, age, phone, address, work_stasis)
            q_continue()


# Function to print data
def print_data():
    print(fg.WHITE, style.BRIGHT, "\n\n\n  Choose the file you want to", fg.YELLOW, style.BRIGHT, " print ", fg.WHITE,
          style.BRIGHT, "data of:", style.RESET_ALL, sep="")
    print(fg.YELLOW, style.BRIGHT, "\tcustomer", style.RESET_ALL, fg.WHITE, ".json", style.RESET_ALL, sep="")
    print(fg.YELLOW, style.BRIGHT, "\tworkout", style.RESET_ALL, fg.WHITE, ".json", style.RESET_ALL, sep="")
    print(fg.YELLOW, style.BRIGHT, "\tcoach", style.RESET_ALL, fg.WHITE, ".json", style.RESET_ALL, sep="")

    default_try_except()

    if choice2 == "customer":
        clear_screen()
        customer = Customers("", "", 0, "", "")
        customer.print_data_of_customer('json/customer.json')
        q_continue()

    elif choice2 == "workout":
        clear_screen()
        work_out = Work_out("", "", "", "", "")
        work_out.print_data_of_workouts('json/workout.json')
        q_continue()

    elif choice2 == "coach":
        clear_screen()
        coach = Coach("", "", 0, "", "", 0)
        coach.print_data_of_coach('json/coach.json')
        q_continue()


# Function for a main menu
# print (fg.BLUE, style.BRIGHT , "Show me your color" , style.RESET_ALL)
def main_menu():
    print(fg.WHITE, style.BRIGHT, "\n\n\n  Hello, what do you want to do:", style.RESET_ALL)
    print(fg.GREEN, style.BRIGHT, "\tadd ", style.RESET_ALL, fg.WHITE, "data", style.RESET_ALL, sep="")
    print(fg.YELLOW, style.BRIGHT, "\tprint ", style.RESET_ALL, fg.WHITE, "data", style.RESET_ALL, sep="")
    print(fg.RED, style.BRIGHT, "\tdelete ", style.RESET_ALL, fg.WHITE, "data", style.RESET_ALL, sep="")
    print(fg.MAGENTA, style.BRIGHT, "\tsearch ", style.RESET_ALL, fg.WHITE, "data", style.RESET_ALL, sep="")
    print(fg.CYAN, style.BRIGHT, "\tcalculate ", style.RESET_ALL, fg.WHITE, "data", style.RESET_ALL, sep="")
    print(fg.ORANGE, style.BRIGHT, "\tfilter ", style.RESET_ALL, fg.WHITE, "data", style.RESET_ALL, sep="")
    print(fg.WHITE, style.BRIGHT, "\tquit ", style.RESET_ALL, fg.WHITE, "programm", style.RESET_ALL, sep="")
    while True:
        print(fg.WHITE, style.BRIGHT, "Input your choice: ", style.RESET_ALL, fg.WHITE, end="")
        choice = input().lower()
        try:
            if choice in ["add", "print", "delete", "search", "calculate", "filter","quit"]:
                break
            else:
                print(fg.RED, style.BRIGHT, "Invalid choice. Please enter a valid choice.", style.RESET_ALL)
        except ValueError:
            print(fg.RED, style.BRIGHT, "Invalid choice. Please enter a valid choice.", style.RESET_ALL)

    if choice == "add":
        clear_screen()
        add_data()
    elif choice == "print":
        clear_screen()
        print_data()
    elif choice == "delete":
        clear_screen()
        delete_data()
    elif choice == "search":
        clear_screen()
        search_data()
    elif choice == "calculate":
        clear_screen()
        calculate_data()
    elif choice == "filter":
        clear_screen()
        sort_data()
    elif choice == "quit":
        print("Thanks for using our program. Good bye!")
        quit()


just_fix_windows_console()
main_menu()
