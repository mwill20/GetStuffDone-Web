import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("My GetStuffDone App")
st.subheader("This is My GetStuffDone App")
st.write("This app is to MAKE SURE we get stuff done!")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="", placeholder="What do we need to Get Done..?",
            on_change=add_todo, key='new_todo')
