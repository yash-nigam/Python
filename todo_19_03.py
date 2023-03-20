def get_todos():
    with open("todos.txt", "r") as file:
        todos = file.readlines()
    return todos


while True:
    user_action = input("add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos.append(todo + '\n')

        with open("todos.txt", "w") as file:
            file.writelines(todos)

    elif "show" in user_action:

        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip("\n")
            print(f"index = {index+1} - item = {item}")

    elif "edit" in user_action:
        try:

            todos = get_todos()

            edit_line = input("Enter as -> <row number><space><new todo>: ")
            edit_line = edit_line.strip(" ")
            line_num = int(edit_line[0:1])
            todo = edit_line[1:].strip()
            todos[line_num -1] = todo + "\n"

            with open("todos.txt", "w") as file:
                file.writelines(todos)
        except IndexError:
            print("The index provided is out of Range")

    elif "complete" in user_action:

        todos = get_todos()
        complete_line_num = int(user_action[8:].strip())
        todos.pop(complete_line_num - 1)

        with open("todos.txt", "w") as file:
            file.writelines(todos)
