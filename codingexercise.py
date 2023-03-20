#Percentage Calculator
# try:
#     total = float(input("Enter total Value : "))
#     value = float(input("Enter value: "))
#
#     print("Percent = ",(value/(total/100)))
# except ValueError:
#     print("Enter int or float value")
# except ZeroDivisionError:
#     print("Enter non zero number")


waiting_list = ["john", "marry"]
name = input("Enter name: ")
try:
    number = waiting_list.index(name)
    print(f"{name}'s turn is {number}")
except ValueError:
    print("name should be in the list")