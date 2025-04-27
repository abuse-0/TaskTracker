# pytest .\tests\test_task_manager.py
import os
import json
import pytest

from time import strftime

from cli import task_manager

'''
Го все наверн покроем тестами, по другому и не научиться
'''

@pytest.fixture(autouse=True)  # Автоматически применяется ко всем тестам
def clean_env(tmp_path):
    """Удаляет data.json перед каждым тестом."""
    os.chdir(tmp_path)
    if os.path.exists("data.json"):
        os.remove("data.json")
    yield 


def test_create_json(tmp_path):
    """
    Ориг функция:
    - объявляет путь до файла './data.json'
    - проверяет, что такого файла нет
    - создает такой файл с наполнением в виде []
    """
    os.chdir(tmp_path) # temporary directory
    assert not os.path.exists('data.json')
    task_manager.create_json()
    assert os.path.exists('data.json')
    with open('data.json', 'r') as f:
        content = json.load(f)
    assert content == []


def test_Task_create():
    id = 1
    desc = 'Купить пива'
    time = strftime("%Y-%m-%d %H:%M:%S")
    task = task_manager.Task(id, desc)
    assert task.id == id
    assert task.description == desc
    assert task.status == "todo"
    assert task.createdAt == time
    assert task.updatedAt == None


def test_Task_update_description():
    task = task_manager.Task(1, 'Купить пива')
    assert task.description == 'Купить пива'

    task.update_description('Не купить пива')
    time = strftime("%Y-%m-%d %H:%M:%S")

    assert task.description == 'Не купить пива'
    assert task.updatedAt == time


def test_Task_change_task_status():
    task = task_manager.Task(1, 'Купить пива')
    assert task.status == "todo"

    task.change_status('done')
    time = strftime("%Y-%m-%d %H:%M:%S")

    assert task.status == 'done'
    assert task.updatedAt == time


def test_Task_to_dict():
    task = task_manager.Task(1, 'Купить пива')
    time = strftime("%Y-%m-%d %H:%M:%S")
    result = task.to_dict()
    check_result = {"id": 1, "description": 'Купить пива', "status": 'todo', "createdAt": time, "updatedAt": None}

    assert result == check_result


def test_Task_from_dict():
    task_from_dict = {"id": 1, "description": 'Купить пива', "status": 'todo', "createdAt": '2025-04-22 16:16:59', "updatedAt": None}

    cls_task = task_manager.Task.from_dict(task_from_dict)

    assert cls_task.id == 1 
    assert cls_task.description == 'Купить пива' 
    assert cls_task.status == 'todo'  
    assert cls_task.createdAt == '2025-04-22 16:16:59'
    assert cls_task.updatedAt == None


def test_TaskManager_load_tasks(tmp_path):
    data = [{"id": 1, "description": 'Купить пива', "status": 'todo', "createdAt": '2025-04-22 16:16:59', "updatedAt": None}, 
            {"id": 2, "description": 'Подкачаться', "status": 'todo', "createdAt": '2025-04-22 17:36:23', "updatedAt": None}]
    
    os.chdir(tmp_path)
    with open('data.json', 'w') as f:
            json.dump(data, f)

    manager = task_manager.TaskManager()

    tasks_list = manager.load_tasks()

    assert tasks_list[0].id == 1
    assert tasks_list[0].description == 'Купить пива'
    assert tasks_list[0].status == 'todo'
    assert tasks_list[0].createdAt == '2025-04-22 16:16:59'
    assert tasks_list[0].updatedAt == None

    assert tasks_list[1].id == 2
    assert tasks_list[1].description == 'Подкачаться'
    assert tasks_list[1].status == 'todo'
    assert tasks_list[1].createdAt == '2025-04-22 17:36:23'
    assert tasks_list[1].updatedAt == None


def test_TaskManager_save_tasks(tmp_path):
    os.chdir(tmp_path)

    with open('data.json', 'w') as f:
            json.dump([], f)

    manager = task_manager.TaskManager()

    task = task_manager.Task(1, 'Купить пива')

    manager.tasks.append(task)

    os.chdir(tmp_path)

    manager.save_tasks()

    with open('data.json', 'r', encoding='utf-8') as f:
        content = json.load(f)

    assert content[0]["id"] == 1
    assert content[0]["description"] == 'Купить пива'



def test_TaskManager_get_next_id_if_empty(tmp_path):
    os.chdir(tmp_path)

    with open('data.json', 'w') as f:
            json.dump([], f)

    manager = task_manager.TaskManager()
    id = manager.get_next_id()

    assert id == 1


def test_TaskManager_get_next_id(tmp_path):
    os.chdir(tmp_path)

    with open('data.json', 'w') as f:
            json.dump([{"id": 1, "description": 'Купить пива', "status": 'todo', "createdAt": '2025-04-22 16:16:59', "updatedAt": None}], f)

    manager = task_manager.TaskManager()
    id = manager.get_next_id()

    assert id == 2


def test_TaskManager_find_task(tmp_path):
    os.chdir(tmp_path)

    data = [{"id": 1, "description": 'Купить пива', "status": 'todo', "createdAt": '2025-04-22 16:16:59', "updatedAt": None},
            {"id": 2, "description": 'Рассказать прикол', "status": 'todo', "createdAt": '2025-04-22 16:16:59', "updatedAt": None},
            {"id": 3, "description": 'Поспать', "status": 'todo', "createdAt": '2025-04-22 16:16:59', "updatedAt": None}]

    with open('data.json', 'w') as f:
        json.dump(data, f)

    manager = task_manager.TaskManager()

    found_task = manager.find_task(2)

    assert manager.find_task(0) == None
    assert manager.find_task(999999999999) == None

    assert found_task.id == data[1]["id"]
    assert found_task.description == data[1]["description"]
    assert found_task.status == data[1]["status"]
    assert found_task.createdAt == data[1]["createdAt"]
    assert found_task.updatedAt == data[1]["updatedAt"]

    
    