import datetime

class Task:
    def __init__(self, description):
        self.id = id(self)
        self.description = description
        self.status = "Pending"
        self.created_at = datetime.datetime.now()

    def mark_as_completed(self):
        self.status = "Completed"

    def __str__(self):
        return f"[{self.status}] {self.description} (Created at: {self.created_at})"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)
        return task

    def list_tasks(self):
        return self.tasks

    def mark_task_completed(self, description):
        for task in self.tasks:
            if task.description == description:
                task.mark_as_completed()
                return task
        raise ValueError("Task not found")

    def clear_tasks(self):
        self.tasks.clear()

    def add_task(self, description):
        if not description.strip():
            raise ValueError("Task description cannot be empty")
        task = Task(description)
        self.tasks.append(task)
        return task

    def mark_task_completed(self, description):
        for task in self.tasks:
            if task.description == description:
                task.mark_as_completed()
                return task
        raise ValueError("Task not found")


# Example usage:
if __name__ == "__main__":
    todo_list = ToDoList()
    todo_list.add_task("Buy groceries")
    todo_list.add_task("Pay bills")
    for task in todo_list.list_tasks():
        print(task)