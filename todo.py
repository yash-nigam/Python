todo_list = []

while(True):
    option = input("Enter add, show, edit or exit: ")
    match option:
        case "add":
            todo_list.append(input("Enter Value: "))
        case "show":
            i = 0
            while i < len(todo_list):
                print(f"{i} : {todo_list[i]}")
                i+=1
        case "edit":
            index=input("Enter index number of item you want to edit")
            print(f"Existing Value: {todo_list[int(index)]}")
            new_value = input("Enter new value")
            todo_list[int(index)] = new_value
        case "exit":
            break
        case _:
            print("Enter a correct value: ")
