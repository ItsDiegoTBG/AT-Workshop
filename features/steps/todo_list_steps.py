# features/steps/todo_list_steps.py
from behave import given, when, then
from todo_list import ToDoList

to_do_list = ToDoList()

@given('the to-do list is empty')
def step_impl(context):
    to_do_list.tasks = []

@given('the to-do list contains tasks')
def step_impl(context):
    to_do_list.tasks = [{"task": row["Task"], "status": "Pending"} for row in context.table]

@when('the user adds a task "{task}"')
def step_impl(context, task):
    to_do_list.add_task(task)

@when('the user lists all tasks')
def step_impl(context):
    context.output = to_do_list.list_tasks()

@when('the user marks task "{task}" as completed')
def step_impl(context, task):
    to_do_list.mark_as_completed(task)

@when('the user clears the to-do list')
def step_impl(context):
    to_do_list.clear_list()

@then('the to-do list should contain "{task}"')
def step_impl(context, task):
    tasks = to_do_list.list_tasks()
    assert task in tasks, f'Task "{task}" not found in the to-do list'

@then('the output should contain')
def step_impl(context):
    tasks = to_do_list.list_tasks()
    for row in context.table:
        assert row["Task"] in tasks, f'Task "{row["Task"]}" not found in the to-do list'

@then('the to-do list should show task "{task}" as completed')
def step_impl(context, task):
    for t in to_do_list.tasks:
        if t["task"] == task:
            assert t["status"] == "Completed", f'Task "{task}" is not completed'
            return
    assert False, f'Task "{task}" not found in the to-do list'

@then('the to-do list should be empty')
def step_impl(context):
    tasks = to_do_list.list_tasks()
    assert len(tasks) == 0, f'To-do list is not empty, it contains: {tasks}'

@then('the to-do list should show an error "{error}"')
def step_impl(context, error):
    # Check that the task isn't in the list and an error is returned
    assert error in context.output, f'Expected error: "{error}" not found'

@then('the to-do list should contain "{task}" twice')
def step_impl(context, task):
    tasks = to_do_list.list_tasks()
    assert tasks.count(task) == 2, f'Task "{task}" is not in the list twice'
