#!/usr/bin/python3
"""
Gather the data from the request then after that
return the emp name and number of task.
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
    emp_name = user.get("name")

    todos_url = (
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(
            emp_id
        )
    )
    with urllib.request.urlopen(todos_url) as response:
        todos = json.loads(response.read().decode())

    done_task = [t for t in todos if t.get("completed")]
    total_task = len(todos)

    print(
        "Employee {} is done with tasks({}/{}):".format(
            emp_name, len(done_task), total_task
        )
    )

    for task in done_task:
        print("\t {}".format(task.get("title")))
