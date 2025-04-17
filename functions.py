import json
import os
from time import strftime


def create_json():
    path = './data.json'
    if os.path.isfile(path) == False:
        with open('data.json', 'w') as f:
            json.dump([], f)


def add_task(description: str):
    id = give_id()

    data = {
    "id": id,
    "description": description,
    "status": "todo",
    "createdAt": strftime("%Y-%m-%d %H:%M:%S"),
    "updatedAt": None
    }

    with open('data.json') as f:
        current_data = json.load(f)

    current_data.append(data)

    result = current_data

    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=4)

    print(f"Task added successfully (ID: {id})")
    

def give_id() -> int:
    with open('data.json') as f:
        current_data = json.load(f)

        if current_data == []:
            return 1
        else:
            return current_data[-1]["id"] + 1
        

def update_task(id:int, description:str):
    with open('data.json') as f:
        current_data = json.load(f)

    flag = "not found"

    for task in current_data:
        if task["id"] == int(id):
            task["description"] = description
            task["updatedAt"] = strftime("%Y-%m-%d %H:%M:%S")
            flag = "found"

    if flag == "not found":
        print("task with this id is not exist")
        return

    result = current_data

    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=4)

    print(f"Task updated successfully (ID: {id}, DESCRIPTION: {description})")


def delete_task(id: int):
    with open('data.json') as f:
        current_data = json.load(f)

    flag = "not found"    

    for i in range(len(current_data)):
        if current_data[i]["id"] == id:
            del current_data[i]
            flag = "found"
            break

    if flag == "not found":
        print("task with this id is not exist")
        return 

    result = current_data

    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=4)    


    print(f"task removed successfully (ID: {id})")


def change_task_status(id: int, status: str):
    with open('data.json') as f:
        current_data = json.load(f)

    flag = "not found"

    for task in current_data:
        if task["id"] == int(id):
            task["status"] = status
            task["updatedAt"] = strftime("%Y-%m-%d %H:%M:%S")
            flag = "found"

    if flag == "not found":
        print("task with this id is not exist")
        return

    result = current_data

    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=4)

    print(f"Task status updated successfully (ID: {id}, STATUS: {status})")


def show_tasks(filter:str=None):
    with open('data.json') as f:
        current_data = json.load(f)
    
    if filter == None:
        for task in current_data:
            print(task)
    elif filter == "todo":
        for task in current_data:
            if task["status"] == "todo":
                print(task)
    elif filter == "in-progress":
        for task in current_data:
            if task["status"] == "in-progress":
                print(task)
    elif filter == "done":
        for task in current_data:
            if task["status"] == "done":
                print(task)