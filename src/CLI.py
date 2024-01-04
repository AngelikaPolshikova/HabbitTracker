import questionary
from questionary import *
from main import Habit
from Analysis import *
from colorama import Fore



def cli():
    # Establish a connection to the database
    #db = get_db(name="habit.db") #Use new database
    db = get_db(name="test.db") #Use testing database
    print("*" * 71)
    width = 20
    print("* Get ready to build better habits and track your progress! *".center(70))
    print("*" * 71)
    print("╔════════════════╗".center(width)) 
    print("║  Main Menu     ║".center(width))
    print("╠════════════════╣".center(width))


# Main loop to handle user interactions
    stop = False
    while not stop:
         # Display the main menu and get user choice
        choice = questionary.select("What do you want to do?",
                                    choices=["Create a habit",
                                             "Complete habit",
                                             "Analyse my habits",
                                             "Remove",
                                             "Exit"]).ask()

        if choice == "Create a habit":
             # Ask user for habit details and create a new habit
            name = questionary.text("What is the name of your habit?\n",
                                    validate=lambda text: True if len(text) > 0 else "Enter a name").ask()
            specification = questionary.text("what is the description of your habit?\n",
                                             validate=lambda text: True if len(
                                                 text) > 0 else "Enter a description").ask()
            period = questionary.select("What is the period of your habit? 'eg. daily, weekly or monthly'",
                                        choices=["daily", "weekly", "monthly"]).ask()
            habit = Habit(db, name, specification, period)
            habit.save_habit(db)

        elif choice == "Complete habit":
            name = questionary.text("Which habit do you want to complete").ask()
            counter = Habit(db, name, "NULL", "NULL")
            counter.complete_habit(db)
            all_habits = get_all_habits(db)


        elif choice == "Analyse my habits":
            # Display options for habit analysis
            analyse_choice = questionary.select("Which habit you want to analyse?",
                                                choices=["Analyse All Tracked Habits",
                                                         "Analyse Habit With Same Period",
                                                         "Analyse Your Longest Streak",
                                                         "Analyse Your Habit logs",
                                                         "Plot Your Habit"]).ask()

            if analyse_choice == "Analyse All Tracked Habits":
                show_all_habit(db)

            elif analyse_choice == "Analyse Habit With Same Period":
                period = questionary.select("Choose period", choices=["Daily", "Weekly", "Monthly"]).ask()

                if period == "Daily":
                    print("Your Daily Habits:-")
                    get_habit_with_period(db, period="daily")
                
                if period == "Monthly":
                    print("Your Monthly Habits:-")
                    get_habit_with_period(db, period="monthly") 

                else:
                    print("Your Weekly Habits:-")
                    get_habit_with_period(db, period="weekly")

            elif analyse_choice == "Analyse Your Longest Streak":
                long = questionary.select("choose one option", choices=["Longest Streak Of Specific Habit",
                                                                        "Longest Streak Of All Current Habits"]).ask()
                if long == "Longest Streak Of Specific Habit":
                    lon_streak = questionary.text(
                        "Enter the name of habit for which you want to see the longest streak",
                        validate=lambda text: True if len(text) > 0 else "Enter a value").ask()
                    get_longest_streak(db, lon_streak)
                else:
                    get_longest_of_all(db)
            elif analyse_choice == "Plot Your Habit":
                graph_habit_name = questionary.text(
                    "Enter the name of the habit for which you want to see the graph",
                    validate=lambda text: True if len(text) > 0 else "Enter a value"
                ).ask()

                # Call the plot_streak_graph function from the analysis file
                plot_streak_graph(db, graph_habit_name)
            else:
                # Ask user for habit name and show logs
                name = questionary.text("Enter the name of the habit for which you want to check logs\n",
                                        validate=lambda text: True if len(text) > 0 else "Enter a habit name").ask()
                show_logs(db, name)
        elif choice == "Remove":
            # Retrieve the list of all existing habits for removal
            all_habits = get_all_habits(db)
            if not all_habits:
                print(f"{Fore.RED}4.No habits available to remove.")
            else:
                # Present the list of habits as options and remove the selected habit
                name = questionary.select("Which habit you want to remove?", choices=all_habits).ask()
                habit = Habit(db, name, "NULL", "NULL")
                habit.delete_habit(db)
        else:
            print("Goodbye")
            # Exit the application
            stop = True


if __name__ == '__main__':
    # Run the command-line interface
    cli()
