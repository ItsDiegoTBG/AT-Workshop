# features/todo_list.feature

Feature: To-Do List Management
  As a user, I want to manage my tasks so that I can stay organized.

  Scenario: Add a task to the to-do list
    Given the to-do list is empty
    When the user adds a task "Buy groceries"
    Then the to-do list should contain "Buy groceries"

  Scenario: List all tasks in the to-do list
    Given the to-do list contains tasks:
      | Task           |
      | Buy groceries  |
      | Pay bills      |
    When the user lists all tasks
    Then the output should contain:
      | Task           |
      | Buy groceries  |
      | Pay bills      |

  Scenario: Mark a task as completed
    Given the to-do list contains tasks:
      | Task           | Status  |
      | Buy groceries  | Pending |
    When the user marks task "Buy groceries" as completed
    Then the to-do list should show task "Buy groceries" as completed

  Scenario: Clear the entire to-do list
    Given the to-do list contains tasks:
      | Task           |
      | Buy groceries  |
      | Pay bills      |
    When the user clears the to-do list
    Then the to-do list should be empty

  # New Scenario 1: Try to mark a non-existent task as completed
  Scenario: Mark a non-existent task as completed
    Given the to-do list contains tasks:
      | Task           | Status  |
      | Buy groceries  | Pending |
    When the user marks task "Go to the gym" as completed
    Then the to-do list should show an error "Task 'Go to the gym' not found"

  # New Scenario 2: Try to add a duplicate task
  Scenario: Add a duplicate task to the to-do list
    Given the to-do list contains tasks:
      | Task           |
      | Buy groceries  |
    When the user adds a task "Buy groceries"
    Then the to-do list should contain "Buy groceries" twice
