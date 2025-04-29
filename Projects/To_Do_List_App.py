# todo_list.py

def display_menu():
    print("\n📋 To-Do List Menu:")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

def view_tasks(tasks):
    if not tasks:
        print("\n✅ No tasks right now!")
    else:
        print("\n🗒️ Your Tasks:")
        for index, task in enumerate(tasks, start=1):
            status = "✅" if task['done'] else "❌"
            print(f"{index}. [{status}] {task['task']}")

def add_task(tasks):
    task_name = input("\n✏️ Enter the task: ")
    tasks.append({"task": task_name, "done": False})
    print("✔️ Task added!")

def mark_done(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_number = int(input("\nEnter task number to mark as done: "))
            if 1 <= task_number <= len(tasks):
                tasks[task_number - 1]['done'] = True
                print("🎯 Task marked as done!")
            else:
                print("❗ Invalid task number.")
        except ValueError:
            print("❗ Please enter a valid number.")

def delete_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_number = int(input("\nEnter task number to delete: "))
            if 1 <= task_number <= len(tasks):
                deleted = tasks.pop(task_number - 1)
                print(f"🗑️ Deleted task: {deleted['task']}")
            else:
                print("❗ Invalid task number.")
        except ValueError:
            print("❗ Please enter a valid number.")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("\nChoose an option (1-5): ")
        
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            mark_done(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("\n👋 Exiting To-Do List. Goodbye!")
            break
        else:
            print("❗ Invalid choice. Please select 1-5.")

if __name__ == "__main__":
    main()
