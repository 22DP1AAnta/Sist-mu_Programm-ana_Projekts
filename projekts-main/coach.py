import json
class Coach:  # definejam klasi
    def __init__(self, name, age, phone, address, work_stasis):
        self.name = name
        self.age = age
        self.phone = phone
        self.address = address
        self.work_stasis = work_stasis

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Phone: {self.phone}, Address: {self.address}, Work Stasis: {self.work_stasis}"
    def append_data_to_coach(self, file_path, name, age, phone, address, work_stasis):
        new_data = { 
            "name": name,
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