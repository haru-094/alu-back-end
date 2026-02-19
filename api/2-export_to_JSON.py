#!/usr/bin/python3
"""
get all the data from file that gather the data then
export in format of json.
"""
import json
import sys
import urllib.request


if __name__ == "__main__":
    emp_id = int(sys.argv[1])

    user_url = (
        "https://jsonplaceholder.typicode.com/users/{}".format(emp_id)
    )
    with urllib.request.urlopen(user_url) as response:
        user = json.loads(response.read().decode())
    username = user.get("username")

    todos_url = (
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(
            emp_id
        )
    )
    with urllib.request.urlopen(todos_url) as response:
        todos = json.loads(response.read().decode())

    tasks = []
    for task in todos:
        tasks.append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        })

    with open("{}.json".format(emp_id), "w") as jsonfile:
        json.dump({str(emp_id): tasks}, jsonfile)
