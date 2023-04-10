#!/usr/bin/python3
"""Gather data from an API"""
import requests
from sys import argv


def main():
    """Gather data from an API"""
    user_id = argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(user_id)).json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                         .format(user_id)).json()
    done = [task for task in todos if task.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):"
          .format(user.get("name"), len(done), len(todos)))
    for task in done:
        print("\t {}".format(task.get("title")))


if __name__ == "__main__":
    main()
