

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "status": "Pending"})

    def list_tasks(self):
        return [task["task"] for task in self.tasks]

    def mark_as_completed(self, task):
        for t in self.tasks:
            if t["task"] == task:
                t["status"] = "Completed"

    def clear_list(self):
        self.tasks = []
