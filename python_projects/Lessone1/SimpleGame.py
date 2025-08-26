# List of tasks
tasks = []

def show_menu():
    print("\n--- Menu ---")
    print("1. Show all tasks")
    print("2. Add a task")
    print("3. Remove a task")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == "1":
        if not tasks:
            print("Task list is empty!")
        else:
            print("\nCurrent tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "2":
        new_task = input("Enter a new task: ")
        tasks.append(new_task)
        print(f"Task '{new_task}' has been added!")

    elif choice == "3":
        if not tasks:
            print("Task list is empty!")
        else:
            num = int(input("Enter the number of the task to remove: "))
            if 1 <= num <= len(tasks):
                removed = tasks.pop(num - 1)
                print(f"Task '{removed}' has been removed!")
            else:
                print("Invalid number!")

    elif choice == "4":
        print("Exiting the app. Goodbye 👋")
        break

    else:
        print("Invalid choice, try again.")
