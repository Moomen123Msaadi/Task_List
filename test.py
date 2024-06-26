from unittest.mock import patch
from Task_List import addTasks, tasks, completeTask, checkTask, deleteTask, random_task, mark_unDone


def test_addTasks(capsys):
    # Here we are mocking an input (which means putting a fake input) for a task called 'New Task'
    # We are testing the length of the list, and the content of the first slot we filled

    tasks.clear()  # Clearing the list of tasks before the test
    with patch('builtins.input', return_value='New Task'):
        addTasks()

    captured = capsys.readouterr()  # this line here was only added to not display 'The task has been added to the list.' when testing

    assert len(tasks) == 1
    assert tasks[1]['task'] == 'New Task'


# Note:
# capsys.readouterr(): This captures the output printed to stdout during the function execution.


def test_checkTask_no_tasks(
        capsys):  # Needs further modification to capture the printed output instead of the list converted into string
    tasks.clear()  # Clear tasklist before the tes

    # Call the function
    checkTask()
    captured = capsys.readouterr()
    assert captured.out.strip() == "There are no current tasks."


def test_checkTask_with_tasks(capsys):
    # Test when there are tasks
    tasks.clear()
    tasks.update({
        1: {"task": "Task 1", "done": False, "category": ""},
        2: {"task": "Task 2", "done": False, "category": ""},
        3: {"task": "Task 3", "done": False, "category": ""}
    })
    checkTask()
    captured = capsys.readouterr()

    assert captured.out.strip() == ('The Current Tasks are:\n'
                                    'Task #1 : Task 1 \n'
                                    'Task #2 : Task 2 \n'
                                    'Task #3 : Task 3 \n'
                                    'Tasks done: 0.0%')


def test_checkTask_marked_asDone(capsys):
    # Test when some tasks are marked as done
    tasks.clear()  # Clearing the tasklist so that it does not get tangled with the results from the other function
    tasks.update({
        1: {"task": "Task 1", "done": True, "category": ""},
        2: {"task": "Task 2", "done": False, "category": ""},
        3: {"task": "Task 3", "done": True, "category": ""}
    })
    checkTask()
    captured = capsys.readouterr()
    assert captured.out.strip() == ("The Current Tasks are:\n"
                                    "Task #1 : Task 1 (done) \n"
                                    "Task #2 : Task 2 \n"
                                    "Task #3 : Task 3 (done) \n"
                                    "Tasks done: 66.66666666666666%")


def test_completeTask_no_tasks(capsys):
    # Clear tasklist and done list before the test
    tasks.clear()

    completeTask()
    captured = capsys.readouterr()
    assert "The are no current tasks to be marked as done" in captured.out


def test_completeTask_all_tasks_alreadyDone(capsys):
    # Clear tasklist and done list before the test
    tasks.clear()
    tasks.update({
        1: {"task": "Task 1", "done": True},
        2: {"task": "Task 2", "done": True},
        3: {"task": "Task 3", "done": True}
    })
    completeTask()
    captured = capsys.readouterr()
    assert "Tasks are all marked as done." in captured.out


def test_completeTask_with_tasksDone(capsys):
    # A test that checks if it is possible to complete tasks even if some of them are marked as done
    tasks.clear()
    tasks.update({
        1: {"task": "Task1", "done": True},
        2: {"task": "Task2", "done": False},
        3: {"task": "Task3", "done": True},
        4: {"task": "Task4", "done": False}
    })

    # We are marking the second task called "Task2" as done
    with patch('builtins.input', return_value='2'):
        completeTask()
    captured = capsys.readouterr()

    assert captured.out == ("Task #2 : Task2\n"
                            "Task #4 : Task4\n"
                            "The task #2 (Task2) has been marked as Done\n")


def test_completeTask_already_Done(capsys):
    # A test that checks if it is possible to complete tasks even if some of them are marked as done
    tasks.clear()
    tasks.update({
        1: {"task": "Task1", "done": True},
        2: {"task": "Task2", "done": True},
        3: {"task": "Task3", "done": True},
        4: {"task": "Task4", "done": False}
    })

    # We are marking the second task called "Task2" as done
    with patch('builtins.input', return_value='2'):
        completeTask()
    captured = capsys.readouterr()

    assert captured.out == ("Task #4 : Task4\n"
                            "The task #2 (Task2) has been marked as Done\n")


def test_deleteTask_with_noTasks(capsys):
    tasks.clear()
    deleteTask()

    captured = capsys.readouterr()

    assert "There are no task to be deleted\n" == captured.out


def test_deleteTask_with_tasks(capsys):
    tasks.clear()
    tasks.update({
        1: {"task": "Task1", "done": False, "category": ""},
        2: {"task": "Task2", "done": False, "category": ""},
        3: {"task": "Task3", "done": False, "category": ""}
    })

    with patch('builtins.input', return_value='2'):
        deleteTask()

    captured = capsys.readouterr()

    assert ("The Current Tasks are:\n"
            "Task #1 : Task1 \n"
            "Task #2 : Task2 \n"
            "Task #3 : Task3 \n"
            "Tasks done: 0.0%\n"
            "The task #2 has been Deleted\n") == captured.out


def test_deleteTask_with_done_tasks(capsys):
    tasks.clear()

    tasks.update({
        1: {"task": "Task1", "done": True, "category": ""},
        2: {"task": "Task2", "done": False, "category": ""},
        3: {"task": "Task3", "done": False, "category": ""}
    })

    with patch('builtins.input', return_value='1'):
        deleteTask()

    captured = capsys.readouterr()

    assert ("The Current Tasks are:\n"
            "Task #1 : Task1 (done) \n"
            "Task #2 : Task2 \n"
            "Task #3 : Task3 \n"
            "Tasks done: 33.33333333333333%\n"
            "The task #1 has been Deleted\n") == captured.out


def test_random_task_with_no_tasks(capsys):
    tasks.clear()

    random_task()

    captured = capsys.readouterr()

    assert captured.out == "There are no tasks right now.\n"


def test_random_task_with_one_task(capsys):
    tasks.clear()

    tasks.update({
        1: {"task": "Task1", "done": False, "category": ""},
    })

    random_task()

    captured = capsys.readouterr()
    nbr = list(tasks.keys())[0]
    assert captured.out == f"There is only one task which is Task #{nbr}: {list(tasks.values())[0]['task']}.\n"


def test_random_task_with_tasks(capsys):
    tasks.clear()

    tasks.update({
        1: {"task": "Task1", "done": False, "category": ""},
        2: {"task": "Task2", "done": False, "category": ""},
        3: {"task": "Task3", "done": False, "category": ""}
    })

    random_task()

    captured = capsys.readouterr()

    assert (captured.out == f"Random Task: #1: Task1\n"
            or captured.out == f"Random Task: #2: Task2\n"
            or captured.out == f"Random Task: #3: Task3\n")


def test_markUndone_no_tasks(capsys):
    tasks.clear()

    mark_unDone()

    captured = capsys.readouterr()

    assert (captured.out == f"The are no current tasks to be Unmarked\n")


def test_markUndone_all_tasks_undone(capsys):
    tasks.clear()

    tasks.update({
        1: {"task": "Task1", "done": False, "category": ""},
        2: {"task": "Task2", "done": False, "category": ""},
        3: {"task": "Task3", "done": False, "category": ""}
    })

    mark_unDone()

    captured = capsys.readouterr()

    assert (captured.out == f"All tasks are Unmarked.\n")


def test_markUndone_all_tasks_done(capsys):
    tasks.clear()

    tasks.update({
        1: {"task": "Task1", "done": True, "category": ""},
        2: {"task": "Task2", "done": True, "category": ""},
        3: {"task": "Task3", "done": True, "category": ""}
    })

    with patch('builtins.input', return_value='1'):
        mark_unDone()

    captured = capsys.readouterr()

    assert (captured.out == f"Task #1 : Task1\n"
                            "Task #2 : Task2\n"
                            "Task #3 : Task3\n"
                            "The task #1 (Task1) has been Unmarked\n")

def test_markUndone_some_tasks(capsys):
    tasks.clear()

    tasks.update({
        1: {"task": "Task1", "done": False, "category": ""},
        2: {"task": "Task2", "done": True, "category": ""},
        3: {"task": "Task3", "done": False, "category": ""}
    })

    with patch('builtins.input', return_value='1'):
        mark_unDone()

    captured1 = capsys.readouterr()

    with patch('builtins.input', return_value='2'):
        mark_unDone()

    captured2 = capsys.readouterr()

    assert (captured1.out == f"Task #2 : Task2\n"
                             f"The task has yet to be Unmarked. Choose another task.\n")

    assert (captured2.out == f"Task #2 : Task2\n"
                             f"The task #2 (Task2) has been Unmarked\n")

