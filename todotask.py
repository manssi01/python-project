task= []
def main_menu():
    print("\n to do list application")
    print("1. Add Task")
    print("2. view Task")
    print("3.  update Task")
    print("4.  remove Task")
    print("5.  Exit Task")
    
    choice= input("choose 1-5 task number : ")
    return choice

def Add_task():
    new_task=input("Enter new task: ")
    task.append(new_task)
    print(f'task"{new_task}" added successfull')

def view_tasks():
    if len(task) == 0:
        print("No tasks available.")
    else:
        print("\nYour Tasks:")
        for idx, new_task in enumerate(task, start=1):
            print(f"{idx}. {new_task}")

def update_task():
    view_tasks()
    task_no = int(input("Enter the task number to update: "))
    if task_no <= len(task) and task_no > 0:
        updated_task = input("Enter the new task: ")
        task[task_no - 1] = updated_task
        print("Task updated successfully!")
    else:
        print("Invalid task number.")

def Remove_task():
    view_tasks()
    task_no = int(input("Enter the task number to delete: "))
    if task_no <= len(task) and task_no > 0:
        task.pop(task_no - 1)
        print("Task deleted successfully!")
    else:
        print("Invalid task number.")

def run_application():
    while True:
        choice = main_menu()
        if choice == '1':
            Add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            update_task()
        elif choice == '4':
            Remove_task()
        elif choice == '5':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    run_application()