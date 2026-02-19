#!/usr/bin/python3
"""
get all the data from file that gather the data then
export in format of dict
"""
import json
import urllib.request


if __name__ == "__main__":
    api = "https://jsonplaceholder.typicode.com"

    with urllib.request.urlopen("{}/users".format(api)) as res:
        users = json.load(res)

    with urllib.request.urlopen("{}/todos".format(api)) as res:
        todos = json.load(res)

    usernames = {}
    for u in users:
        usernames[u.get("id")] = u.get("username")

    result = {}
    for t in todos:
        uid = str(t.get("userId"))
        if uid not in result:
            result[uid] = []
        result[uid].append({
            "username": usernames.get(t.get("userId")),
            "task": t.get("title"),
            "completed": t.get("completed")
        })

    with open("todo_all_employees.json", "w") as f:
        json.dump(result, f)
