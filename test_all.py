from Analysis import *
from main import Habit

# import unittest
# from unittest.mock import patch
# from habit_database import Habit

class TestHabitTracker:
    def setup_method(self):
        # Create a test habit
        self.test_db = get_db("test.db")
        # self.test_habit = add_habit(self.test_db, "test","testing","daily")

    def test_savehabit(self):
        # Test saving a habit to the test database
        test_habit = Habit(self.test_db, "test_save","testing_save","weekly")
        
        test_habit.save_habit(self.test_db)
        # Assert that the habit is in the database
        assert verification(self.test_db, "test_save")
        # Deletes a habit from the database when given a valid habit name.
    def test_delete_valid_habit_name(self):
        # Initialize habit object
        db = get_db("test_db")
        habit = Habit(db, "Exercise", "Do 30 minutes of exercise", "daily")
    
        # Save habit in the database
        habit.save_habit(db)
    
        # Delete habit from the database
        habit.delete_habit(db)
    
        # Check if habit is deleted
        assert habit.name is None
        assert habit.task_specification is None
        assert habit.period is None
        assert habit.streak == 0

        # increases the streak counter by 1
    
        



