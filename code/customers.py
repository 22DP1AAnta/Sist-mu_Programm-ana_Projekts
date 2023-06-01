import json
import os
from code.colors import fg, style


def clear_screen():
    os.system("cls")


class Customers:
    def __init__(self, name, surname, age, phone, address):
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
            clear_screen()
            print(fg.RED, style.BRIGHT, "File not found.", style.RESET_ALL)
            return
        except json.JSONDecodeError:
            clear_screen()
            print(fg.RED, style.BRIGHT, "Invalid JSON format.", style.RESET_ALL)
            return
        if not data:
            clear_screen()
            print(fg.RED, style.BRIGHT, "No data available.", style.RESET_ALL)
            return

        # Print table header
        print("\n\n\033[92m" + "-" * 92 + "\033[0m")
        print(
            "№".ljust(3),
            "\033[92m" + "|" + "\033[0m",
            "Name".ljust(15),
            "\033[92m" + "|" + "\033[0m",
            "Surname".ljust(15),
            "\033[92m" + "|" + "\033[0m",
            "Age".ljust(5),
            "\033[92m" + "|" + "\033[0m",
            "Phone".ljust(12),
            "\033[92m" + "|" + "\033[0m",
            "Address"
        )

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
                  name.ljust(15), "\033[92m" + "|" + "\033[0m",
                  surname.ljust(15), "\033[92m" + "|" + "\033[0m",
                  age.ljust(5), "\033[92m" + "|" + "\033[0m",
                  phone.ljust(12), "\033[92m" + "|" + "\033[0m",
                  address)
            index += 1

        print("\033[92m" + "-" * 92 + "\033[0m")
        print("\n\n")

    def search_filter_customers_data(self, file_path, search_query):
        try:
            with open(file_path, 'r', encoding="UTF-8") as file:
                data = json.load(file)
        except FileNotFoundError:
            clear_screen()
            print(fg.RED, style.BRIGHT, "File not found.", style.RESET_ALL)
            return
        except json.JSONDecodeError:
            clear_screen()
            print(fg.RED, style.BRIGHT, "Invalid JSON format.", style.RESET_ALL)
            return
        if not data:
            clear_screen()
            print(fg.RED, style.BRIGHT, "No data available.", style.RESET_ALL)
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

    def delete_data_from_customer(self, file_path, delete_option, index):
        try:
            with open(file_path, 'r', encoding="UTF-8") as file:
                data = json.load(file)
        except FileNotFoundError:
            clear_screen()
            print(fg.RED, style.BRIGHT, "File not found.", style.RESET_ALL)
            return
        except json.JSONDecodeError:
            clear_screen()
            print(fg.RED, style.BRIGHT, "Invalid JSON format.", style.RESET_ALL)
            return
        if not data:
            clear_screen()
            print(fg.RED, style.BRIGHT, "No data available.", style.RESET_ALL)
            return

        if delete_option == "certain index":
            clear_screen()
            if index < 0 or index >= len(data):
                print(fg.RED, style.BRIGHT, "  Invalid index.", style.RESET_ALL)
                return
            del data[index]
        elif delete_option == "from index to index":
            clear_screen()
            print(fg.WHITE, style.BRIGHT, "  Enter the", fg.RED, " start index ",
                  fg.WHITE, "to delete: ", style.RESET_ALL, sep="", end="")
            start_index = int(input())
            print(fg.WHITE, style.BRIGHT, "  Enter the", fg.RED, " end ",
                  fg.WHITE, "index to delete: ", style.RESET_ALL, sep="", end="")
            end_index = int(input())
            if start_index < 0 or start_index >= len(data) or end_index < 0 or end_index >= len(data):
                print(fg.RED, style.BRIGHT, "  Invalid index.", style.RESET_ALL)
                return
            del data[start_index:end_index + 1]
        elif delete_option == "all data":
            clear_screen()
            data.clear()
        else:
            print(fg.RED, style.BRIGHT,
                  "  Invalid delete option.", style.RESET_ALL)
            return

        with open(file_path, 'w') as file:
            json.dump(data, file, indent=2)

        print(fg.GREEN, style.BRIGHT,
              "  Data deleted successfully.", style.RESET_ALL)

    # 6 funkcija
    @staticmethod
    def sort_json_customers(file_path, sort_option):
        try:
            with open(file_path, 'r', encoding="UTF-8") as file:
                data = json.load(file)
        except FileNotFoundError:
            clear_screen()
            print(fg.RED, style.BRIGHT, "File not found.", style.RESET_ALL)
            return
        except json.JSONDecodeError:
            clear_screen()
            print(fg.RED, style.BRIGHT, "Invalid JSON format.", style.RESET_ALL)
            return
        if not data:
            clear_screen()
            print(fg.RED, style.BRIGHT, "No data available.", style.RESET_ALL)
            return

        if sort_option == 1:  # by name in alphabetical order
            sorted_data = sorted(data, key=lambda x: x['name'])
        elif sort_option == 2:  # by
            # reverse =  True, reverses the sort
            sorted_data = sorted(data, key=lambda x: x['name'], reverse=True)
        elif sort_option == 3:  # by surname in alphabetical order
            sorted_data = sorted(data, key=lambda x: x['surname'])
        elif sort_option == 4:
            sorted_data = sorted(
                data, key=lambda x: x['surname'], reverse=True)
        elif sort_option == 5:  # by age
            sorted_data = sorted(data, key=lambda x: x['age'])
        elif sort_option == 6:
            sorted_data = sorted(data, key=lambda x: x['age'], reverse=True)
        else:
            print(fg.RED, style.BRIGHT, "Invalid sort option.", style.RESET_ALL)
            return

        with open(file_path, 'w') as file:
            json.dump(sorted_data, file, indent=2)

        print(fg.WHITE, style.BRIGHT, "Data sorted successfully.", style.RESET_ALL)

    def calculate_data_customer(self, file_path, search_query):
        try:
            with open(file_path, 'r', encoding="UTF-8") as file:
                data = json.load(file)
        except FileNotFoundError:
            clear_screen()
            print(fg.RED, style.BRIGHT, "File not found.", style.RESET_ALL)
            return
        except json.JSONDecodeError:
            clear_screen()
            print(fg.RED, style.BRIGHT, "Invalid JSON format.", style.RESET_ALL)
            return
        if not data:
            clear_screen()
            print(fg.RED, style.BRIGHT, "No data available.", style.RESET_ALL)
            return

        matching_data = []
        for customer in data:
            name = customer.get("name", "")
            surname = customer.get("surname", "")
            age = str(customer.get("age", ""))
            phone = customer.get("phone", "")
            address = customer.get("address", "")

            if (
                    search_query in name.lower()
                    or search_query in surname.lower()
                    or search_query in age.lower()
                    or search_query in phone.lower()
                    or search_query in address.lower()
            ):
                matching_data.append(customer)

        count = len(matching_data)
        clear_screen()
        print(fg.WHITE, style.BRIGHT, "By querry: ", fg.CYAN, search_query, fg.WHITE, ", has been found ", fg.CYAN,
              count, fg.WHITE, " mathching data.", style.RESET_ALL, sep="")
