# To-do list 
tasks = []

def add_task(task):
    task_id = len(tasks) + 1
    tasks.append({"id": task_id, "task": task, "completed": False})
    print(f"Task '{task}' added.")

def view_tasks():
    for task in tasks:
        status = "Completed" if task["completed"] else "Pending"
        print(f"{task['id']}. {task['task']} - {status}")

def mark_completed(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            print(f"{task['id']}.'{task['task']}' Marked As Completed.")
            return
    print("Task not found.")

def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]
    print(f"Task {task_id} deleted.")
#interface
def main():
    while True:
        print("\nTo-Do List Application")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Mark a task as completed")
        print("4. Delete a task")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            task = input("Enter the task: ")
            add_task(task)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            task_id = int(input("Enter the task ID to mark as completed: "))
            mark_completed(task_id)
        elif choice == '4':
            task_id = int(input("Enter the task ID to delete: "))
            delete_task(task_id)
        elif choice == '5':
            print("EXITING THE APPLICATION.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

