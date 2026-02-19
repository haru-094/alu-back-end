#!/usr/bin/python3
"""Exports employee TODO data to JSON format."""

import json
import requests
import sys

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

tasks = []
for task in todos:
    tasks.append({
        "task": task.get("title"),
        "completed": task.get("completed"),
        "username": username
    })

with open("{}.json".format(emp_id), "w") as jsonfile:
    json.dump({str(emp_id): tasks}, jsonfile)
