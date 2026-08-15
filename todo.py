import json

tasks = []

try:
    with open("tasks.json", "r") as file:
        tasks = json.load(file)
except FileNotFoundError:
    tasks = []

while True:
    print("\n==MY TODO LIST==")
    print("1. Add tasks")
    print("2. View tasks")
    print("3. Mark task as complete")
    print("4. Update task")
    print("5. Delete task")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter your task: ")
        tasks.append(task)

        with open("tasks.json", "w") as file:
            json.dump(tasks, file)

        print("Task added successfully!")
    
    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks found.")
        else:
            print("Your Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(i, ".", task)

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks found.")
        else:
            task_number = int(input("Enter the task number to mark complete: "))
            if 1 <= task_number <= len(tasks):
                tasks[task_number - 1] = tasks[task_number - 1] + " [Completed]"
                
                with open("tasks.json", "w") as file:
                    json.dump(tasks, file)
                    
                print("Task marked as complete!")
            else:
                print("Invalid task number.")

    elif choice == "4":
        if len(tasks) == 0:
            print("No tasks found.")
        else:
            task_number = int(input("Enter the task number to update: "))
            if 1 <= task_number <= len(tasks):
                new_task = input("Enter the new task: ")
                tasks[task_number - 1] = new_task
                
                with open("tasks.json", "w") as file:
                    json.dump(tasks, file)
                    
                print("Task updated successfully!")
            else:
                print("Invalid task number.")

    elif choice == "5":
        if len(tasks) == 0:
            print("No tasks found.")
        else:
            task_number = int(input("Enter the task number to delete: "))
            if 1 <= task_number <= len(tasks):
                del tasks[task_number - 1]
                
                with open("tasks.json", "w") as file:
                    json.dump(tasks, file)
                    
                print("Task deleted successfully!")
            else:
                print("Invalid task number.")

    elif choice == "6":
        print("Thank you for using My To-Do List!")
        break

    else:
        print("Invalid choice. Please try again.")           