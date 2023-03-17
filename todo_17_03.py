while True:
    user_action = input("add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if "add" in user_action:
        todo = input("Enter todo :")

        with open("todos.txt", "r") as file:
            todos = file.readlines()

        todos.append(todo + '\n')

        with open("todos.txt", "w") as file:
            file.writelines(todos)

    elif "show" in user_action:

        with open("todos.txt", "r") as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            item = item.strip("\n")
            print(f"index = {index+1} - item = {item}")

    elif "edit" in user_action:

        with open("todos.txt","r") as file:
            todos = file.readlines()

        line_num = input("Enter the number of row to edit: ")
        todo = input("Enter the new todo: ")

        line_num = int(line_num) - 1
        todos[line_num] = todo + "\n"

        with open("todos.txt", "w") as file:
            file.writelines(todos)
