from time import strftime
import json
import os


def create_json():
    path = './data.json'
    if os.path.isfile(path) == False:
        with open('data.json', 'w') as f:
            json.dump([], f)


class Task:
    def __init__(self, id, description, status="todo", createdAt=None, updatedAt=None):
        self.id = id
        self.description = description
        self.status = status
        self.createdAt = createdAt or strftime("%Y-%m-%d %H:%M:%S")
        self.updatedAt = updatedAt

    
    def update_description(self, new_description):
        self.description = new_description
        self.updatedAt = strftime("%Y-%m-%d %H:%M:%S")


    def change_status(self, new_status):
        self.status = new_status
        self.updatedAt = strftime("%Y-%m-%d %H:%M:%S")
    

    # return dict with class values
    def to_dict(self):
        result = {
            "id": self.id,
            "description": self.description,
            "status": self.status,
            "createdAt": self.createdAt,
            "updatedAt": self.updatedAt
        }
        return result
    
        
    # return a class with the passed values
    @classmethod
    def from_dict(cls, json_task):
        task = cls(
            id=json_task["id"],
            description=json_task["description"],
            status=json_task["status"],
            createdAt=json_task["createdAt"],
            updatedAt=json_task["updatedAt"]
        )
        return task



class TaskManager:
    def __init__(self):
        self.filepath = "data.json"
        self.tasks = self.load_tasks()


    # return [<__main__.Task object at 0x742ea0175f70>, <__main__.Task object at 0x742ea01763f0>...]
    def load_tasks(self):
        tasks_list = []

        with open(self.filepath) as f:
            for task in json.load(f):
                tasks_list.append(Task.from_dict(task))
            
            return tasks_list
        

    # save tasks to json
    def save_tasks(self):
        with open(self.filepath, 'w', encoding='utf-8') as f:
            tasks_list = []

            for task in self.tasks:
                tasks_list.append(task.to_dict())

            json.dump(tasks_list, f, ensure_ascii=False, indent=4)
    

    def add_task(self):
        pass


    def get_next_id(self):
        pass


    def update_task(self, id, description):
        task = self.find_task(id)

        if task:
            task.update_description(description)
            self.save_tasks()
            print(f"Task updated (ID: {id})")
        else:
            print("Task not found.")


    def delete_task(self, id):
        pass


    def change_task_status(self, id):
        pass


    def show_task(self, filter):
        pass


    def find_task(self, id):
        for task in self.tasks:
            if task.id == id:
                return task
        return None

# manager.update_task(1, '123') # worked
# manager = TaskManager()