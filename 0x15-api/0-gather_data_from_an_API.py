#!/usr/bin/python3

import requests
from sys import argv

user_id = int(argv[1])
users = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                     .format(user_id)).json()
all_tasks = requests.get(
        'https://jsonplaceholder.typicode.com/todos').json()
all_tasks_for_userid = [key for key in all_tasks
                        if key["userId"] == user_id]
task_completed = [key for key in all_tasks_for_userid
                  if key["completed"] is True]

user = users["name"]
all_tasks = len(all_tasks_for_userid)
completed = len(task_completed)

print("Employee {} is done with tasks({}/{}):".
      format(user, completed, all_tasks))
for key in task_completed:
    print('\t {}'.format(key['title']))
