#!/usr/bin/python3
"""
Gather the data from the request then after that
return the emp name and number of task.
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
        user = json.load(res)

    with urllib.request.urlopen(
        "{}/todos?userId={}".format(api, emp_id)
    ) as res:
        todos = json.load(res)

    completed = [t for t in todos if t.get("completed")]

    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)
    ))

    for t in completed:
        print("\t {}".format(t.get("title")))
