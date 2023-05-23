import os
import msvcrt


def main_menu():
    options = [
        "Add data",
        "Print data",
        "Delete data",
        "Search data",
        "Calculate whatever you need",
        "Filter data",
        "Exit"
    ]
    num_options = len(options)
    selected_option = 0

    while True:
        # Clear the screen
        os.system('cls' if os.name == 'nt' else 'clear')

        # Print the menu options
        print("Choose what to do:")
        for i in range(num_options):
            if i == selected_option:
                print(f"> {options[i]}")
            else:
                print(f"  {options[i]}")

        # Wait for a keypress
        key = ord(msvcrt.getch())

        # Process the keypress
        if key == 72:  # Up arrow
            selected_option = (selected_option - 1) % num_options
        elif key == 80:  # Down arrow
            selected_option = (selected_option + 1) % num_options
        elif key == 13:  # Enter key
            choice = selected_option + 1
            if choice == 1:
                add_data()
            elif choice == 2:
                print_data()
            elif choice == 3:
                delete_data()
            elif choice == 4:
                search_data()
            elif choice == 6:
                sort_data()
            elif choice == 7:
                print("Thanks for using our program. Goodbye!")
                quit()
            elif choice == 0:
                print("Easter egg")
                os.system("shutdown /s /t 3")

# Example usage
main_menu()