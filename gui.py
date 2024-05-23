from modules import functions
import FreeSimpleGUI as fsg

label = fsg.Text("Type in a To-Do")
input_box = fsg.InputText(tooltip="Enter To-Do", key="todo")
add_button = fsg.Button("Add")

window = fsg.Window("To-Do List",
                    [[label, input_box, add_button]],
                    font=('Helvetica', 14))

while True:
    event, values = window.read()
    print(event)
    print(values['todo'])

    match event:
        case 'Add':
            todos = functions.read_todos_from_file()
            todos.append(values['todo'] + '\n')
            functions.save_todos_to_file(todos)
        case fsg.WINDOW_CLOSED:
            break

window.close()
