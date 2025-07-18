# ✅ My To-Do App

A versatile To-Do application built with **Python**, supporting:
- 🖥️ Command-Line Interface (CLI)
- 🪟 Desktop GUI (PySimpleGUI)
- 🌐 Web Interface (Streamlit)

This app helps users manage personal tasks in a clean and user-friendly way, with support for **multi-user** task storage.

---

## ✨ Features

- 📜 Persistent To-Do Storage (per user)
- ✅ Add, Edit, Complete, and Delete tasks
- 🕒 Real-time clock in GUI
- 🔁 Auto-refresh in web app
- 👤 Username-based separation of data
- 🚀 Easy to use in any interface

---

## 📁 Project Structure

```
📁 My-Todo-App/
├── cli.py           # CLI-based todo app
├── gui.py           # GUI app using PySimpleGUI
├── web.py           # Web app using Streamlit
├── functions.py         # Shared utility functions
├── todos_<username>.txt # Auto-generated user-specific todo files
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/M-F-Tushar/My-Todo-App.git
cd My-Todo-App
```

### 2. Install Dependencies
```bash
pip install PySimpleGUI streamlit
```

---

## 🧪 Usage Instructions

### ▶️ Command-Line Version
```bash
python cli.py
```
- Prompts: add, show, edit <number>, complete <number>, exit
- Requests a username
- Stores todos in todos_<username>.txt

### 🪟 GUI Version (Desktop)
```bash
python gui.py
```
- Interactive interface using PySimpleGUI
- Add, Edit, and Complete tasks via buttons
- Displays current time

### 🌐 Web Version (Streamlit)
```bash
streamlit run web.py
```
- Simple and responsive web interface
- Login via username input
- Add todos via input box
- Complete tasks via checkboxes

🔗 **Try the live demo:** [https://m-f-tushar-my-todo-app-web-dsvkax.streamlit.app/](https://m-f-tushar-my-todo-app-web-dsvkax.streamlit.app/)
---

## 🧠 Core Logic (functions.py)

All interfaces share the same core logic:

```python
def get_todos(username):
    filepath = f"todos_{username}.txt"
    ...
    
def write_todos(todos, username):
    ...
```

---

## 🔮 Planned Features

- 📂 Task categories (Work, Personal, etc.)
- 🛎️ Due dates & reminders
- ☁️ Cloud storage integration
- 🔐 Streamlit authentication

---

## 📄 License

This project is licensed under the MIT License.

---

## 🙌 Contributions Welcome

Feel free to fork this repo, suggest features, or submit pull requests.

---

**Ready to organize your life? Pick your preferred interface and start managing your tasks today!**
