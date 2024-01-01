Welcome to the Habit Tracker – a versatile tool designed to help you build and maintain positive habits effortlessly. Whether you're striving for daily, weekly, or monthly goals, this user-friendly application provides a simple yet effective way to track your progress, analyze your habits, and stay motivated on your journey toward self-improvement.

## Table of Contents
1. [What is a Habit Tracker?](#what-is-a-habit-tracker)
2. [How It Works](#how-it-works)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Analysis](#analysis)
6. [Database](#database)
7. [Requirements](#requirements)
8. [Contributing](#contributing)
9. [License](#license)

Let's get started on cultivating those positive habits!

## What is a Habit Tracker?
A habit tracker is a powerful tool that assists individuals in developing and maintaining positive habits by providing a systematic way to monitor and analyze their progress. This Habit Tracker offers a range of features to suit various habit-building needs, from daily routines to weekly commitments and monthly goals. It can be run on any platform that has access to Python 3.

## How It Works
The application is built with a command-line interface (CLI) for ease of use. Users can create habits, mark them as complete, analyze their habits, and even remove habits they no longer wish to track.

## Installation
Before getting started with the Habit Tracker, make sure you have Python 3.7+ installed on your machine. 
Afterward, follow these simple installation steps:

git clone [https://github.com/AngelikaPolshikova/HabitTracker.git](https://github.com/AngelikaPolshikova/HabitTracker.git)

```bash
cd habit-tracker
```

```bash
pip install -r requirements.txt
```

## Usage
The Habit Tracker CLI provides a user-friendly menu for creating habits, marking them as complete, analyzing habits, and removing habits. Simply follow the prompts to interact with the application.

 ![Main Menu](https://github.com/AngelikaPolshikova/HabitTracker/blob/main/img/Main_menu.png)

### Example Commands:
- **Creating a Habit**: Choose "Create a habit" from the menu and follow the prompts to define a new habit.
  
 ![Main Menu](https://github.com/AngelikaPolshikova/HabitTracker/blob/main/img/create_habit.png)

- **Completing a Habit**: Select "Complete habit," enter the habit name, and the application will handle the completion process.
  
![complete_habit](https://github.com/AngelikaPolshikova/HabitTracker/blob/main/img/Completed_habit.png)
  
- **Analyzing Habits**:
  
  * analyzing all habits
  
![Analyse habits](https://github.com/AngelikaPolshikova/HabitTracker/blob/main/img/analyse_habits.png)

  * habits within the same period
    
 ![Analyse habits](https://github.com/AngelikaPolshikova/HabitTracker/blob/main/img/analyze_all.png)
 
  * longest streaks
    
 ![Longest_streak](https://github.com/AngelikaPolshikova/HabitTracker/blob/main/img/longest_all_streak.png)     
 
  * habit logs
    
 ![logs](https://github.com/AngelikaPolshikova/HabitTracker/blob/main/img/check_logs.png)
      
- **Removing a Habit**: Under "Remove," you will see the list of the existing habits. Choose the habit you want to remove from the provided list.

![remove](https://github.com/AngelikaPolshikova/HabitTracker/blob/main/img/remove.png)


![remove_2](https://github.com/AngelikaPolshikova/HabitTracker/blob/main/img/remove_2.png)

## Analysis
The application offers several analysis features, allowing users to gain insights into their habit-building journey. Analyze all tracked habits, habits with the same period, your longest streak, and see all your habit logs.

## Requirements
Ensure you have the required dependencies installed by running:

```bash
pip install -r requirements.txt
```
### Dependencies:
- colorama
- questionary
- pytest

## Database
The application uses SQLite as the database to store habit information. The database is created and maintained automatically when you first run the application.

## Contributing
Contributions are welcome! Feel free to submit issues or pull requests to enhance the functionality, fix bugs, or suggest new features.

## License
This project is licensed under the MIT License.

