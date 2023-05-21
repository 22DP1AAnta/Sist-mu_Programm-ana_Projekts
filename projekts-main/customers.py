import json

class Customers:
    def __init__(self, name,surname, age, phone, address):
        self.name = name
        self.surname = surname
        self.age = age
        self.phone = phone
        self.address = address


    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Phone: {self.phone}, Address: {self.address}"
    
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

