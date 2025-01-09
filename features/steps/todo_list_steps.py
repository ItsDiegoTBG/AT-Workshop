from behave import given, when, then
from todo_list import ToDoList

@given("the to-do list is empty")
def step_given_todo_list_empty(context):
    context.todo_list = ToDoList()

@when('the user adds a task "{task_description}"')
def step_when_user_adds_task(context, task_description):
    context.todo_list.add_task(task_description)

@then('the to-do list should contain "{task_description}"')
def step_then_todo_list_should_contain(context, task_description):
    tasks = [task.description for task in context.todo_list.list_tasks()]
    assert task_description in tasks

@given('the to-do list contains tasks:')
def step_given_todo_list_contains_tasks(context):
    context.todo_list = ToDoList()
    for row in context.table:
        context.todo_list.add_task(row['Task'])

@when("the user lists all tasks")
def step_when_user_lists_all_tasks(context):
    context.tasks = context.todo_list.list_tasks()

@then("the output should contain:")
def step_then_output_should_contain(context):
    output = "\n".join(f"- {task.description}" for task in context.tasks)
    assert context.text.strip() in output

@when('the user marks task "{task_description}" as completed')
def step_when_user_marks_task_completed(context, task_description):
    context.todo_list.mark_task_completed(task_description)

@then('the to-do list should show task "{task_description}" as completed')
def step_then_todo_list_should_show_task_completed(context, task_description):
    task = next(task for task in context.todo_list.list_tasks() if task.description == task_description)
    assert task.status == "Completed"

@when("the user clears the to-do list")
def step_when_user_clears_todo_list(context):
    context.todo_list.clear_tasks()

@then("the to-do list should be empty")
def step_then_todo_list_should_be_empty(context):
    assert len(context.todo_list.list_tasks()) == 0


# 2 extra

@when('the user tries to add a task with an empty description')
def step_when_user_adds_empty_task(context):
    try:
        context.todo_list.add_task("")
    except ValueError as e:
        context.error_message = str(e)

@then('the system should display an error message "{message}"')
def step_then_system_displays_error_message(context, message):
    assert context.error_message == message

@when('the user tries to mark task "{task_description}" as completed')
def step_when_user_marks_nonexistent_task_completed(context, task_description):
    try:
        context.todo_list.mark_task_completed(task_description)
    except ValueError as e:
        context.error_message = str(e)

@then('the to-do list should remain unchanged')
def step_then_todo_list_remains_unchanged(context):
    tasks_before = getattr(context, "tasks_before", [])
    tasks_after = context.todo_list.list_tasks()
    assert tasks_before == tasks_after
