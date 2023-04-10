#!/usr/bin/python3
"""Export to CSV"""
import csv
import requests
from sys import argv


def main():
    """Export to CSV"""
    user_id = argv[1]
    user = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{user_id}"
    ).json()
    todos = requests.get(
        f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
    ).json()
    with open(f"{user_id}.csv", "w") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow(
                [
                    user_id,
                    user.get("username"),
                    task.get("completed"),
                    task.get("title")
                ]
            )


if __name__ == "__main__":
    main()
