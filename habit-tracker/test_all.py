from main import *
from habit_database import *
from Analysis import *
import pytest

class Test_set_up:
    # make a connection with database file
    def setup_method(self):
        # Create a test habit
        self.db = get_db("test.db")
        habit = Habit(self.db, "Exercise", "Do 30 minutes of exercise", "daily")
        habit.save_habit(self.db)
        habit = Habit(self.db, "Reading ", "Read a book", "daily")
        habit.save_habit(self.db)
        habit = Habit(self.db, "Coding", "Code in Python", "weekly")
        habit.save_habit(self.db)
        habit = Habit(self.db, "Meditation", "1 Hour of Meditation", "weekly")
        habit.save_habit(self.db)
        habit = Habit(self.db, "Writing", "Write my feelings", "daily")
        habit.save_habit(self.db)
        habit = Habit(self.db, "Deep Clean", "Full cleaning of the house", "monthly")
        habit.save_habit(self.db)
    def test_data(self):
        # four weeks of pre-defined data
        db = sqlite3.connect("test.db")
        cur = db.cursor()
        # habit Exercise has the most success
        test_data = [
                    ("Exercise", "2023-12-28 00:00:00", 9),
                    ("Exercise", "2023-12-27 00:00:00", 8),
                    ("Exercise", "2023-12-26 00:00:00", 7),
                    ("Exercise", "2023-12-25 00:00:00", 6),
                    ("Exercise", "2023-12-24 00:00:00", 5),
                    ("Exercise", "2023-12-23 00:00:00", 4),
                    ("Exercise", "2023-12-22 00:00:00", 3),
                    ("Exercise", "2023-12-21 00:00:00", 2),
                    ("Exercise", "2023-12-20 00:00:00", 1),
                    ("Exercise", "2023-12-17 00:00:00", 1),
                    ("Exercise", "2023-12-15 00:00:00", 4),
                    ("Exercise", "2023-12-14 00:00:00", 3),
                    ("Exercise", "2023-12-13 00:00:00", 2),
                    ("Exercise", "2023-12-12 00:00:00", 1),
                    ("Exercise", "2023-12-10 00:00:00", 2),
                    ("Exercise", "2023-12-09 00:00:00", 1),
                    ("Exercise", "2023-12-06 00:00:00", 1),
                    ("Exercise", "2023-12-04 00:00:00", 4),
                    ("Exercise", "2023-12-03 00:00:00", 3),
                    ("Exercise", "2023-12-02 00:00:00", 2),
                    ("Exercise", "2023-12-01 00:00:00", 1),
                    

                    ("Reading", "2023-12-25 00:00:00", 2),
                    ("Reading", "2023-12-24 00:00:00", 1),
                    ("Reading", "2023-12-20 00:00:00", 1),
                    ("Reading", "2023-12-17 00:00:00", 3),
                    ("Reading", "2023-12-16 00:00:00", 2),
                    ("Reading", "2023-12-15 00:00:00", 1),
                    ("Reading", "2023-12-13 00:00:00", 1),
                    ("Reading", "2023-12-11 00:00:00", 2),
                    ("Reading", "2023-12-09 00:00:00", 1),
                    ("Reading", "2023-12-06 00:00:00", 1),
                    ("Reading", "2023-12-04 00:00:00", 4),
                    ("Reading", "2023-12-03 00:00:00", 3),
                    ("Reading", "2023-12-02 00:00:00", 2),
                    ("Reading", "2023-12-01 00:00:00", 1),


                    ("Coding", "2023-12-29 00:00:00", 5),
                    ("Coding", "2023-12-21 00:00:00", 4),
                    ("Coding", "2023-12-14 00:00:00", 3),
                    ("Coding", "2023-12-08 00:00:00", 2),
                    ("Coding", "2023-12-01 00:00:00", 1),

                    ("Meditation", "2023-12-21 00:00:00", 1),
                    ("Meditation", "2023-12-02 00:00:00", 1),



                    ("Writing", "2023-12-28 00:00:00", 1),
                    ("Writing", "2023-12-17 00:00:00", 1),
                    ("Writing", "2023-12-08 00:00:00", 1),
                    ("Writing", "2023-12-06 00:00:00", 2),
                    ("Writing", "2023-12-05 00:00:00", 1),
                    ("Writing", "2023-12-01 00:00:00", 1),


                    ("Deep Clean", "2023-12-01 00:00:00", 1),
                    ("Deep Clean", "2023-11-05 00:00:00", 1),
                    ]

        cur.executemany("INSERT INTO count VALUES(?,?,?)", test_data)
        db.commit()

        # Plots streak graph for a habit with valid data.

    # Plot graph with valid habit name and existing data
    def test_savehabit(self):
        # Test saving a habit to the test database
        test_habit = Habit(self.db, "test_save","testing_save","weekly")
        
        test_habit.save_habit(self.db)
        # Assert that the habit is in the database
        assert verification(self.db, "test_save")
        # Deletes a habit from the database when given a valid habit name.
    def test_delete_valid_habit_name(self):
        # Initialize habit object
        habit = Habit(self.db, "test_delete","testing_delete","weekly")
    
        # Save habit in the database
        habit.save_habit(self.db)
    
        # Delete habit from the database
        habit.delete_habit(self.db)
    
        # Check if habit is deleted
        assert habit.name is None
        assert habit.task_specification is None
        assert habit.period is None
        assert habit.streak == 0


    
    def test_complete(self):
        # complete habit
        habit1 = Habit(self.db, "Exercise", "Do 30 minutes of exercise", "daily")
        habit1.complete_habit(self.db)

        assert habit1.streak == 1

    # Successfully add a new habit to the database with default checked_at and streak values
    def test_add_new_habit_default_values(self):
        check_habit(self.db, "check")  # Add a new habit with default values
        cur = self.db.cursor()
        cur.execute("SELECT * FROM count WHERE name=?", ("check",))
        result = cur.fetchone()
        assert result[0] == "check"  # Check if the habit name is correct
        assert result[1] is not None  # Check if the checked_at value is not None
        assert result[2] == 0  # Check if the streak value is 0
        self.db.close()  # Close the test database

    
    def test_update_habit(self):
        update_habit(self.db, "Writing", 10)
        assert get_streak(self.db, "Writing") == 10
    
    def test_longest_streak(self):
        result = get_longest_streak(self.db, "Exercise")
        assert result == 9


    def test_longest_streak_all(self):
        result = longest_of_all(self.db)
        assert result == 9 

 

    def test_graph_streak(self):
        plot_streak_graph(self.db, "Exercise")
        # Assert that the graph is displayed correctly
        # (no assertion on the actual graph content is made)
        figure_number = plt.gcf().number
        assert plt.fignum_exists(figure_number), f"Figure {figure_number} does not exist."
        plt.close(figure_number)
    
    # Streak is initially 0, increase method should increase it to 1.
    def test_streak_initially_0(self):
        habit = Habit(self.db,  "test_streak", "streak", "daily")
        habit.increase()
        assert habit.streak == 1

    # Streak is initially 1, increase method should increase it to 2.
    def test_streak_initially_1(self):
        habit = Habit(self.db,  "test_streak", "streak", "daily")
        habit.streak = 1
        habit.increase()
        assert habit.streak == 2

    # Streak is initially 10, increase method should increase it to 11.
    def test_streak_initially_10(self):
        habit = Habit(self.db,  "test_streak", "streak", "daily")
        habit.streak = 10
        habit.increase()
        assert habit.streak == 11

    # Habit name is None, increase method should not increase the streak.
    def test_habit_name_none(self):
        habit = Habit(self.db, None, "streak", "daily")
        habit.streak = 5
        habit.increase()
        assert habit.streak == 5

    # Habit name is an empty string, increase method should not increase the streak.
    def test_habit_name_empty(self):
        habit = Habit(self.db, "", "streak", "daily")
        habit.streak = 7
        habit.increase()
        assert habit.streak == 7

        # If last checked date is more than a day ago, decrement streak and update db.
    def test_more_than_a_day_ago(self):
        # Set up a habit with a last checked date more than a day ago
        habit = Habit(self.db, "Exercise", "Do 30 minutes of exercise", "daily")
        habit.streak = 5
        last_check = datetime.now() - timedelta(days=2)
        add_habit(self.db, "Exercise", "Do 30 minutes of exercise", "daily")
        habit.add_event(self.db)
        update_last_checked_date(self.db, "Exercise", last_check.strftime("%Y-%m-%d %H:%M:%S"))
    
        # Invoke the daily_habit method
        habit.daily_habit(self.db)
        
        # Assert that the streak is decremented
        assert get_streak(self.db, "Exercise") == 1

    def test_more_than_a_week_ago(self):
        # Set up a habit with a last checked date more than a day ago
        habit = Habit(self.db, "Meditation", "1 Hour of Meditation", "weekly")
        habit.save_habit(self.db)
        habit.streak = 5
        last_check = datetime.now() - timedelta(days=8)
        add_habit(self.db, "Meditation", "1 Hour of Meditation", "weekly")
        habit.add_event(self.db)
        update_last_checked_date(self.db, "Exercise", last_check.strftime("%Y-%m-%d %H:%M:%S"))
    
        # Invoke the daily_habit method
        habit.weekly_habit(self.db)
        
        # Assert that the streak is decremented
        assert get_streak(self.db, "Exercise") == 1


    def test_more_than_a_week_ago(self):
        # Set up a habit with a last checked date more than a day ago
        habit = Habit(self.db, "Meditation", "1 Hour of Meditation", "weekly")
        habit.save_habit(self.db)
        habit.streak = 5
        last_check = datetime.now() - timedelta(days=8)
        add_habit(self.db, "Meditation", "1 Hour of Meditation", "weekly")
        habit.add_event(self.db)
        update_last_checked_date(self.db, "Exercise", last_check.strftime("%Y-%m-%d %H:%M:%S"))
    
        # Invoke the daily_habit method
        habit.weekly_habit(self.db)
        
        # Assert that the streak is decremented
        assert get_streak(self.db, "Exercise") == 1


    def test_more_than_a_month_ago(self):
        # Set up a habit with a last checked date more than a day ago
        habit = Habit(self.db, "Deep Clean", "Full cleaning of the house", "monthly")
        habit.save_habit(self.db)
        habit.streak = 5
        last_check = datetime.now() - timedelta(days=31)
        add_habit(self.db, "Deep Clean", "Full cleaning of the house", "monthly")
        habit.add_event(self.db)
        update_last_checked_date(self.db, "Exercise", last_check.strftime("%Y-%m-%d %H:%M:%S"))
    
        # Invoke the daily_habit method
        habit.weekly_habit(self.db)
        
        # Assert that the streak is decremented
        assert get_streak(self.db, "Exercise") == 1   
def teardown_method(self):
    import os
    pass




    
    