# To-Do List Application

tasks = []

def display_tasks():
    if not tasks:
        print("\nYour task list is empty!")
    else:
        print("nYour tasks:")
        fof i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter a task to add: ")
    tasks.append(task)
    print(f'"{task}" has been added to your task list!')

def remove_task():
    display_tasks()
    try:
        task_num = int(input("Enter the number of the task to remove: "))
        removed_task = tasks.pop(task_num - 1)
        print(f'"{removed_task}" has been removed from your task list!')
    except (ValueError, IndexError):
        print("Invalid input. Please try again.")

def main():
    while True:
        print("\nTo-Do List Options:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task") 
        print("4. Exit")

        choise = input("Choose an option (1-4): ")
        
        if choise == "1":
            display_tasks()
        elif choise == "2":
            add_task()
        elif choise == "3":
            remove_task()
        elif choise == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choise. Please try again.")

if __name__ == "__main__":
     main()
        
