#!/usr/bin/python3
"""
get all the data from file that gather the data then
export in format of json.
"""
import json
import sys
import urllib.request


if __name__ == "__main__":
    emp_id = sys.argv[1]
    api = "https://jsonplaceholder.typicode.com"

    with urllib.request.urlopen(
        "{}/users/{}".format(api, emp_id)
    ) as res:
        username = json.load(res).get("username")

    with urllib.request.urlopen(
        "{}/todos?userId={}".format(api, emp_id)
    ) as res:
        todos = json.load(res)

    tasks = []
    for t in todos:
        tasks.append({
            "task": t.get("title"),
            "completed": t.get("completed"),
            "username": username
        })

    with open("{}.json".format(emp_id), "w") as f:
        json.dump({emp_id: tasks}, f)
