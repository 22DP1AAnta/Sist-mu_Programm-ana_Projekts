from customers import Customers
from workouts import Work_out
from coach import Coach
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
    choice = input("Input your choice: ")
    if choice == "1" or choice == "1.":
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
            reps = int(input("Input your reps: "))
            description = input("Input your description: ")
            weight = input("Input your weight: ")
            workout = Work_out(exercise, sets, reps, description, weight)
            
            while True:
                workout.append_data_to_workout('workout.json', exercise, sets, reps, description, weight)
                q_continue = input("Do you want to add something more to the file? Yes / No\nYour choice: ").lower()
                if q_continue == "no":
                    break
        elif choice2 == "3" or choice2 == "3.":
            name = input("Input your name: ")
            age = int(input("Input your sets: "))
            phone = int(input("Input your reps: "))
            address = input("Input your description: ")
            work_stasis = int(input("Input your work stasis: "))
            coach = Coach(name, age, phone, address, work_stasis)
            
            while True:
                coach.append_data_to_coach('workout.json', name, age, phone, address, work_stasis)
                q_continue = input("Do you want to add something more to the file? Yes / No\nYour choice: ").lower()
                if q_continue == "no":
                    break
    # ...
    """ ...    elif choice == "2":
        pass
    elif choice == "3":
        pass
    elif choice == "4":
        pass
    elif choice == "5":
        pass
    elif choice == "6":
        pass
    elif choice == "7":
        quit()
"""

main_menu()
