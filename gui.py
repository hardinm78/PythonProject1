from modules import functions
import FreeSimpleGUI as fsg

label = fsg.Text("Type in a To-Do")
input_box = fsg.InputText(tooltip="Enter To-Do", key="todo")
add_button = fsg.Button("Add")
edit_button = fsg.Button("Edit")
list_box = fsg.Listbox(values=functions.read_todos_from_file(), key='todos', enable_events=True, size=(45, 10))

window = fsg.Window("To-Do List",
                    [[label, input_box, add_button], [list_box, edit_button]],
                    font=('Helvetica', 14))

while True:
    event, values = window.read()
    print(event)
    print(values)

    match event:
        case 'Add':
            todos = functions.read_todos_from_file()
            todos.append(str(values['todo'] + '\n').title())
            list_box.update(todos)
            functions.save_todos_to_file(todos)
        case 'Edit':
            todo_to_edit = values['todos'][0]
            new_todo = str(values['todo']+"\n").title()
            todos = functions.read_todos_from_file()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            list_box.update(todos)
            functions.save_todos_to_file(todos)
        case 'todos':
            input_box.update(value=values['todos'][0])
        case fsg.WINDOW_CLOSED:
            break

window.close()
