from pathlib import Path

todo_list = []

while(True):
    option = input("Enter add, show, edit or exit: ")
    match option:
        case "add":

            readfile = open("todo_list.txt", "r")
            todo_list = readfile.readlines()
            print(f"value read from file = {todo_list}")

            todo_list.append(input("Enter Value: ")+"\n")
            writefile = open("todo_list.txt","w")
            writefile.writelines(todo_list)
            writefile.close()
        case "show":
            for index,val in enumerate(todo_list):
                print(f"{index+1}-{val}")
        case "edit":
            index=input("Enter index number of item you want to edit")
            print(f"Existing Value: {todo_list[int(index)]}")
            new_value = input("Enter new value")
            todo_list[int(index)] = new_value
        case "complete":
            todo_list.pop(int(input("Enter the index of item to delete"))-1)
        case "exit":
            break
        case _:
            print("Enter a correct value: ")
