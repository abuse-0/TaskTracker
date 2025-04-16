import json
import os
from time import strftime

class Task:
    def __init__(self, id, description, status, createdAt, updatedAt):
        self.id = id
        self.description = description
        self.status = "todo"
        self.createdAt = createdAt or strftime("%Y-%m-%d %H:%M:%S")
        self.updatedAt = None

    def load_from_json():
        with open('data.json') as f:
            data = json.load(f)

        result = []

        for task in data:
            result.append(Task(id=task["id"], description=task["description"], status=task['status'], createdAt=task['createdAt'], updatedAt=task['updatedAt']))

        return result
        

class TaskManager:
    def __init__(self):
        if os.path.isfile('./data.json') == False:
            with open('data.json', 'w') as f:
                json.dump([], f)

        self.tasks = Task.load_from_json() 

    def give_id(self) -> int:
        if self.tasks == []:
            return 0
        else:
            return self.tasks[-1].id +1
        
    def add_task(self, description):
        id = self.give_id()
        self.tasks.append(Task(id, description))
        print(self.tasks)

manager = TaskManager()

print(manager.add_task("negr"))

Task.load_from_json()

