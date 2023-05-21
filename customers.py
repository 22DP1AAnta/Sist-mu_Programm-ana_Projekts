import json

class Customers:
    def __init__(self, name,surname, age, phone, address):
        self.name = name
        self.surname = surname
        self.age = age
        self.phone = phone
        self.address = address

    
    def append_data_to_customer(self, file_path, name, surname, age, phone, address):
        new_data = { 
            "name": name,
            "surname": surname,
            "age": age,
            "phone": phone,
            "address": address
        }
        try:
            with open(file_path, 'r', encoding="UTF-8") as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = []

        data.append(new_data)

        with open(file_path, 'w') as file:
            json.dump(data, file, indent=2)


    def print_data_of_customer(self, file_path):
        try:
            with open(file_path, 'r', encoding="UTF-8") as file:
                data = json.load(file)
        except FileNotFoundError:
            print("File not found.")
            return
        except json.JSONDecodeError:
            print("Invalid JSON format.")
            return

        if not data:
            print("No data available.")
            return

        # Print table header
        print("\n\n\033[92m" + "-" * 92 + "\033[0m")
        print(
            "№".ljust(3),
            "\033[92m" + "|" + "\033[0m",
            "Name".ljust(20),
            "\033[92m" + "|" + "\033[0m",
            "Surname".ljust(20),
            "\033[92m" + "|" + "\033[0m",
            "Age".ljust(5),
            "\033[92m" + "|" + "\033[0m",
            "Phone".ljust(15),
            "\033[92m" + "|" + "\033[0m",
            "Address"
        )

        # Print data rows"|"
        index = 0
        for customer in data:
            name = customer.get("name", "")
            surname = customer.get("surname", "")
            age = str(customer.get("age", ""))
            phone = customer.get("phone", "")
            address = customer.get("address", "")
            print("\033[92m" + "-" * 92 + "\033[0m")
            print(str(index).ljust(3),
                  "\033[92m" + "|" + "\033[0m",
                  name.ljust(20),"\033[92m" + "|" + "\033[0m",
                  surname.ljust(20),"\033[92m" + "|" + "\033[0m",
                  age.ljust(5),"\033[92m" + "|" + "\033[0m",
                  phone.ljust(15),"\033[92m" + "|" + "\033[0m",
                  address)
            index += 1

        print("\033[92m" + "-" * 92 + "\033[0m")
        print("\n\n")