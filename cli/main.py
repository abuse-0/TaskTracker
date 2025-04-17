# python3 main.py create_json
# python3 main.py -h
# python3 main.py add 'xd'
# python3 main.py update 1 'xd1'
# python3 main.py delete 1
# python3 main.py mark-todo 1
# python3 main.py mark-in-progress 1
# python3 main.py mark-done 1
# python3 main.py list ''/'todo'/'in-progress'/'done'

import argparse
import task_manager as tm

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest="command")


# what is this?

add_parser = subparsers.add_parser("add",
                                   help="add task | example: add 'some task'")
add_parser.add_argument("description", type=str)


update_parser = subparsers.add_parser("update",
                                      help="update task, required id, desc | example: update 1 'some task'")
update_parser.add_argument("id", type=int)
update_parser.add_argument("description", type=str)


delete_parser = subparsers.add_parser("delete", 
                                      help="delete task at id | example: delete 1")
delete_parser.add_argument("id", type=int)


mark_todo_parser = subparsers.add_parser("mark-todo", 
                                                help="make task status to todo | example mark-todo 1")
mark_todo_parser.add_argument("id", type=int)


mark_in_progress_parser = subparsers.add_parser("mark-in-progress", 
                                                help="make task status to todo | example mark-in-progress 1")
mark_in_progress_parser.add_argument("id", type=int)


mark_done = subparsers.add_parser("mark-done", 
                                  help="make task status to todo | example: mark-done 1")
mark_done.add_argument("id", type=int)


list_parser = subparsers.add_parser("list",
                                    help="view items | example: list / list todo / list in-progress / list done")
list_parser.add_argument("filter", nargs="?",choices=["todo", "in-progress", "done"]) 


# commands 

def main():
# Надо open(always executed)
    args = parser.parse_args() 
    print(args)
    tm.create_json()

    manager = tm.TaskManager()
# close
    if args.command == "add":
        description = args.description
        manager.add_task(description)
    elif args.command == "update":
        id = args.id
        description = args.description
        manager.update_task(id, description)
    elif args.command == "delete":
        id = args.id
        manager.delete_task(id)
    elif args.command == "mark-todo":
        id = args.id
        manager.change_task_status(id, "todo")
    elif args.command == "mark-in-progress":
        id = args.id
        manager.change_task_status(id, "in-progress")
    elif args.command == "mark-done":
        id = args.id
        manager.change_task_status(id, "done")
    elif args.command == "list":
        if args.filter == "todo":
            manager.show_tasks("todo")
        elif args.filter == "in-progress":
            manager.show_tasks("in-progress")
        elif args.filter == "done":
            manager.show_tasks("done")
        else:
            manager.show_tasks()


if __name__ == "__main__":
    main()