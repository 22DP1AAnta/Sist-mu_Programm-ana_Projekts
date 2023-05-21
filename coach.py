import json
class Coach:  # definejam klasi
    def __init__(self, name , surname, age, phone, address, work_stasis):
        self.name = name
        self.surname = surname
        self.age = age
        self.phone = phone
        self.address = address
        self.work_stasis = work_stasis


    def append_data_to_coach(self, file_path, name, surname, age, phone, address, work_stasis):
        new_data = { 
            "name": name,
            "surname" : surname,
            "age": age,
            "phone": phone,
            "address": address,
            "work_stasis": work_stasis
        }

        try:
            with open(file_path, 'r', encoding="UTF-8") as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = []

        data.append(new_data)
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=2)



    def print_data_of_coach(self, file_path):
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
            "Stasis".ljust(5),
            "\033[92m" + "|" + "\033[0m",
            "Phone".ljust(15),
            "\033[92m" + "|" + "\033[0m",
            "Address"
        )

        # Print data rows"|"
        index = 0
        for coach in data:
            name = coach.get("name", "")
            surname = coach.get("surname", "")
            age = str(coach.get("age", ""))
            phone = coach.get("phone", "")
            address = coach.get("address", "")
            work_stasis = str(coach.get("work_stasis", ""))
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
                work_stasis.ljust(6),
                "\033[92m" + "|" + "\033[0m",
                phone.ljust(15),
                "\033[92m" + "|" + "\033[0m",
                address
            )
            index += 1

        print("\033[92m" + "-" * 115 + "\033[0m")
        print("\n\n")