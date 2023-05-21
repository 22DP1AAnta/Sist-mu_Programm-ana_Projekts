import json
class Work_out:
    def __init__(self, exercise, sets, reps, description, weight):
        self.exercise = exercise
        self.sets = sets
        self.reps= reps
        self.description = description
        self.weight = weight



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

    def print_data_of_workouts(self, file_path):
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
            "Exercise".ljust(20),
            "\033[92m" + "|" + "\033[0m",
            "Sets".ljust(6),
            "\033[92m" + "|" + "\033[0m",
            "Reps".ljust(6),
            "\033[92m" + "|" + "\033[0m",
            "Weight".ljust(8),
            "\033[92m" + "|" + "\033[0m",
            "Descriptions"
        )

        # Print data rows"|"
        index = 0
        for workout in data:
            exercise = workout.get("exercise", "")
            sets = str(workout.get("sets", ""))
            reps = str(workout.get("reps", ""))
            description = workout.get("description", "")
            weight = str(workout.get("weight", ""))

            print("\033[92m" + "-" * 115 + "\033[0m")  # augsa
            print(
                str(index).ljust(3),
                "\033[92m" + "|" + "\033[0m",
                exercise.ljust(20),
                "\033[92m" + "|" + "\033[0m",
                sets.ljust(6),
                "\033[92m" + "|" + "\033[0m",
                reps.ljust(6),
                "\033[92m" + "|" + "\033[0m",
                weight.ljust(8),
                "\033[92m" + "|" + "\033[0m",
                description
            )
            index += 1

        print("\033[92m" + "-" * 115 + "\033[0m")
        print("\n\n")
        