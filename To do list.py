import os

# The name of the file where tasks are stored
FILENAME = "tasks.txt"


def load_tasks():
    """
    Loads tasks from the tasks.txt file.
    Returns a list of tasks. If the file doesn't exist, returns an empty list.
    """
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, 'r') as file:
        # Read each line and strip the trailing newline character
        tasks = [line.strip() for line in file.readlines()]
    return tasks


def save_tasks(tasks):
    """
    Saves the list of tasks to the tasks.txt file.
    Each task is written on a new line.
    """
    with open(FILENAME, 'w') as file:
        for task in tasks:
            file.write(task + "\n")


def view_tasks(tasks):
    """
    Displays all tasks in the list.
    """
    print("\n--- Your To-Do List ---")
    if not tasks:
        print("Your to-do list is empty. Great job! 👍")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    print("-----------------------\n")


def add_task(tasks):
    """
    Adds a new task to the list.
    """
    task = input("Enter the new task: ")
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print(f"✅ Task '{task}' added successfully!")
    else:
        print("Task cannot be empty.")


def remove_task(tasks):
    """
    Removes a task from the list based on its number.
    """
    if not tasks:
        print("No tasks to remove.")
        return

    view_tasks(tasks)
    try:
        task_num_to_remove = int(input("Enter the number of the task to remove: "))

        # Adjust for 0-based index
        if 1 <= task_num_to_remove <= len(tasks):
            removed_task = tasks.pop(task_num_to_remove - 1)
            save_tasks(tasks)
            print(f"🗑️ Task '{removed_task}' removed successfully!")
        else:
            print("Invalid task number. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")


def main():
    """
    The main function to run the to-do list application.
    """
    tasks = load_tasks()

    while True:
        print("===== To-Do List Menu =====")
        print("1. View tasks")
        print("2. Add a task")
        print("3. Remove a task")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            print("Goodbye! 👋")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


# Run the main function when the script is executed
if __name__ == "__main__":
    main()
