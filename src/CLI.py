import questionary
from questionary import *
from main import Habit
from Analytic import *


def cli():
    db = get_db()

    print("=".center(71, "="))
    print(" Welcome To The Habit Tracker App ".center(70, "-"))
    print("=".center(71, "="))

    stop = False
    while not stop:
        choice = questionary.select("What do you want to do?",
                                    choices=["Create a habit",
                                             "Check-off a habit",
                                             "Analyse my habits",
                                             "Remove",
                                             "Exit"]).ask()

        if choice == "Create a habit":
            name = questionary.text("What is the name of your habit?\n",
                                    validate=lambda text: True if len(text) > 0 else "Enter a name").ask()
            specification = questionary.text("what is the description of your habit?\n",
                                             validate=lambda text: True if len(
                                                 text) > 0 else "Enter a description").ask()
            period = questionary.select("What is the period of your habit? 'eg. daily or weekly'",
                                        choices=["daily", "weekly"]).ask()
            habit = Habit(db, name, specification, period)
            habit.save_habit(db)

        elif choice == "Check-off a habit":
            name = questionary.text("Which habit you want to check-off?").ask()
            counter = Habit(db, name, "NULL", "NULL")
            counter.complete_habit(db)

        elif choice == "Analyse my habits":
            analyse_choice = questionary.select("Which habit you want to analyse?",
                                                choices=["Analyse All Tracked Habits",
                                                         "Analyse Habit With Same Period",
                                                         "Analyse Your Longest Streak",
                                                         "Analyse Your Habit logs"]).ask()

            if analyse_choice == "Analyse All Tracked Habits":
                show_all_habit(db)

            elif analyse_choice == "Analyse Habit With Same Period":
                period = questionary.select("choose period", choices=["Daily", "Weekly"]).ask()

                if period == "Daily":
                    print("Your Daily Habits:-")
                    get_habit_with_period(db, period="daily")

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
            else:
                name = questionary.text("Enter the name of the habit for which you want to check logs\n",
                                        validate=lambda text: True if len(text) > 0 else "Enter a habit name").ask()
                show_logs(db, name)
        elif choice == "Remove":
            name = questionary.text("Enter the name of the habit you want to remove\n",
                                    validate=lambda text: True if len(text) > 0 else "Enter a habit name").ask()
            habit = Habit(db, name, "NULL", "NULL")
            habit.delete_habit(db)
        else:
            print("Goodbye")

            stop = True


if __name__ == '__main__':
    cli()
