import streamlit as st
from modules import functions


def add_todo():
    new_todo = st.session_state['todo_input']
    todos.append(new_todo + '\n')
    functions.save_todos_to_file(todos)

st.title('My ToDo App')

todos = functions.read_todos_from_file()

for index,todo in enumerate(todos):
    checkbox = st.checkbox(label=todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.save_todos_to_file(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label='label', label_visibility='hidden', placeholder='Add new todo',
              on_change=add_todo, key='todo_input')
