class Task:
    def __init__(self, name, description, due_date):
        self.name = name
        self.description = description
        self.due_date = due_date

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)

    def display_tasks(self):
        for task in self.tasks:
            print(f'Name: {task.name}')
            print(f'Description: {task.description}')
            print(f'Due Date: {task.due_date}')
            print()

manager = TaskManager()

task1 = Task("Buy groceries", "Pick up milk, bread, and eggs from the store", "2022-01-01")
task2 = Task("Write report", "Write a report on the benefits of task management", "2022-01-15")

manager.add_task(task1)
manager.add_task(task2)

manager.display_tasks()
