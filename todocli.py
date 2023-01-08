import json
from datetime import date

emptyDoc = False

while True:
    with open("todoDB.json", "r") as f:
        todoData = json.load(f)
    # f = open("todoDB.json","r")
    # todoData = json.load(f)
    # print(todoData, type(todoData))

    currentData = date.today()

    if len(todoData) == 0:
        emptyDoc = True
        username = input(
            "\nHi there!! Welcome to TodoCLI. Please enter your username: ")
        todoData["name"] = username
        todoData["date"] = str(currentData)

        print(f"Hey {username}! I hope you had a good start of the day ")
        print("\nCreat a task by weriting <create task> or <add task>")

        cmd = input(">>")
        todoData["today"] = []

        if cmd == "creat task" or cmd == "add task":
            task_description = input("\nEnter your task description: ")
            scheduled_time = input("\nEnter scheduled time for the task: ")

            task = {
                "description": task_description,
                "scheduled_time": scheduled_time
            }
            todoData["today"].append(task)

            with open("todoDB.json", "w") as f:
                json.dump(todoData, f, indent=4)  # dump(saveLoc, indent = x)
    elif "today" in list(todoData.keys()):
        # First print the existing task
        tasks = todoData["today"]
        username = todoData["name"]
        print(f"\nToday is {currentData}")
        print(f"\nHey {username}, here are the tasks for your day\n")

        for task in tasks:
            print(f"\nTask number {tasks.index(task)+1}")
            print("\nTask Description: ", task["description"])
            print("\nSchedule time: ", task["scheduled_time"])

        print("\nCreate another task")
        cmd = input(">>")

        if cmd == "creat task" or cmd == "add task":
            task_description = input("\nEnter your task description: ")
            scheduled_time = input("\nEnter scheduled time for the task: ")

            task = {
                "description": task_description,
                "scheduled_time": scheduled_time
            }
            todoData["today"].append(task)

            with open("todoDB.json", "r+") as f:
                f.seek(0)  # where to start the index
                json.dump(todoData, f, indent=4)  # dump(saveLoc, indent = x)

            print("Task created successfully\n")
            print("If you want to add more task, type add task /create task\n")
            print("If you're done for now, please type done\n")


        if cmd == "done" or cmd == "exit":
            print("Have a great day!!")
            break
        
#your task is to delete whole data of todoDB.json
        if cmd == "clear" or "clear":
            with open("todoDB.json", "w") as f:
                print(todoData)
                # del todoData[1:]
