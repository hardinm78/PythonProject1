from modules import functions
import FreeSimpleGUI as fsg
from datetime import datetime

fsg.theme('DarkAmber')

def update_todos():
    todos = functions.read_todos_from_file()
    list_box.update(todos)
    return todos


def save_and_update_todos(todos):
    functions.save_todos_to_file(todos)
    list_box.update(todos)


current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
time_label = fsg.Text(current_time, key='clock')
label = fsg.Text("Type in a To-Do")
input_box = fsg.InputText(tooltip="Enter To-Do", key="todo")
add_button = fsg.Button("Add")
edit_button = fsg.Button("Edit")
complete_button = fsg.Button("Complete")
exit_button = fsg.Button("Exit")
list_box = fsg.Listbox(values=functions.read_todos_from_file(), key='todos', enable_events=True, size=(45, 10))

window = fsg.Window("To-Do List",
                    [[time_label], [label, input_box, add_button],
                     [list_box, edit_button, complete_button, exit_button]],
                    font=('Helvetica', 14))

while True:
    event, values = window.read(timeout=200)
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    time_label.update(current_time)

    match event:
        case 'Add':
            todos = functions.read_todos_from_file()
            todos.append(str(values['todo'] + '\n').title())
            list_box.update(todos)
            functions.save_todos_to_file(todos)
        case 'Edit':
            todo_to_edit = values['todos'][0]
            new_todo = str(values['todo'] + "\n").title()
            todos = update_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            save_and_update_todos(todos)
        case 'Complete':
            try:
                todos = functions.read_todos_from_file()
                todo_to_complete = values['todos'][0]
                index = todos.index(todo_to_complete)
                todos.remove(todos[index])
                functions.save_todos_to_file(todos)
                list_box.update(todos)
            except IndexError:
                fsg.popup("No To-Do entered", font='Helvetica 14')
        case 'Exit':
            break
        case 'todos':
            input_box.update(value=values['todos'][0])
        case fsg.WINDOW_CLOSED:
            break

window.close()
