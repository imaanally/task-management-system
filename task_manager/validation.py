from datetime import datetime

def validate_task_title(title):
    if len(title) == 0:
        print("Title cannot be empty.")
        return False

    return True

def validate_task_description(description):
    if len(description) == 0:
        print("Description cannot be empty.")
        return False

    if len(description) > 500:
        raise ValueError("Description cannot be more than 500 characters.")

    return True

def validate_due_date(due_date):
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
        return True
    except ValueError:
        print("Due date must be in YYYY-MM-DD format.")
        return False