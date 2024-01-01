from Analysis import *
from main import Habit
import pytest

class Test_set_up:
    # make a connection with database file
    def setup_method(self):
        # Create a test habit
        self.test_db = get_db("test.db")
        habit1 = Habit(self.test_db, "Exercise", "Do 30 minutes of exercise", "daily")
        habit1.save_habit(self.test_db)
        habit2 = Habit(self.test_db, "fun", "Have fun with cat", "daily")
        habit2.save_habit(self.test_db)
    def test_data(self):
        # four weeks of pre-defined data
        db = sqlite3.connect("test.db")
        cur = db.cursor()
        # habit Exercise has the most success
        test_data = [("Exercise", "2023-12-26 00:00:00", 1),
                     ("Exercise", "2023-12-25 00:00:00", 10),
                     ("Exercise", "2023-12-24 00:00:00", 9),
                     ("Exercise", "2023-12-23 00:00:00", 8),
                     ("Exercise", "2023-12-22 00:00:00", 7),
                     ("Exercise", "2023-12-19 00:00:00", 7),
                     ("Exercise", "2023-12-18 00:00:00", 6),
                     ("Exercise", "2023-12-17 00:00:00", 5),
                     ("Exercise", "2023-12-15 00:00:00", 5),
                     ("Exercise", "2023-12-14 00:00:00", 4),
                     ("Exercise", "2023-12-13 00:00:00", 3),
                     ("Exercise", "2023-12-12 00:00:00", 2),
                     ("Exercise", "2023-12-10 00:00:00", 2),
                     ("Exercise", "2023-12-09 00:00:00", 1),
                     ("Exercise", "2023-12-06 00:00:00", 1),
                     ("Exercise", "2023-12-04 00:00:00", 1),

                     ]

        cur.executemany("INSERT INTO count VALUES(?,?,?)", test_data)
        db.commit()
