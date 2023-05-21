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
    elif choice2 == "2" or choice2 == "2.":
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
                
    elif choice2 == "3" or choice2 == "3.":
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
    choice2 = input("Input your second choice: ")
    if choice2 == "1" or choice2 == "1.":
        customer = Customers("", "", 0, "", "")
        customer.print_data_of_customer('customer.json')
        q_continue = input("Do you want to leave to main menu? Yes / No\nYour choice: ").lower()
        if q_continue == "no":
            main_menu()
        else:
            exit()
    elif choice2 == "2" or choice2 == "2.":
        work_out = Work_out("","","","","")
        work_out.print_data_of_workouts('workout.json')
        q_continue = input("Do you want to leave to main menu? Yes / No\nYour choice: ").lower()
        if q_continue == "no":
            main_menu()
        else:
            exit()
    elif choice2 == "3" or choice2 == "3.":
        coach = Coach("","", 0, "", "", 0)
        coach.print_data_of_coach('coach.json')
        q_continue = input("Do you want to leave to main menu? Yes / No\nYour choice: ").lower()
        if q_continue == "no":
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
    if choice == "7" or choice == "7.":
        quit()




main_menu()
