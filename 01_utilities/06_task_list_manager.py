import os


taks_file = "06_task_list.txt"

def load_tasks():
    tasks = []
    if os.path.exists(taks_file):
        with open(taks_file, "r") as file:
            for line in file:
                text, status = line.strip().split("||", 1)
                tasks.append({"text": text, "status": status == "done"})
    else:
        return tasks

def save_tasks(tasks):
    with open(taks_file, "w") as file:
        for task in tasks:
            file.write(f"{task['text']}||{ 'done' if task['status'] else 'pending' }\n")

def display_tasks(tasks):
    if not tasks:
        print("\nNo tasks found.")
    else:
        print("\nTask List:")
        for i, task in enumerate(tasks, start=1):
            status = "✓" if task["status"] else ""
            print(f"{i}. [{status}] {task['text']}")

def task_manager():
    tasks = load_tasks()

    while True:
        print("\nTask Manager Menu:")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Mark a task as done")
        print("4. Remove a task")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ")

        if choice == "1":
            task_text = input("Enter the task description: ")
            tasks.append({"text": task_text, "status": False})
            save_tasks(tasks)
            print(f'Task "{task_text}" added.')

        elif choice == "2":
            display_tasks(tasks)

        elif choice == "3":
            display_tasks(tasks)
            task_number = int(input("Enter the task number to mark as done: "))
            if 1 <= task_number <= len(tasks):
                tasks[task_number - 1]["status"] = True
                save_tasks(tasks)
                print(f'Task "{tasks[task_number - 1]["text"]}" marked as done.')
            else:
                print("Invalid task number.")

        elif choice == "4":
            display_tasks(tasks)
            task_number = int(input("Enter the task number to remove: "))
            if 1 <= task_number <= len(tasks):
                removed_task = tasks.pop(task_number - 1)
                save_tasks(tasks)
                print(f'Task "{removed_task["text"]}" removed.')
            else:
                print("Invalid task number.")

        elif choice == "5":
            print("Exiting the task manager. Goodbye!")
            break

        else:
            print("\nInvalid choice. Please try again.")


task_manager()