#!/usr/bin/python3
"""Dictionary of list of dictionaries"""
import json
import requests
from sys import argv


def main():
    """Dictionary of list of dictionaries"""
    users = requests.get("https://jsonplaceholder.typicode.com/users").json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos").json()
    with open("todo_all_employees.json", "w") as file:
        json.dump({user.get("id"): [{
            "username": user.get("username"),
            "task": task.get("title"),
            "completed": task.get("completed")
        } for task in todos if task.get("userId") == user.get("id")]
            for user in users}, file)


if __name__ == "__main__":
    main()
