#!/usr/bin/python3
"""
get all the data from file that gather the data then
export in format of csv.
"""
import csv
import requests
import sys


if __name__ == "__main__":
    emp_id = int(sys.argv[1])

    user_url = (
        "https://jsonplaceholder.typicode.com/users/{}".format(emp_id)
    )
    user = requests.get(user_url).json()
    username = user.get("username")

    todos_url = (
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(
            emp_id
        )
    )
    todos = requests.get(todos_url).json()

    with open("{}.csv".format(emp_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                emp_id,
                username,
                str(task.get("completed")),
                task.get("title")
            ])
