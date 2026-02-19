#!/usr/bin/python3
"""
get all the data from file that gather the data then
export in format of csv.
"""
import csv
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

    with open("{}.csv".format(emp_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                emp_id,
                username,
                str(task.get("completed")),
                task.get("title")
            ])
