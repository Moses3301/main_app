# todo.py

# Define a list to store the todo items
todos = []

# Function to display the todo list
def display_todos():
    if not todos:
        print("No todos found. The list is empty.")
    else:
        print("Todo List:")
        for i, todo in enumerate(todos, start=1):
            print(f"{i}. {todo}")

# Function to add a new todo item
def add_todo():
    todo = input("Enter a new todo: ")
    todos.append(todo)
    print("Todo added successfully!")

# Function to remove a todo item
def remove_todo():
    display_todos()
    index = int(input("Enter the index of the todo to remove: "))
    if index < 1 or index > len(todos):
        print("Invalid index!")
    else:
        removed_todo = todos.pop(index - 1)
        print(f"Removed todo: {removed_todo}")

# Main loop
while True:
    
    print("\nTodo List Application")
    print("1. Display Todos")
    print("2. Add Todo")
    print("3. Remove Todo")
    print("4. Quit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        display_todos()
    elif choice == "2":
        add_todo()
    elif choice == "3":
        remove_todo()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")