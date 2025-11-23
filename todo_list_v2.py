"""To-Do list Program v2 
Initializes a list where tasks will be stored.
"""
todo_list = []


def greeting():
    """Displays a greeting message to the user."""
    print("\nWelcome to your to-do list!")


def menu():
    """Displays the main menu."""
    print("1. Add")
    print("2. Edit")
    print("3. View")
    print("4. Delete")
    print("5. Complete")
    print("6. Exit")


def clear_screen():
    """Clears terminal window."""
    print("\n" * 100)


def keep_adding(todo_list):
    """
    Prompts the user to continue adding items.
    Utilized within the add definition.
    Calls: add, clear_screen, todo_list.
    """
    keep_adding = input(str("\nContinue adding tasks? (y/n): "))
    keep_adding = keep_adding.lower()
    if keep_adding == "y":
        add(todo_list)
        return
    elif keep_adding == "n":
        clear_screen()
        return
    else:
        input("Invalid choice. Press enter to return to the menu.")
        clear_screen()


def add(todo_list):
    """
    Add tasks to the todo_list dictionary.
    Format: Name, Details, Status, Priority.
    Calls: clear_screen, keep_adding, todo_list.
    """
    task_name = input("Name of the task? (type 'done' to return to menu): ")
    if  task_name == "done":
        clear_screen()
        return
    details = input("Add details (type 'done' to return to menu): ")
    if details == "done":
        clear_screen()
        return
    priority = input("Enter the priority of the task (type 'done' to return to menu): ")
    if priority == "done":
        clear_screen()
        return
    task = {"name": task_name, "details": details, "status": "Incomplete", "priority": priority}
    todo_list.append(task)
    clear_screen()
    print(f"\n{task_name} added to your to-do list.")
    keep_adding(todo_list)


def edit(todo_list):
    """
    Edits task based on user input.
    Calls: clear_screen, view, todo_list.
    """
    if not todo_list:
        input("The list is empty. Press enter to continue.")
        clear_screen()
        return
    view(todo_list)
    try:
        selection = int(input("\nSelect a task to edit: ")) - 1
    except ValueError:
        input("Invalid choice. Press enter to continue.")
        clear_screen()
        return
    if 0 <= selection < len(todo_list):
        updated_name = input("New name (leave blank to keep): ")
        updated_details = input("New details (leave blank to keep): ")
        updated_priority = input("New priority status (leave blank to keep): ")
        if updated_name:
            todo_list[selection]["name"] = updated_name
        if updated_details:
            todo_list[selection]["details"] = updated_details
        if updated_priority:
            todo_list[selection]["priority"] = updated_priority
        clear_screen()
        print(f"\n{todo_list[selection]['name']} updated.")
    else:
        input("Invalid choice. Press enter to continue.")
        clear_screen()


def view(todo_list):
    """
    Displays the current tasks.
    Calls: clear_screen, todo_list.
    """
    if not todo_list:
        input("The list is empty. Press enter to continue.")
        clear_screen()
        return
    if todo_list:
        clear_screen()
        print("-" * 48)
        print("----Task(s)----Details----Status----Priority----")
        for z, task in enumerate(todo_list):
            print(f"{z+1}. {task['name']} - {task['details']} - {task['status']} - {task['priority']}")

def delete(todo_list):
    """
    Deletes task based on user input.
    Calls: clear_screen, todo_list, view.
    """
    if not todo_list:
        input("The list is empty. Press enter to continue.")
        clear_screen()
        return
    view(todo_list)
    try:
        selection = int(input("\nSelect a task to delete: ")) - 1
    except ValueError:
        input("Invalid choice. Press enter to continue.")
        clear_screen()
        return
    if 0 <= selection < len(todo_list):
        del_task = todo_list[selection]['name']
        del todo_list[selection]
        clear_screen()
        print(f"\n{del_task} has been deleted.")
        return
    else:
        input("Invalid choice. Press enter to continue.")
        clear_screen()

def complete(todo_list):
    """
    Completes task based on user input.
    Calls: clear_screen, todo_list, view.
    """
    if not todo_list:
        input("The list is empty. Press enter to continue.")
        clear_screen()
        return
    view(todo_list)
    try:
        selection = int(input("\nSelect a task to complete: ")) - 1
        clear_screen()
    except ValueError:
        input("Invalid choice. Press enter to continue.")
        clear_screen()
        return
    if 0 <= selection < len(todo_list):
        if todo_list[selection]["status"] == "Complete":
            print(f"{todo_list[selection]['name']} that task has already been completed.")
        else:
            todo_list[selection]["status"] = "Complete"
            completed_task = todo_list[selection]['name']
            clear_screen()
            print(f"\n{completed_task} marked as complete.")
    else:
        input("Invalid choice. Press enter to continue.")
        clear_screen()


while True:
    """
    The main loop.
    Greets user, displays menu, and handles user input.
    Calls: add, complete, delete, edit, greeting, menu, view.
    """
    greeting()
    menu()
    choice = input("\nMake a selection (1-6): ")
   
    if choice == "1":
        add(todo_list)

    elif choice == "2":
        edit(todo_list)

    elif choice == "3":        
        view(todo_list)

    elif choice == "4":
        delete(todo_list)

    elif choice == "5":
        complete(todo_list)

    elif choice == "6":
        print("Exiting...")
        break

    else:
        input("Invalid choice. Press enter to continue.")
        clear_screen()