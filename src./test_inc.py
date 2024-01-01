from Analysis import *
from main import Habit
import pytest

class TestIncrease:
    def setup_method(self):
        # Create a test habit
        self.test_db = get_db("test.db")
        habit = Habit(self.test_db, "Exercise", "Do 30 minutes of exercise", "daily")
        habit.save_habit(self.test_db)
    # Streak is initially 0, increase method should increase it to 1.
    def test_streak_initially_0(self):
        habit = Habit(self.test_db,  "Exercise", "Do 30 minutes of exercise", "daily")
        habit.increase()
        assert habit.streak == 1

    # Streak is initially 1, increase method should increase it to 2.
    def test_streak_initially_1(self):
        habit = Habit(self.test_db,  "Exercise", "Do 30 minutes of exercise", "daily")
        habit.streak = 1
        habit.increase()
        assert habit.streak == 2

    # Streak is initially 10, increase method should increase it to 11.
    def test_streak_initially_10(self):
        habit = Habit(self.test_db,  "Exercise", "Do 30 minutes of exercise", "daily")
        habit.streak = 10
        habit.increase()
        assert habit.streak == 11

    # Habit name is None, increase method should not increase the streak.
    def test_habit_name_none(self):
        habit = Habit(self.test_db, None, "Do 30 minutes of exercise", "daily")
        habit.streak = 5
        habit.increase()
        assert habit.streak == 5

    # Habit name is an empty string, increase method should not increase the streak.
    def test_habit_name_empty(self):
        habit = Habit(self.test_db, "", "Do 30 minutes of exercise", "daily")
        habit.streak = 7
        habit.increase()
        assert habit.streak == 7
    # def test_addEvent(self):
    #     db = get_db("test_db")
    #     habit = Habit(db, "Exercise", "Do 30 minutes of cardio", "daily")
    #     habit.streak = 0
    #     habit.add_event(db)
    #     assert habit.streak == 1

    # Habit name is not in the database, increase method should not increase the streak.
    # def test_habit_name_not_in_database(self):
    #     habit = Habit(self.test_db, "nonexistent_habit", "task_specification", "period")
    #     habit.streak = 3
    #     habit.increase()
    #     assert habit.streak == 3
    # def test_add_event(self):
    #     # Test adding an event to the habit
    #     with patch("habit_database.add_event") as mock_add_event:
    #         self.test_habit.add_event(test_db)
    #     # Assert that add_event was called with the correct parameters

    # # Add more test cases for other methods...
        # saves a habit in the database when valid inputs are provided
    # def test_save_habit_valid_inputs(self, mocker):
    #     # Arrange
    #     db_mock = mocker.Mock()
    #     habit = Habit(db_mock, "Exercise", "Do 30 minutes of cardio", "daily")
    
    #     # Act
    #     habit.save_habit(db_mock)
    
    #     # Assert
    #     assert db_mock.add_habit.assert_called_once_with("Exercise", "Do 30 minutes of cardio", "daily")
def teardown_method(self):
    import os
    pass

