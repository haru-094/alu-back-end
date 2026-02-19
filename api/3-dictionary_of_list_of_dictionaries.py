#!/usr/bin/python3
"""Exports all employees' TODO data to JSON format."""

import json
import requests

users = requests.get(
    "https://jsonplaceholder.typicode.com/users"
).json()
todos = requests.get(
    "https://jsonplaceholder.typicode.com/todos"
).json()

user_map = {}
for user in users:
    user_map[user.get("id")] = user.get("username")

result = {}
for task in todos:
    uid = task.get("userId")
    str_uid = str(uid)
    if str_uid not in result:
        result[str_uid] = []
    result[str_uid].append({
        "username": user_map.get(uid),
        "task": task.get("title"),
        "completed": task.get("completed")
    })

with open("todo_all_employees.json", "w") as jsonfile:
    json.dump(result, jsonfile)
