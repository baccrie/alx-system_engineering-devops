#!/usr/bin/python3
"""
Playing with a SOAP api sounds exquisite
"""

import json
import requests
from sys import argv


if __name__ == '__main__':
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

    for key in all_tasks_for_userid:
        key['task'] = key['title']
        key['username'] = users['username']
        del key['title']
        del key['id']
        del key['userId']
    res = {user_id: all_tasks_for_userid}
    filename = ('{}.json'.format(user_id))
    with open(filename, 'w') as json_file:
        json.dump(res, json_file)
