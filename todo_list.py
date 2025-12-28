from pathlib import Path

#Task is for task manipulation / task itself
class Task:

    def __init__(self, controller):
        """
        Creates an instance of ToDo_List.
        Calls: ToDo_List
        """
        self.controller = controller 

    def add(self):
        """
        Add tasks to the todo_list.
        Format: Name, Details, Status, Priority.
        Calls: clear_screen, keep_adding, task_name todo_list.
        """
        self.controller.clear_screen()
        print("\n--- Add Tasks (type 'done' to stop) ---")

        task_name = input("Name of the task?: ")
        if  task_name.lower() == "done":
            self.controller.clear_screen()
            return

        details = input("Add details: " )
        if details.lower() == "done":
            self.controller.clear_screen()
            return

        priority = input("Enter priority of the task (High, Medium, Low): ")
        if priority.lower() == "done":
            self.controller.clear_screen()
            return

        task = {
            "name": task_name, 
            "details": details,
            "status": "Incomplete",
            "priority": priority
            }

        self.controller.todo_list.append(task)
        self.controller.save_task()
        self.controller.clear_screen()
        self.task_name(task_name)
        self.keep_adding()

    def keep_adding(self):
        """
        Prompts the user to continue adding items.
        Utilized within the add definition.
        Calls: add, clear_screen.
        """
        keep_adding = input(str("\nContinue adding tasks? (y/n): "))
        keep_adding = keep_adding.lower()

        if keep_adding == "y":
            self.add()
            return

        elif keep_adding == "n":
            self.controller.clear_screen()
            return
        else:
            input("Invalid choice. Press enter to return to the menu.")
            self.controller.clear_screen()

    def complete(self):
        """
        Completes task based on user input.
        Calls: clear_screen, todo_list, view_all.
        """
        if not self.controller.todo_list:
            input("The list is empty. Press enter to continue.")
            self.controller.clear_screen()
            return
        self.view_all()
        try:
            selection = int(input("\nSelect a task to complete: ")) - 1
            self.controller.clear_screen()
        except ValueError:
            input("Invalid choice. Press enter to continue.")
            self.controller.clear_screen()
            return
        if 0 <= selection < len(self.controller.todo_list):
            if self.controller.todo_list[selection]["status"] == "Complete":
                print(f"{self.controller.todo_list[selection]['name']} has already been completed.")
            else:
                self.controller.todo_list[selection]["status"] = "Complete"
                completed_task = self.controller.todo_list[selection]['name']
                self.controller.clear_screen()
                print(f"\n{completed_task} marked as complete.")
                self.controller.save_task()
        else:
            input("Invalid choice. Press enter to continue.")
            self.controller.clear_screen()




    def edit(self):
        """
        Edits task based on user input.
        Calls: clear_screen, view_all, todo_list.
        """
        if not self.controller.todo_list:
            input("The list is empty. Press enter to continue.")
            self.controller.clear_screen()
            return
        self.view_all()
        try:
            selection = int(input("\nSelect a task to edit: ")) - 1
        except ValueError:
            input("Invalid choice. Press enter to continue.")
            self.controller.clear_screen()
            return
        if 0 <= selection < len(self.controller.todo_list):
            updated_name = input("New name (leave blank to keep): ")
            updated_details = input("New details (leave blank to keep): ")
            updated_priority = input("New priority (leave blank to keep): ")
            if updated_name:
                self.controller.todo_list[selection]["name"] = updated_name
            if updated_details:
                self.controller.todo_list[selection]["details"] = updated_details
            if updated_priority:
                self.controller.todo_list[selection]["priority"] = updated_priority
            self.controller.clear_screen()
            print(f"\n{self.controller.todo_list[selection]['name']} updated.")
            self.controller.save_task()
        else:
            input("Invalid choice. Press enter to continue.")
            self.controller.clear_screen()




    def view_all(self):
        """
        Displays the current tasks.
        Calls: clear_screen, task_display, todo_list.
        """
        if not self.controller.todo_list:
            input("The list is empty. Press enter to continue.")
            self.controller.clear_screen()
            return
        if self.controller.todo_list:
            self.controller.clear_screen()
            self.task_display()

    def view_incomp(self):
        """
        Displays only incomplete tasks.
        Calls: clear_screen, todo_list.
        """
        if not self.controller.todo_list:
            input("The list is empty. Press enter to continue.")
            self.controller.clear_screen()
            return

        self.controller.clear_screen()
        print("--- Incomplete Tasks ----")
        track = False

        for z, task in enumerate(self.controller.todo_list):
            if task["status"] == "Incomplete":
                print(f"{z+1}. {task['name']} | {task['details']} | Status: {task['status']} | Priority: {task['priority']}")
                track = True

        if not track:
            input("All tasks are complete. Press enter to return to the menu.")
            self.controller.clear_screen()

    def delete(self):
        """
        Deletes task based on user input.
        Calls: clear_screen, todo_list, view_all.
        """
        if not self.controller.todo_list:
            input("The list is empty. Press enter to continue.")
            self.controller.clear_screen()
            return
        self.view_all()
        try:
            selection = int(input("\nSelect a task to delete: ")) - 1
        except ValueError:
            input("Invalid choice. Press enter to continue.")
            self.controller.clear_screen()
            return
        if 0 <= selection < len(self.controller.todo_list):
            del_task = self.controller.todo_list[selection]['name']
            del self.controller.todo_list[selection]
            self.controller.clear_screen()
            print(f"\n{del_task} has been deleted.")
            self.controller.save_task()
            return
        else:
            input("Invalid choice. Press enter to continue.")
            self.controller.clear_screen()

    def task_display(self):
        """
        Displays an enumerated list of tasks.
        Calls: todo_list.
        """
        print("--- All Tasks ---")
        for z, task in enumerate(self.controller.todo_list):
            print(f"{z+1}. {task['name']} | {task['details']} | Status: {task['status']} | Priority: {task['priority']}")

    
    def task_name(self, name):
        """
        Displays the name of task added to list.
        Calls: todo_list.
        """
        print(f"{name} added to your to-do list.")

# ToDo_List is for menu navigation
class ToDo_List:
    def __init__(self):
        """
        Initialize todo list.
        """
        self.todo_list = []
        self.load_task()

    def save_task(self):
        path = Path("tasks.txt")
        with path.open("w", encoding="utf-8") as z:
            for task in self.todo_list:
                line = f"{task['name']}|{task['status']}|{task['details']}|{task['priority']}"
                z.write(line + "\n")


    def load_task(self):
        path = Path("tasks.txt")
        if path.exists():
            with path.open("r", encoding="utf-8") as z:
                for line in z:
                    split = line.strip().split("|")
                    if len(split) == 4:
                        name, status, details, priority = split
                        task = {
                            "name": name,
                            "status": status,
                            "details": details,
                            "priority": priority,
                        }
                        self.todo_list.append(task)

    def menu(self):
        """
        Main loop that handles menu display & user input.
        Calls: add, view_all, view_incomp, edit, complete,
               delete, clear_screen, Task.
        Note: The task variable allows class interaction.
        """
        task = Task(self)
        while True:
            print("\n")
            print("--- To-Do List Menu ---")
            print("1. Add")
            print("2. View All")
            print("3. View Incomplete")
            print("4. Edit")
            print("5. Complete")
            print("6. Delete")
            print("7. Exit")

            choice = input("\nMake a selection (1-7): ")
   
            if choice == "1":
                task.add()

            elif choice == "2":
                task.view_all()
        
            elif choice == "3":
                task.view_incomp()

            elif choice == "4":        
                task.edit()

            elif choice == "5":
                task.complete()

            elif choice == "6":
                task.delete()

            elif choice == "7":
                print("Exiting...")
                break

            else:
                input("Invalid choice. Press enter to continue.")
                self.clear_screen()

    def clear_screen(self):
        """Prints 100 blank lines, clearing terminal."""
        print("\n" * 100)

"""
Runs the program.
"""
run = ToDo_List()
run.menu()
