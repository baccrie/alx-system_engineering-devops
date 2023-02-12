#!/usr/bin/python3
"""
Playing with a SOAP api sounds exquisite
"""

import json
import requests
from sys import argv


if __name__ == '__main__':
    users = requests.get('https://jsonplaceholder.typicode.com/users').json()
    all_tasks = requests.get(
            'https://jsonplaceholder.typicode.com/todos').json()
    nos = [key['id'] for key in users]
    names = [key['username'] for key in users]
    dic = {}
    for i in nos:
        all_tasks_for_userid = [key for key in all_tasks if key["userId"] == i]

        for keys in all_tasks_for_userid:
            keys['task'] = keys['title']
            keys['username'] = names[i - 1]
            del keys['title']
            del keys['id']
        dic[str(i)] = all_tasks_for_userid
    for i, j in dic.items():
        for k in j:
            del k['userId']

    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(dic, json_file)
