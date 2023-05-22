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

    def search_filter_customers_data(self, file_path, search_query):
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

        # Filter data based on search query
        filtered_data = []
        for customer in data:
            name = customer.get("name", "")
            surname = customer.get("surname", "")
            age = str(customer.get("age", ""))
            phone = customer.get("phone", "")
            address = customer.get("address", "")

            # Check if any attribute matches the search query
            if (
                    search_query.lower() in name.lower()
                    or search_query.lower() in surname.lower()
                    or search_query.lower() in age.lower()
                    or search_query.lower() in phone.lower()
                    or search_query.lower() in address.lower()
            ):
                filtered_data.append(customer)

        if not filtered_data:
            print("No matching data found.")
            return

        # Print filtered data
        print("\n\n\033[92m" + "-" * 115 + "\033[0m")
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

        # Print filtered data rows
        index = 0
        for customer in filtered_data:
            name = customer.get("name", "")
            surname = customer.get("surname", "")
            age = str(customer.get("age", ""))
            phone = customer.get("phone", "")
            address = customer.get("address", "")

            print("\033[92m" + "-" * 115 + "\033[0m")
            print(
                str(index).ljust(3),
                "\033[92m" + "|" + "\033[0m",
                name.ljust(20),
                "\033[92m" + "|" + "\033[0m",
                surname.ljust(20),
                "\033[92m" + "|" + "\033[0m",
                age.ljust(5),
                "\033[92m" + "|" + "\033[0m",
                phone.ljust(15),
                "\033[92m" + "|" + "\033[0m",
                address
            )
            index += 1

        print("\033[92m" + "-" * 115 + "\033[0m")
        print("\n\n")

    def delete_data_from_customers(self, file_path, index):
        # Read the JSON file and load its contents into a Python variable.
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

        if index < 0 or index >= len(data): # Check if the index is within the valid range.
            print("Invalid index.")
            return

        del data[index] # Delete the element at the specified index.

        with open(file_path, 'w') as file:  # Write the updated JSON data back to the file.
            json.dump(data, file, indent=2)

        print("Data deleted successfully.")

    @staticmethod
    def sort_json_customers(file_path, sort_option):
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

        if sort_option == 1:  # by name in alphabetical order
            sorted_data = sorted(data, key=lambda x: x['name'])
        elif sort_option == 2:
            sorted_data = sorted(data, key=lambda x: x['name'], reverse=True)  # reverse =  True, reverses the sort
        elif sort_option == 3:  # by surname in alphabetical order
            sorted_data = sorted(data, key=lambda x: x['surname'])
        elif sort_option == 4:
            sorted_data = sorted(data, key=lambda x: x['surname'], reverse=True)
        elif sort_option == 5:  # by age
            sorted_data = sorted(data, key=lambda x: x['age'])
        elif sort_option == 6:
            sorted_data = sorted(data, key=lambda x: x['age'], reverse=True)
        else:
            print("Invalid sort option.")
            return

        with open(file_path, 'w') as file:
            json.dump(sorted_data, file, indent=2)

        print("Data sorted successfully.")