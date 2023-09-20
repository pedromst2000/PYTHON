import os

todoList = []

def addTask():
    task = input("Enter task: ")

    # check if task is empty
    if task == "":
        print("Task cannot be empty")
        return
    # check if the task is already in the list
    if task in todoList:
        print("Task already in list")
        return
    
    todoList.append(task)
    print("Task added successfully")



def viewTasks():
    if len(todoList) == 0:
        print("No tasks in list")
        return

    for task in todoList:
        for i in range(len(todoList)):
            print(f"{i+1}. [ ] {todoList[i]}") # 1. [ ] task1

        

def markTask():
    taskNumber = int(input("Enter task number to mark: "))

    if taskNumber > len(todoList):
        print("Invalid task number")
        return
    
    # check if the task is already marked
    if todoList[taskNumber-1].startswith("[✓]"):
        print("Task already marked")
        return

    todoList[taskNumber-1] = f"[✓] {todoList[taskNumber-1]}"
    print("Task marked successfully")


def menu():
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark Task as Completed")
    print("4. Remove Task")
    print("5. Exit")

    while True:
        choice = input("Enter choice: ")

        if choice == "1":
            addTask()
        elif choice == "2":
            viewTasks()
        elif choice == "3":
            markTask()
        else:
            print("Invalid choice")

menu()


