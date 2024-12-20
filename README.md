# To-Do List Application

## Overview
This Python-based To-Do List application allows users to manage their tasks efficiently. It provides options to add, view, update, and delete tasks, with the tasks being stored in a JSON file for persistence.

---

## Features
- View all tasks with their status (Pending or Done).
- Add new tasks to your to-do list.
- Mark tasks as completed.
- Delete tasks from your list.
- Persistent storage using `tasks.json`.

---

## Requirements
- Python 3.x installed on your system.

---

## Installation
1. **Download Python:**
   - If Python is not installed, download it from [https://www.python.org/](https://www.python.org/).

2. **Clone or Download the Project:**
   - Save the script file `todo_list_app.py` to your local system.

---

## Usage
### Running the Application
1. Open your terminal or command prompt.
2. Navigate to the directory containing the `todo_list_app.py` file using the `cd` command. For example:
   ```bash
   cd path/to/directory
   ```
3. Run the script using the command:
   ```bash
   python todo_list_app.py
   ```
   or, if Python 3 is required:
   ```bash
   python3 todo_list_app.py
   ```

### Interacting with the Application
When the application runs, you will see the following menu:
```
=== To-Do List Menu ===
1. View all tasks
2. Add a new task
3. Mark a task as complete
4. Delete a task
5. Quit
```

- **Option 1:** View all tasks currently stored.
- **Option 2:** Add a new task by entering its description.
- **Option 3:** Mark a specific task as completed by entering its number.
- **Option 4:** Delete a task by entering its number.
- **Option 5:** Exit the application.

---

## Storage
Tasks are stored in a file named `tasks.json` in the same directory as the script. This file will be created automatically if it does not exist. Tasks are saved in the following format:
```json
[
    {
        "task": "Example Task",
        "completed": false
    }
]
```

---

## Troubleshooting
### Common Issues
1. **Python not found:**
   - Ensure Python is installed and added to your system's PATH.
   - Verify installation with:
     ```bash
     python --version
     ```
     or
     ```bash
     python3 --version
     ```

2. **`tasks.json` Issues:**
   - If the file is corrupted, delete it, and the program will recreate it as empty.

3. **Invalid Input:**
   - Ensure numeric inputs are provided where required (e.g., task numbers).

---

## License
This project is open-source and available under the MIT License.

---

## Author
Created by [Your Name].
