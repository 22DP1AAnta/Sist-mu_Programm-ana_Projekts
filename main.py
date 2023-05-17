import json
from klienti import Customers

def main_menu():
    print("""Chose what to do:\n
    1. Add data\n
    2. Print data\n
    3. Delete data\n
    4. Search data\n
    5. Calculate whatever you need\n
    6. Filter data\n   
    7. Exit\n
    """)
    choice = input("Input your choice: ")
    if choice == "1":
        while True:
            append_data_to_json('customer.json', int(input("Input your age: ")), input("Input your name: "), input("Input your number: "), input("Input your adress: "))
            q_continue = input("Do you want to add something more?  Yes / No\n Your choice: ").lower()
            if q_continue == "no":
                break


        main_menu()

        
    elif choice == "2":
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

def append_data_to_json(file_path, age, name, number, address):  # izveidoju funkciju, kas lauj lietotajam pievienot datus funkcijai
    with open(file_path, 'r', encoding="UTF-8") as file:  # atveram file un nolasam jau eksistejosus datus
        data = json.load(file)
    
    new_data = {  # sample, lai pievienotu datus
        "age": age,
        "name": name,
        "number": number,
        "address": address
    }
    data.append(new_data)
    with open(file_path, 'w') as file:  # ierakstam datus json file
        json.dump(data, file, indent=2)

    

main_menu()