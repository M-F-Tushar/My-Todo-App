import os

def get_todos(username):
    filepath = f"todos_{username}.txt"
    if not os.path.exists(filepath):
        return []
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, username):
    filepath = f"todos_{username}.txt"
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

# For debugging or CLI test
if __name__ == "__main__":
    user = input("Enter username: ")
    print(f"Hello, {user}")
    print(get_todos(user))
