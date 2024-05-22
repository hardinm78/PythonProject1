from modules import functions
import time

def execute_user_command():
    """Execute a user command.

    This function reads to-do items, displays them, processes user action, and saves the updates.
    """
    todos = functions.read_todos_from_file()
    functions.show_todos(todos)
    user_action = input("Type add, show, edit, complete or quit: ").lower().strip()
    process_user_action(todos, user_action)
    functions.save_todos_to_file(todos)


def process_user_action(todos, user_action):
    """Process a user action.

    Args:
    todos (list): The current to-do items.
    user_action (str): The user's action to process.
    """
    if user_action.startswith("add") or user_action.startswith("new"):
        functions.add_todo(todos, user_action)
    elif user_action.startswith("edit"):
        functions.edit_todo(todos, user_action)
    elif user_action.startswith("complete"):
        functions.complete_todo(todos, user_action)
    elif user_action.startswith("show"):
        functions.show_todos(todos)
    elif user_action.startswith("quit"):
        quit()

print(time.strftime("%m-%d-%Y %H:%M"))
print(dir(functions))
while True:
    execute_user_command()
