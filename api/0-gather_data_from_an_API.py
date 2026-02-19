#!/usr/bin/python3
import requests
import sys

emp_id = int(sys.argv[1])

user_url = (
    "https://jsonplaceholder.typicode.com/users/{}".format(emp_id)
)
user = requests.get(user_url).json()
emp_name = user.get("name")

todos_url = (
    "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        emp_id
    )
)
todos = requests.get(todos_url).json()

done_task = [t for t in todos if t.get("completed")]
total_task = len(todos)

print(
    "Employee {} is done with tasks({}/{}):".format(
        emp_name, len(done_task), total_task
    )
)

for task in done_task:
    print("\t {}".format(task.get("title")))
