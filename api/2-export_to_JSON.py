#!/usr/bin/python3
"""Export to JSON"""
import json
import requests
from sys import argv


def main():
    """Export to JSON"""
    user_id = argv[1]
    user = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{user_id}"
    ).json()
    todos = requests.get(
        f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
    ).json()
    with open(f"{user_id}.json", "w") as file:
        json.dump({user_id: [{
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": user.get("username")
        } for task in todos]}, file)


if __name__ == "__main__":
    main()
