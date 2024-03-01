import pytest

from unittest.mock import patch
from Task_List import addTasks, tasklist, done, checkTask


def test_addTasks():
    # Here we are mocking an input (which means putting a fake input) for a task called 'New Task'
    # We are testing the length of the list, and the content of the first slot we filled
    tasklist.clear() # Clearing the list of tasks before the test
    with patch('builtins.input', return_value='New Task'):
        addTasks()
    assert len(tasklist) == 1
    assert tasklist[0] == 'New Task'

# Note:
# capsys.readouterr(): This captures the output printed to stdout during the function execution.

def test_checkTask_no_tasks(capsys): # Needs further modification to capture the printed output instead of the list converted into string
    tasklist.clear()  # Clear tasklist before the test
    done.clear()  # Clear done list before the test

    # Call the function
    checkTask()

    captured = capsys.readouterr()
    assert captured.out.strip() == "There are no current tasks."
def test_checkTask_with_tasks(capsys):
    # Test when there are tasks
    tasklist.extend(["Task 1", "Task 2", "Task 3"])
    checkTask()
    captured = capsys.readouterr()
    assert captured.out.strip() == "The Current Tasks are:\nTask #1 : Task 1\nTask #2 : Task 2\nTask #3 : Task 3"

def test_checkTask_marked_asDone(capsys):
    # Test when some tasks are marked as done
    tasklist.clear() # Clearing the tasklist so that it does not get tangled with the results from the other function
    tasklist.extend(["Task 1", "Task 2", "Task 3"])
    done.extend([0, 2])  # Mark Task 1 and Task 3 as done
    checkTask()
    captured = capsys.readouterr()
    assert captured.out.strip() == "The Current Tasks are:\nTask #1 : Task 1 (done)\nTask #2 : Task 2\nTask #3 : Task 3 (done)"
