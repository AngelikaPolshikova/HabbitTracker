import json
from datetime import datetime, timedelta

class Habit:
    def __init__(self, name, description, frequency, creation_time):
        self.name = name
        self.description = description
        self.completed_dates = []
        self.frequency = frequency
        self.creation_time = creation_time

    def mark_completed(self, date=None):
      if date is None:
        date = datetime.today().date()
      if date not in self.completed_dates:
        self.completed_dates.append(date)

    def remove_completed(self, date):
        # If user needs to UNDO
        if date in self.completed:
            self.completed.remove(date)

    def to_json(self):
        # Convert the habit object to a JSON string
        return json.dumps({
            'name': self.name,
            'description': self.description,
            'frequency': self.frequency,  # Include 'frequency' key
            'creation_time': self.creation_time.isoformat(),
            'completed_dates': [date.isoformat() for date in self.completed_dates]
        })

    @classmethod
    def from_json(cls, json_string):
        # Create a Habit object from a JSON string
        data = json.loads(json_string)
        habit = cls(data['name'], data['description'], data['frequency'], datetime.fromisoformat(data['creation_time']))
        habit.completed_dates = [datetime.fromisoformat(date_str).date() for date_str in data['completed_dates']]
        return habit

# application code to test JSON serialization and deserialization
habit1 = Habit("Exercise", "Run for 30 mins", "daily", datetime.today().date())
for i in range(3):
    habit1.mark_completed(datetime.today().date() - timedelta(days=i))

json_data = habit1.to_json()
print("JSON Representation:")
print(json_data)

print("\nRestored from JSON:")
restored_habit = Habit.from_json(json_data)
print(restored_habit)


def test_habit_creation_and_retrieval():
    # Create a habit and mark completions
    habit = Habit(name="Exercise", description="Run for 30 mins", frequency="daily", creation_time=datetime.today().date())

    for i in range(3):
        habit.mark_completed(datetime.today().date() - timedelta(days=i))

    assert habit.name == "Exercise"
    assert habit.description == "Run for 30 mins"
    assert habit.calculate_streak() == 3

    json_data = habit.to_json()

    fetched_habit = Habit.from_json(json_data)
    assert fetched_habit is not None
    assert fetched_habit.name == "Exercise"
    assert fetched_habit.description == "Run for 30 mins"
    assert fetched_habit.calculate_streak() == 3

def to_dict(self):
        return {
            'name': self.name,
            'description': self.description,
            'frequency': self.frequency,
            'creation_time': self.creation_time.isoformat(),
            'completed_dates': [date.isoformat() for date in self.completed_dates]
        }

@classmethod

def from_dict(cls, data):
        habit = cls(data['name'], data['description'], data['frequency'], datetime.fromisoformat(data['creation_time']))
        habit.completed_dates = [datetime.fromisoformat(date_str).date() for date_str in data['completed_dates']]
        return habit    
