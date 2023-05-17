class Customers:  # definejam klasi
    def __init__(self, name, age, phone, address):
        self.name = name
        self.age = age
        self.phone = phone
        self.address = address

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Phone: {self.phone}, Address: {self.address}"