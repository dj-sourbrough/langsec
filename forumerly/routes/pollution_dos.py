import requests as r
import json
from rich import print, inspect

if __name__ == "__main__":

    with open('pollution_create_user.json', 'rb') as f1:
        res = r.post(
            "http://localhost:3000/upload/users",
            files = {'upload-users': f1}
        )
    with open('pollution_dos.json', 'rb') as f2:

        res = r.post(
            "http://localhost:3000/upload/users",
            files = {'upload-users': f2}
        )
