class Coach:  # definejam klasi
    def __init__(self, name, age, phone, address, work_stasis):
        self.name = name
        self.age = age
        self.phone = phone
        self.address = address
        self.work_stasis = work_stasis

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Phone: {self.phone}, Address: {self.address}, Work Stasis: {self.work_stasis}"