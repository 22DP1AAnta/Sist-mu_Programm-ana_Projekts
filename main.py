from customers import Customers
from workouts import Work_out
from coach import Coach


def add_data():
    print("""Choose the file you want to add data to:\n
    1. Customers\n
    2. Workout\n
    3. Coach\n""")
    choice2 = input("Input your second choice: ")
    if choice2 == "1" or choice2 == "1.":
        name = input("Input your name: ")
        surname = input("Input your surname: ")
        age = int(input("Input your age: "))
        phone = input("Input your phone: ")
        address = input("Input your address: ")
        customer = Customers(name, surname, age, phone, address)
        while True:
            customer.append_data_to_customer('customer.json', name, surname, age, phone, address)
            q_continue = input("Do you want to add something more to the file? Yes / No\nYour choice: ").lower()
            if q_continue == "no":
                break
    elif choice2 == "2" or choice2 == "2.":
        exercise = input("Input your exercise: ")
        sets = input("Input your sets: ")
        reps = input("Input your reps: ")
        description = input("Input your description: ")
        weight = input("Input your weight: ")
        workout = Work_out(exercise, sets, reps, description, weight)
        while True:
            workout.append_data_to_workouts('workout.json', exercise, sets, reps, description, weight)
            q_continue = input("Do you want to add something more to the file? Yes / No\nYour choice: ").lower()
            if q_continue == "no":
                break
    elif choice2 == "3" or choice2 == "3.":
        name = input("Input your name: ")
        surname = input("Input your surname: ")
        age = int(input("Input your age: "))
        phone = input("Input your phone: ")
        address = input("Input your address: ")
        work_stasis = int(input("Input your work stasis: "))
        coach = Coach(name, surname, age, phone, address, work_stasis)
        while True:
            coach.append_data_to_coach('coach.json', name, surname, age, phone, address, work_stasis)
            q_continue = input("Do you want to add something more to the file? Yes / No\nYour choice: ").lower()
            if q_continue == "no":
                break

def print_data():
    print("""Choose the file you want to print data of:\n
        1. Customers\n
        2. Workout\n
        3. Coach\n""")
    choice2 = input("Input your second choice: ")
    if choice2 == "1" or choice2 == "1.":
        customer = Customers("", "", 0, "", "")
        customer.print_data_of_customer('customer.json')
        q_continue = input("Do you want to leave to main menu? Yes / No\nYour choice: ").lower()
        if q_continue == "menu":
            main_menu()
        else:
            exit()
    elif choice2 == "2" or choice2 == "2.":
        work_out = Work_out("","","","","")
        work_out.print_data_of_workouts('workout.json')
        q_continue = input("Do you want to leave to main menu? Yes / No\nYour choice: ").lower()
        if q_continue == "menu":
            main_menu()
        else:
            exit()
    elif choice2 == "3" or choice2 == "3.":
        coach = Coach("","", 0, "", "", 0)
        coach.print_data_of_coach('coach.json')
        q_continue = input("Do you want to leave to main menu? Yes / No\nYour choice: ").lower()
        if q_continue == "menu":
            main_menu()
        else:
            exit()




def main_menu():
    global choice
    print("""Choose what to do:\n
    1. Add data\n
    2. Print data\n
    3. Delete data\n
    4. Search data\n
    5. Calculate whatever you need\n
    6. Filter data\n   
    7. Exit\n
    """)
    choice = input("Input your choice: ")

    if choice == "1" or choice == "1.":
        add_data()
    if choice == "2" or choice == "2.":
        print_data()




main_menu()
