from database import *

def get_all_habits(db):
    
    # Retrieve a list of all habit names from the database.
    # Creates a connection with the db
    # List of habit names
   
    cursor = db.cursor()
    cursor.execute("SELECT name FROM Habit")
    habits = [row[0] for row in cursor.fetchall()]
    return habits if habits else None

def show_all_habit(db):
    
    # Gets information about all habits
    # Creates connection with db
    # Returns list of all habit with their complete info
    
    habit_list = show_habits(db)
    for row in habit_list:
        print("Habit Name: ", row[1])
        print("Specification: ", row[2])
        print("Period: ", row[3])
        print("Creation: ", row[4])
        print("Current streak:", row[5])
        print("\n")

def show_logs(db, name):
    #Returns a list of dates
    #Maintains connection with db
    #Name of the specified habit
    #Returns a list of all complete dates
    
    result = display_habit_logs(db, name)
    
def get_habit_with_period(db, period):
    #Gets information from the database and returns to the user
    #Creates a connection with the database
    #param period: Timespan of a habit 
    #Returns a list of habits with selected period/timpespan
    list = habit_with_period(db, period)
    for row in list:
        print(f"Name: {row[1]}")
        print(f"created_at: {row[4]}")
        print(f"Current streak: {row[5]}")
        print("\n")

def get_longest_streak(db, name):
    #Chooses among existing streaks and returns the longest one
    #Maintains connection to the db
    #Name of the specified habit
    #Returns Longest streak
    
    verify = verification(db, name)
    if verify:
        cur = db.cursor()
        cur.execute("SELECT name FROM count where name=?", (name,))
        result = cur.fetchone()
        if result:
            longest = get_longest_streak_from_logs(db, name)
            print(f"Longest streak for habit '{name}' is \n {longest} days ")
            return longest
        else:
            print(f"Longest streak for habit '{name}' is \n {0} days")
    else:
        print("Enter A Valid Habit Name")

def get_longest_of_all(db):
    #From the database, returns the longest run streak of all habit
    #Maintains connection with the db
    #Return the longest streak from all defined habits

    long = longest_of_all(db)
    print(f"Longest streak for all defined habits is \n {long} days ")

