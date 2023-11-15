# https://twitter.com/cassidoo/status/1723954160058462637
# https://buttondown.email/cassidoo/archive/mellow-doesnt-always-make-for-a-good-story-but-it/

tasks = [
    {"name": 'Task 1', "duration": 4},
    {"name": 'Task 2', "duration": 2},
    {"name": 'Task 3', "duration": 7},
    {"name": 'Task 4', "duration": 5},
    {"name": 'Task 5', "duration": 1},
    {"name": 'Task 6', "duration": 3}]

def get_duration(task):
    return task["duration"]

def do_tasks(tasks, time_to_work):
    sorted_tasks = sorted(tasks, key=get_duration)
    tasks_completed_names = []
    for task in sorted_tasks:
        if task["duration"] <= time_to_work:
            tasks_completed_names.append(task["name"])
            time_to_work -= task["duration"]

    results = []
    for task in tasks:
        if task["name"] in tasks_completed_names:
            results.append(task["name"])
    return results

assert do_tasks(tasks, 6) == ["Task 2", "Task 5", "Task 6"]
assert do_tasks(tasks, 0) == []
