import questionary
from db import get_db
from HabitCounter import HabitCounter
from analyse import calculate_count
from questions import confirm_ready, select_action, counter_name, counter_description, analyze_counter, increment_counter

def start_screen():
    questionary.text("Welcome to Habit Tracker! Press Enter to start...").ask()

def cli():
    db = get_db()
    confirm_ready()
    
    stop = False
    while not stop:
        start_screen()

        choice = select_action()

        if choice == "Create":
            name = counter_name()
            desc = counter_description()
            counter = HabitCounter(name, desc)  # Fix: Use HabitCounter instead of Counter
            counter.store(db)
        elif choice == "Increment":
            name = increment_counter()
            try:
                counter = HabitCounter(name, "no desc")  # Fix: Use HabitCounter instead of Counter
                counter.increment()
                counter.add_event(db)
            except ValueError:
                print(f"Error: Counter '{name}' does not exist.")
        elif choice == "Analyze":
            name = analyze_counter()
            try:
                count = calculate_count(db, name)
                print(f"{name} has been incremented {count} times")
            except ValueError:
                print(f"Error: Counter '{name}' does not exist.")
        elif choice == "Exit":
            print("Bye!")
            stop = True
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == '__main__':
    cli()
