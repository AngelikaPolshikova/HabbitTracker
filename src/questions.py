import questionary #why do i need questions, questionnaire AND still write text of questions in main file??? triple redundancy 

def confirm_ready():
    return questionary.confirm("Are you ready?").ask()

def select_action():
    return questionary.select(  # Fix: Use questionary instead of questionnaire
        "What do you want to do?",
        choices=["Create a new habit", "Complete the existing habit", "Analyze my habits", "Exit"]
    ).ask()

def counter_name():
    return questionary.text("What's the name of your habit?").ask()

def counter_description():
    return questionary.text("Enter a description for your habit:").ask()

def analyze_counter():
    return questionary.text("Which habit do you want to analyze?").ask()

def increment_counter():
    return questionary.text("Which habit do you want to complete?").ask()
