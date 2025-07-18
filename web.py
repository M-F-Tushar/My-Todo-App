import streamlit as st
import functions

st.set_page_config(page_title="My To-Do App", page_icon="✅")

st.title("✅ My Todo App")
st.subheader("Your personalized to-do list")
st.write("This app helps you stay organized and productive.")

# Ask for username if not already in session
if "username" not in st.session_state:
    username_input = st.text_input("Enter your username to continue:", key="username_input")
    if username_input:
        st.session_state.username = username_input.strip()
        st.rerun()

if "username" in st.session_state:
    username = st.session_state.username
    todos = functions.get_todos(username)

    def add_todo():
        new_todo = st.session_state["new_todo"].strip()
        if new_todo:
            todos.append(new_todo + "\n")
            functions.write_todos(todos, username)
            st.session_state["new_todo"] = ""

    st.markdown("### Your Tasks:")

    # List all todos with checkboxes
    for index, todo in enumerate(todos):
        checkbox = st.checkbox(todo.strip(), key=f"{todo}_{index}")
        if checkbox:
            todos.pop(index)
            functions.write_todos(todos, username)
            st.rerun()

    # Input field to add new todo
    st.text_input(label="Add a new task", placeholder="E.g. Walk the dog",
                  on_change=add_todo, key='new_todo')
