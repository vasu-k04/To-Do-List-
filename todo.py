import json
import os

# Define a class for the To-Do List application
class ToDoListApp:
    def __init__(self):
        self.filename = "tasks.json"
        self.tasks = self.load_tasks()

    def load_tasks(self):
        """Load tasks from the file, or return an empty list if the file doesn't exist."""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as file:
                    return json.load(file)
            except json.JSONDecodeError:
                print("Error: Corrupted or empty task file. Starting with an empty task list.")
                return []
        return []

    def save_tasks(self):
        """Save the current task list to the file."""
        with open(self.filename, "w") as file:
            json.dump(self.tasks, file, indent=4)

    def show_tasks(self):
        """Display all the tasks."""
        if not self.tasks:
            print("\nNo tasks found!")
        else:
            print("\nYour To-Do List:")
            for idx, task in enumerate(self.tasks, 1):
                status = "Done" if task["completed"] else "Pending"
                print(f"{idx}. {task['task']} [{status}]")

    def add_task(self):
        """Add a new task to the to-do list."""
        task_description = input("\nEnter the description of the new task: ").strip()
        if task_description:
            self.tasks.append({"task": task_description, "completed": False})
            self.save_tasks()
            print("Task added successfully!")
        else:
            print("Task description cannot be empty!")

    def update_task(self):
        """Update a task's completion status."""
        self.show_tasks()
        if not self.tasks:
            return
        try:
            task_number = int(input("\nEnter the number of the task to mark as complete: "))
            if 1 <= task_number <= len(self.tasks):
                self.tasks[task_number - 1]["completed"] = True
                self.save_tasks()
                print("Task marked as completed!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

    def delete_task(self):
        """Delete a task from the to-do list."""
        self.show_tasks()
        if not self.tasks:
            return
        try:
            task_number = int(input("\nEnter the number of the task to delete: "))
            if 1 <= task_number <= len(self.tasks):
                deleted_task = self.tasks.pop(task_number - 1)
                self.save_tasks()
                print(f"Deleted task: '{deleted_task['task']}'")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

    def menu(self):
        """Main menu for user interaction."""
        while True:
            print("\n=== To-Do List Menu ===")
            print("1. View all tasks")
            print("2. Add a new task")
            print("3. Mark a task as complete")
            print("4. Delete a task")
            print("5. Quit")

            choice = input("\nEnter your choice: ").strip()

            if choice == "1":
                self.show_tasks()
            elif choice == "2":
                self.add_task()
            elif choice == "3":
                self.update_task()
            elif choice == "4":
                self.delete_task()
            elif choice == "5":
                print("\nGoodbye!")
                break
            else:
                print("\nInvalid choice. Please try again!")


# Initialize the application and run the menu
if __name__ == "__main__":
    app = ToDoListApp()
    app.menu()

