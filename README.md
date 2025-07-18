# 📋 My To-Do App

A versatile, multi-interface To-Do application built with **Python** that adapts to your workflow preferences.

## 🚀 Three Ways to Stay Organized

| Interface | Technology | Best For |
|-----------|------------|----------|
| 🖥️ **Command Line** | Pure Python | Power users & automation |
| 🪟 **Desktop GUI** | PySimpleGUI | Local desktop experience |
| 🌐 **Web Interface** | Streamlit | Remote access & sharing |

---

## ✨ Key Features

- **📜 Persistent Storage** - Your tasks are saved automatically per user
- **✅ Full CRUD Operations** - Add, edit, complete, and delete tasks seamlessly
- **👤 Multi-User Support** - Username-based task separation
- **🕒 Real-Time Updates** - Live clock in GUI, auto-refresh in web app
- **🔄 Cross-Platform** - Works on Windows, macOS, and Linux
- **🎯 Clean Interface** - Intuitive design across all three interfaces

---

## 📁 Project Structure

```
My-Todo-App/
├── 📄 cli.py                    # Command-line interface
├── 🖼️ gui.py                    # Desktop GUI application
├── 🌐 web.py                    # Streamlit web application
├── ⚙️ functions.py              # Shared utility functions
├── 📝 todos_<username>.txt      # Auto-generated user data files
└── 📖 README.md                 # This file
```

---

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Quick Start
```bash
# 1. Clone the repository
git clone https://github.com/M-F-Tushar/My-Todo-App.git
cd My-Todo-App

# 2. Install dependencies
pip install PySimpleGUI streamlit

# 3. Run your preferred interface
python cli.py          # Command line
python gui.py          # Desktop GUI
streamlit run web.py   # Web interface
```

---

## 💻 Usage Guide

### Command-Line Interface
```bash
python cli.py
```
**Perfect for:** Terminal enthusiasts and automation scripts

**Commands:**
- `add` - Add a new task
- `show` - Display all tasks
- `edit <number>` - Modify existing task
- `complete <number>` - Mark task as done
- `exit` - Close application

### Desktop GUI
```bash
python gui.py
```
**Perfect for:** Local desktop users who prefer visual interfaces

**Features:**
- Interactive buttons for all operations
- Real-time clock display
- Clean, responsive layout
- Instant visual feedback

### Web Interface
```bash
streamlit run web.py
```
**Perfect for:** Remote access and team collaboration

**Features:**
- Browser-based access from anywhere
- Responsive design for mobile/desktop
- Auto-refresh functionality
- Simple login system

🔗 **[Try the Live Demo](https://m-f-tushar-my-todo-app-web-dsvkax.streamlit.app/)**

---

## 🏗️ Technical Architecture

### Core Functions (`functions.py`)
```python
def get_todos(username):
    """Load user-specific todos from file"""
    filepath = f"todos_{username}.txt"
    # Implementation handles file creation and reading
    
def write_todos(todos, username):
    """Save todos to user-specific file"""
    # Atomic write operations for data integrity
```

### Data Storage
- **Format:** Plain text files (human-readable)
- **Location:** Local filesystem
- **Naming:** `todos_<username>.txt`
- **Encoding:** UTF-8 with proper error handling

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
