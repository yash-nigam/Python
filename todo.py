todo_list = []

while(True):
    option = input("Enter add, show, edit or exit: ")
    match option:
        case "add":
            todo_list.append(input("Enter Value: "))
        case "show":
            for item in todo_list:
                print(item)
        case "exit":
            break
        case _:
            print("Enter a correct value: ")
