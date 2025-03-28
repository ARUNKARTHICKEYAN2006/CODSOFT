tasks = []  # List to store tasks

def add_task():
    task = input("Enter a task: ")
    tasks.append(task)
    print("Task added!")
    show_tasks()

def remove_task():
    show_tasks()
    if tasks:
        task_name = input("Enter the exact task to remove: ")
        if task_name in tasks:
            tasks.remove(task_name)  # Remove by task name
            print("Task removed!")
            show_tasks()
        else:
            print("Task not found!")

def show_tasks():
    if tasks:
        print("Your Tasks:")
        for task in tasks:
            print("-", task)
    else:
        print("No tasks found!")

def main():
    while True:
        print("\n1) Add Task")
        print("2) Remove Task")
        print("3) View Tasks")
        print("4) Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            remove_task()
        elif choice == "3":
            show_tasks()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Try again.")

# Run the program
main()

