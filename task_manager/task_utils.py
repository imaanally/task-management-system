from datetime import datetime

from task_manager.validation import validate_task_title
from task_manager.validation import validate_task_description
from task_manager.validation import validate_due_date

tasks = []

def add_task(title, description, due_date):
    if not validate_task_title(title):
        return

    if not validate_task_description(description):
        return

    if not validate_due_date(due_date):
        return

    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    }

    tasks.append(task)
    print("Task added successfully!")

def mark_task_as_complete(index, tasks=tasks):
    if index < 0 or index >= len(tasks):
        print("Invalid task number.")
        return

    tasks[index]["completed"] = True
    print("Task marked as complete!")

def view_pending_tasks(tasks=tasks):
    for task in tasks:
        if task["completed"] == False:
            print(task)

def calculate_progress(tasks=tasks):
    if len(tasks) == 0:
        return 0

    completed_tasks = 0

    for task in tasks:
        if task["completed"] == True:
            completed_tasks = completed_tasks + 1

    progress = (completed_tasks / len(tasks)) * 100
    return progress