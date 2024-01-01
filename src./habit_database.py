import datetime
import sqlite3
from datetime import *

# Function to create and maintain connection with the database
def get_db(name="test.db"):
    db = sqlite3.connect(name)
    create_tables(db)
    return db

# Function that creates tables into the database
def create_tables(db):
    cur = db.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS Habit (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    task_specification TEXT,
    period TEXT,
    created_at INTEGER,
    streak INTEGER ) """)

    cur.execute("""CREATE TABLE IF NOT EXISTS count (
    name TEXT,
    Checked_at INTEGER,
    streak INTEGER,
    FOREIGN KEY (name) REFERENCES Habit(name))""")

    db.commit()

# Return a list of habits with all information
def show_habits(db):
    cur = db.cursor()
    cur.execute("SELECT * FROM Habit ")
    return cur.fetchall() 

# Add a new habit into the database
def add_habit(db, name, task_specification, period, streak=0):
    cur = db.cursor()
    cur.execute("SELECT name FROM Habit WHERE name=?", (name,))
    result = cur.fetchone()
    if result:
        print("Habit already exists")
    else:
        created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cur.execute("INSERT INTO Habit VALUES (NULL,?,?,?,?,?)",
                    (name, task_specification, period, created_at, streak))
        db.commit()
        print("Habit created successfully")

# Check a specific habit
def check_habit(db, name, checked_at=None, streak=0):
    cur = db.cursor()
    if checked_at is None:
        checked_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cur.execute("INSERT INTO count VALUES(?,?,?)", (name, checked_at, streak))
    print("Habit completed successfully")
    print("Name :-", name)
    print("checked_at :-", checked_at)
    db.commit()

# Update the value of streak in the habit table
def update_habit(db, name, streak):
    cur = db.cursor()
    cur.execute("UPDATE Habit SET streak=? WHERE name=?", (streak, name))
    db.commit()
    
# Update the value of streak in the count table
def update_count(db, name, streak):
    cur = db.cursor()
    cur.execute("UPDATE count SET streak=? WHERE name=?", (streak, name))
    db.commit()

# Verify habit from the database
def verification(db, name):
    cur = db.cursor()
    cur.execute("SELECT name FROM Habit WHERE name=?", (name,))
    return cur.fetchone()

# Return the last completed date
def get_last_checked_date(db, name):
    cur = db.cursor()
    cur.execute("SELECT checked_at FROM count WHERE name=?", (name,))
    return cur.fetchall()

def habit_exists(db, name):
    cur = db.cursor()
    cur.execute("SELECT COUNT(*) FROM Habit WHERE name=?", (name,))
    habit_count = cur.fetchone()[0]
    print(habit_count)
    return habit_count > 0

# Return the current streak from the database
def get_streak(db, name):
    if not habit_exists(db, name):
        # If the habit doesn't exist, return None or 0, depending on your requirements
        return None
    
    cur = db.cursor()
    cur.execute("SELECT streak FROM Habit WHERE name=?", (name,))
    streak_count = cur.fetchall()
    
    # if not streak_count:
    #     return 0  # or handle the case where no rows are returned
    return streak_count[0][0]
def get_streak_from_date(db, name, date_str):
    # date = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    date = date_str
    cur = db.cursor()
    cur.execute("SELECT streak FROM count WHERE name=? AND Checked_at=?", (name, date))
    result = cur.fetchone()
    return result[0] if result else 0

# Return the longest streak from the count table
def get_longest_streak_from_logs(db, name):
    cur = db.cursor()
    cur.execute("SELECT streak FROM count WHERE name=?", (name,))
    str_count = cur.fetchall()
    return str_count[0][0]


# Select the periodicity of a specified habit
def get_period(db, name):
    cur = db.cursor()
    cur.execute("SELECT period FROM Habit WHERE name=?", (name,))
    return cur.fetchall()[0][0]

# Return a list of habits according to their period
def habit_with_period(db, period):
    if period == "daily":
        cur = db.cursor()
        cur.execute("SELECT * FROM Habit WHERE period=?", (period,))
        return cur.fetchall()
    if period == "monthly":
        cur = db.cursor("SELECT * FROM Habit WHERE period=?", (period,))
        return cur.fetchall()
        cur.execute("")
    else:
        cur = db.cursor()
        cur.execute("SELECT * FROM Habit WHERE period=?", (period,))
        return cur.fetchall()

# Select the max streak from all defined habits
def longest_of_all(db):
    cur = db.cursor()
    cur.execute("SELECT MAX(streak) FROM count")
    return cur.fetchall()[0][0]

# Return a list of all habit checked_at dates
def display_habit_logs(db, name):
    result = verification(db, name)
    if result:
        cur = db.cursor()
        cur.execute('SELECT checked_at FROM count WHERE name=?', (name,))
        long = cur.fetchone()
        if long:
            cur.execute("SELECT checked_at FROM count WHERE name=?", (name,))
            log = cur.fetchall()
            print(f"Your logs for {name}")
            print(f"checked at \n {log}")
        else:
            print("No Logs For This Habit Yet")
    else:
        print("No logs for this habit exist in our database")

# Delete the specified habit from the database
def remove_habit(db, name):
    cur = db.cursor()
    cur.execute("DELETE FROM Habit WHERE name=?", (name,))
    cur.execute("DELETE FROM count WHERE name=?", (name,))
    db.commit()
    print("Habit removed successfully")
