from habit_database import *
from datetime import *
from colorama import Fore

class Habit:
    def __init__(self, db, name: str, task_specification: str, period):
        #Creates a new habit instance with a specified name name, description and time period.
        self.db = db
        self.name = name
        self.task_specification = task_specification
        self.period = period
        self.streak = 0
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        return f"{self.name}:{self.task_specification}:{self.period}"

    def save_habit(self, db):
        #Saves a habit in the db.
        add_habit(self.db, self.name, self.task_specification, self.period)

    def delete_habit(self, db):
        #Deletes habit from db.
        name = verification(self.db, self.name)
        if name:
            remove_habit(self.db, self.name)
            self.name = None
            self.task_specification = None
            self.period = None
            self.streak = 0
        else:
            print(f"{Fore.RED}4.Enter a valid habit name")

    def increase(self):
        #Increase streak by 1.

        if not self.name:
        # If the habit name is None, do not increase the streak
            return
        
        
        if self.streak is None:
            self.streak = get_streak(self.db, self.name)
        self.streak += 1

    def reset(self):
        #Resets streak to 1.
        self.streak = 1

    def add_event(self, db):
        #Increases counter by 1.
        self.increase()
        check_habit(self.db, self.name)
        update_habit(self.db, self.name, self.streak)
        self.longest(self.db)

    def decrement_event(self, db):
        #Resets counter to 1 if streak was broken.
        self.streak = 1
        check_habit(self.db, self.name)
        update_habit(self.db, self.name, self.streak)
        self.longest(self.db)

    def daily_habit(self, db):
        #Completes daily habit and adds it to the db.
        today = date.today()
        last = get_last_checked_date(self.db, self.name)
        last1 = [i[0] for i in last]
        if len(last1) < 0:
            self.add_event(self)
        else:
            ls = last1[-1]
            last_check = datetime.strptime(ls, "%Y-%m-%d %H:%M:%S").date()
            if today - last_check < timedelta(days=1):
                print(f"{Fore.RED}You already completed this habit today!")
            elif today - last_check < timedelta(days=2):
                self.add_event(self)
            else:
                self.decrement_event(db)

    def weekly_habit(self, db):
        #Completes weekly habit and adds it to db.
        today = date.today()
        last = get_last_checked_date(self.db, self.name)
        last1 = [i[0] for i in last]
        if len(last1) < 0:
            self.add_event(self)
        else:
            ls = last1[-1]
            last_check = datetime.strptime(ls, "%Y-%m-%d %H:%M:%S").date()
            if today - last_check < timedelta(days=7):
                print(f"{Fore.RED}You already completed current habit this week!")
            elif today - last_check < timedelta(days=8):
                self.add_event(self)
            else:
                self.decrement_event(db)
    
    def monthly_habit(self, db):
        #Complete monthly habit and add it to db.
        today = date.today()
        last = get_last_checked_date(self.db, self.name)
        last1 = [i[0] for i in last]
        if len(last1) < 0:
            self.add_event(self)
        else:
            ls = last1[-1]
            last_check = datetime.strptime(ls, "%Y-%m-%d %H:%M:%S").date()
            if today - last_check < timedelta(days=30):
                print(f"{Fore.RED}You already completed current habit this month!")
            elif today - last_check < timedelta(days=31):
                self.add_event(self)
            else:
                self.decrement_event(db)

    def complete_habit(self, db):
       #Completes habit in the db.
       name = verification(self.db, self.name)
    
       if name:
        streak = get_streak(self.db, self.name)
        period = get_period(self.db, self.name)
        per = period
        
        if per == 'daily':
            if streak == 0:
                self.add_event(self)
            else:
                self.daily_habit(db)
        
        elif per == 'monthly':
            if streak == 0:
                self.add_event(self)
            else:
                self.monthly_habit(db)
        
        else:
            if streak == 0:
                self.add_event(self)
            else:
                self.weekly_habit(db)
       else:
        print(f"{Fore.RED}Enter a valid habit name")


    def longest(self, db):
        #Computes the longest streak based on the current streak value.
        streak = get_streak(self.db, self.name)
        count = get_longest_streak_from_logs(self.db, self.name)
        if streak >= count:
            self.streak = get_streak(self.db, self.name)
            update_count(self.db, self.name, self.streak)

    