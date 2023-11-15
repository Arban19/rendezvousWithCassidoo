tasks = [
    {"name": 'Task 1', "duration": 4},
    {"name": 'Task 2', "duration": 2},
    {"name": 'Task 3', "duration": 7},
    {"name": 'Task 4', "duration": 5},
    {"name": 'Task 5', "duration": 1},
    {"name": 'Task 6', "duration": 3}]

def get_duration(task):
    return task["duration"]
get_duration({"name": "Task 1", "duration": 12})

def doTasks(tasks, time_to_work):
    sorted_tasks = sorted(tasks, key=get_duration)
    tasks_completed = []
    for task in sorted_tasks:
        if task["duration"] <= time_to_work:
            tasks_completed.append(task["name"])
            time_to_work -= task["duration"]
    return sorted(tasks_completed)

print(doTasks(tasks,6))





# > doTasks(tasks, timeToWork)
# > ['Task 2', 'Task 5', 'Task 6']
