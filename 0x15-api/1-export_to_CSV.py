#!/usr/bin/python3
"""
Playing with a SOAP api sounds exquisite
"""


import requests
from sys import argv
import csv


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
    username = users["username"]
    filename = ('{}.csv'.format(user_id))
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC)
        for key in all_tasks_for_userid:
            writer.writerow([(user_id),users["username"],(key["completed"]),key['title']])

