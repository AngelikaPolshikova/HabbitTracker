#import dependencies
from habit import Habit
import json
from datetime import datetime, timedelta


class HabitCounter:
    def __init__(self, name, description):
         self.name = name
         self.description = description
         self.habits = []

    def add_habit(self, habit):
        self.habits.append(habit)

    def remove_habit(self, habit_name):
        self.habits = [habit for habit in self.habits if habit.name != habit_name]

    def complete_habit(self, habit_name, date=None):
        for habit in self.habits:
            if habit.name == habit_name:
                habit.mark_completed(date)
                break

    def calculate_streak(self):
        if not self.completed_dates:
            return 0

        streak = 0
        today = datetime.today().date()

        while today in self.completed_dates:
            streak += 1
            today -= timedelta(days=1)

        return streak

    def list_habits_by_frequency(self):
        habits_by_frequency = {}
        for habit in self.habits:
            if habit.frequency not in habits_by_frequency:
                habits_by_frequency[habit.frequency] = []
            habits_by_frequency[habit.frequency].append(habit.to_dict())
        return habits_by_frequency

    def view_streaks(self):
        streaks = {}
        for habit in self.habits:
            streaks[habit.name] = habit.calculate_streak()
        return streaks

    def find_weakest_strongest_habit(self):
        if not self.habits:
            return None, None

        weakest_habit = min(self.habits, key=lambda habit: habit.calculate_streak())
        strongest_habit = max(self.habits, key=lambda habit: habit.calculate_streak())

        return weakest_habit.name, strongest_habit.name

    def save_to_file(self):
        with open(filename, 'w') as file:
            data = {
                "name": self.name,
                "description": self.description,
                "habits": [habit.to_dict() for habit in self.habits]
            }
            json.dump(data, file)

    def load_from_file(self):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                self.name = data.get("name", "")
                self.description = data.get("description", "")
                self.habits = [Habit.from_dict(habit_data) for habit_data in data.get("habits", [])]
        except FileNotFoundError:
            print(f"Error: File '{JSON_FILE_PATH}' not found.")
        except json.JSONDecodeError:
            print(f"Error: Unable to decode JSON in file '{JSON_FILE_PATH}'. File may be improperly formatted.")
    
    def store(self, filename):
        self.save_to_file(filename)
