tasks = []

while True:
    print("\n--- TODO APP ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Mark Task as Done")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter new task: ")
        tasks.append({"task": task, "done": False})
        print("Task added successfully!")

    elif choice == "2":
        if not tasks:
            print("No tasks available.")
        else:
            for i, t in enumerate(tasks, start=1):
                status = "✔" if t["done"] else "✘"
                print(f"{i}. {t['task']} [{status}]")

    elif choice == "3":
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            print(f"Deleted task: {removed['task']}")
        else:
            print("Invalid task number!")

    elif choice == "4":
        num = int(input("Enter task number to mark as done: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]["done"] = True
            print("Task marked as done!")
        else:
            print("Invalid task number!")

    elif choice == "5":
        print("Exiting Todo App. Goodbye!")
        break

    else:
        print("Invalid choice! Try again.")