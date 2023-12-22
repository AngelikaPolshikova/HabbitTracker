import questionary
from db import get_db
from HabitCounter import HabitCounter
from analyse import calculate_count


def cli():
    db = get_db()
    questionary.confirm("Are you ready?").ask()
    counter = HabitCounter("MyCounter", "Description") #instantiating
    JSON_FILE_PATH = "habit_data.json"


    stop = False
    while not stop:
        choice = questionary.select(
            "What do you want to do?",
            choices=[
                "Create a new habit",
                "Complete the existing habit",
                "Analyze my habits",
                "Save and Exit"
            ]
        ).ask()
        if choice == "Save and Exit":
            filename = questionary.text("Enter the filename to save your data:").ask()
            counter.store(filename)  # Passing the filename to the store method
            print(f"Data saved to {filename}. Bye!")
            stop = True

        if choice == "Create a new habit":
            name = questionary.text("What's the name of your habit?").ask()
            desc = questionary.text("Enter a description for your habit:").ask()
            counter.add_habit(Habit(name, desc))  # Using the add_habit method
        elif choice == "Complete the existing habit":
            name = questionary.text("Which habit do you want to perform?").ask()
            try:
                # Using the existing counter instance
                counter.complete_habit(name)
                counter.add_event(db)  # Assuming add_event method exists
            except ValueError:
                print(f"Error: Habit '{name}' does not exist.")
        elif choice == "Analyze my habits":
            name = questionary.text("Which habit do you want to analyze?").ask()
            try:
                count = calculate_count(db, name)
                print(f"{name} has been performed {count} times")
            except ValueError:
                print(f"Error: Habit '{name}' does not exist.")
        elif choice == "Exit":  # Corrected option
            filename = questionary.text("Enter the filename to save your data:").ask()
            counter.save_to_file(filename)
            print(f"Data saved to {filename}. Bye!")
            stop = True
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == '__main__':
    cli()
