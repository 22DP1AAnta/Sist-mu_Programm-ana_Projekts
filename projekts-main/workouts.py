import json
class Work_out:
    def __init__(self, exercise, sets, reps, description, weight):
        self.exercise = exercise
        self.sets = sets
        self.reps= reps
        self.weight = weight
        self.description = description

    def retur_nstr(self):
        return f"Exercise name: {self.exercise}, Working sets: {self.sets}, Working reps: {self.reps}, Workout weight: {self.weight}, Position: {self.description}"

    def append_data_to_workouts(self, file_path, exercise, sets, reps, description, weight):
        new_data = { 
            "exercise": exercise,
            "sets": sets,
            "reps": reps,
            "description": description,
            "weight": weight
        }
        try:
            with open(file_path, 'r', encoding="UTF-8") as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = []

        data.append(new_data)

        with open(file_path, 'w') as file:
            json.dump(data, file, indent=2)    
        