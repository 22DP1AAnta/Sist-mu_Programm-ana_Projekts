class Work_out:
    def __init__(self, exercise, sets, reps, description, weight):
        self.exercise = exercise
        self.sets = sets
        self.reps= reps
        self.weight = weight
        self.description = description

    def retur_nstr(self):
        return f"Name: {self.exercise}, Age: {self.sets}, Phone: {self.reps}, Address: {self.weight}, Position: {self.description}"

    def add_data(self):
        