tasks_db = []


def add_task(user_id, task):
    task_id = len(tasks_db) + 1
    tasks_db.append({"id": task_id, "user_id": user_id, "description": task, "status": "pending"})
    return task_id


def list_tasks(user_id):
    return [task for task in tasks_db if task["user_id"] == user_id]


def edit_task(user_id, task_id, new_description):
    for task in tasks_db:
        if task["id"] == int(task_id) and task["user_id"] == user_id:
            task["description"] = new_description
            return True
    return False


def delete_task(user_id, task_id):
    for task in tasks_db:
        if task["id"] == int(task_id) and task["user_id"] == user_id:
            tasks_db.remove(task)
            return True
    return False
