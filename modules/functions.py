import os

DEFAULT_FILE_PATH = os.path.join("files", "todos.txt")


def read_todos_from_file(filename=DEFAULT_FILE_PATH):
    """Read to-do items from a file.

    If the specified file does not exist, returns an empty list.

    Args:
    filename (str): The name of the file to read from. Defaults to DEFAULT_FILE_PATH.

    Returns:
    list: A list of to-do items.
    """
    try:
        with open(filename, "r") as todo_file:
            return todo_file.readlines()
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
        return []


def save_todos_to_file(todos, filename=DEFAULT_FILE_PATH):
    """Save to-do items to a file.

    Args:
    todos (list): The to-do items to save.
    filename (str): The name of the file to save to. Defaults to DEFAULT_FILE_PATH.
    """
    with open(filename, "w") as todo_file:
        todo_file.writelines(todos)


def show_todos(todos_list):
    """Display the given to-do items.

    Args:
    todos_list (list): The to-do items to display.
    """
    new_todos = [todo.strip("\n") for todo in todos_list]
    for index, todo in enumerate(new_todos, start=1):
        print(f"{index}. {todo.title()}")


def complete_todo(todos, user_action):
    """Complete a to-do item.

    Args:
    todos (list): The current to-do items.
    user_action (str): The user's action, which should contain the index of the to-do item to be completed.
    """
    try:
        todo_index = int(user_action[9:]) - 1
        todos.remove(todos[todo_index])
    except ValueError:
        print("Invalid input")


def edit_todo(todos, user_action):
    """Edit a to-do item.

    Args:
    todos (list): The current to-do items.
    user_action (str): The user's action, which should contain the index of the to-do item to be edited.
    """
    try:
        todo_index = int(user_action[5:]) - 1
        if todos[todo_index]:
            todos[todo_index] = input("Input new text: ") + "\n"
    except ValueError:
        print("Invalid Value")
    except IndexError:
        print("Invalid Index")


def add_todo(todos, user_action):
    """Add a to-do item.

    Args:
    todos (list): The current to-do items.
    user_action (str): The user's action, which should contain the text of the to-do item to be added.
    """
    todo = str(user_action[4:]) + "\n"
    todos.append(todo)
