tasklist = []
done = []


def addTasks():  # a function that adds a task to the list
    t = input("Insert your task here: ")
    tasklist.append(t)
    print("The task has been added to the list.")


def checkTask():  # a function that checks if there are tasks, or if they are done or not
    if len(tasklist) != 0:
        print("The Current Tasks are:")
        count = 0
        for i in range(len(tasklist)):
            if count in done:
                print(f"Task #{i + 1} : " + tasklist[i] + " (done)")
            else:
                print(f"Task #{i + 1} : " + tasklist[i])
            count += 1

        if len(tasklist) == len(done) and len(tasklist) != 0:
            print("All tasks are marked as done.")
    else:
        print("There are no current tasks.")


def completeTask():  # a function that marks a task as (done)
    if len(tasklist) == 0 or len(tasklist) == len(done):
        print("The are no current tasks to be marked as done")
    else:
        for i in range(len(tasklist)):
            if i not in done:
                print(f"Task #{i + 1}: " + tasklist[i])

        d = int(input("Select which task to be marked as Done: "))
        done.append(d - 1)

        print(f"The task #{d} ({tasklist[d - 1]}) has been marked as Done")


def deleteTask():  # a function that deletes a task from the list, weather it is done or not
    if len(tasklist) == 0:
        print("There aare no task to br deleted")
    else:
        for i in range(len(tasklist)):
            print(f"Task #{i + 1}: " + tasklist[i])

        d = int(input("Select which task to be marked as Done: "))
        tasklist.remove(tasklist[d - 1])
        print(f"The task #{d} has been Deleted")

        if d in done:
            done.remove(d)


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

print("Thank you. Goodbye.")
