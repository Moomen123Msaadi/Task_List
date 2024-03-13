tasks = {}


def addTasks():  # a function that adds a task to the list
    t = input("Insert your task here: ")
    cat = input("Insert Category: ")

    tasks[len(tasks) + 1] = {"task": t, "done": False, "category": cat}
    print("The task has been added to the list.")


def checkTask():  # a function that checks if there are tasks, or if they are done or not
    if len(tasks) != 0:
        print("The Current Tasks are:")

        for i, task in tasks.items():
            if task["done"]:
                print(f"Task #{i} : " + task["task"] + " (done) - " + task["category"])
            else:
                print(f"Task #{i} : " + task["task"] + " - " + task["category"])

        if all(task["done"] for task in tasks.values()):
            print("All tasks are marked as done.")
    else:
        print("There are no current tasks.")


def completeTask():  # a function that marks a task as (done)
    if len(tasks) == 0:
        print("The are no current tasks to be marked as done")
    else:
        # checkTask() if you want to see the tasks even if they are done; the one bellow will only show the ones not marked as done
        for i, task in tasks.items():
            if not task["done"]:  # or we can just say ' if task["done"] == False '
                print(f"Task #{i} : " + task["task"])
        try:
            if not all(task["done"] for task in tasks.values()):
                d = int(input("Select which task to be marked as Done: "))
                if 1 <= d <= len(tasks):
                    tasks[d]["done"] = True
                    print(f"The task #{d} ({tasks[d]['task']}) has been marked as Done")
                else:
                    print("Invalid task number. No task has been marked as Done.")
                    completeTask()
            else:
                print("Tasks are all marked as done.")

        except ValueError:
            print("Invalid Input. Try Again.")
            completeTask()


def deleteTask():  # a function that deletes a task from the list, weather it is done or not
    if len(tasks) == 0:
        print("There are no task to be deleted")
    else:
        checkTask()
        try:
            d = int(input("Select which task to be Deleted: "))
            if 1 <= d <= len(tasks):
                del tasks[d]
                print(f"The task #{d} has been Deleted")
            else:
                print("Invalid task number. No task has been deleted.")
                deleteTask()

        except ValueError:
            print("Invalid Input. Try Again.")
            deleteTask()


if __name__ == "__main__":
    print("Welcome to the To do list :")
    while True:
        print("-----------------------------------")
        print("Please select one of these choices:")
        print("-----------------------------------")
        print("1.Check your list")
        print("2.Add Task")
        print("3.Complete Task")
        print("4.Delete Task")
        print("5.Quit")

        try:
            choice = int(input("Select your choice: "))
            if choice == 1:
                checkTask()
            elif choice == 2:
                addTasks()
            elif choice == 3:
                completeTask()
            elif choice == 4:
                deleteTask()
            elif choice == 5:
                break
            else:
                print("invalid choice, please select again")

        except ValueError:
            print("Invalid input. Please enter a valid task number.")

    print("Thank you. Goodbye.")
