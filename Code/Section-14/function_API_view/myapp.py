import requests
import json

URL = "http://127.0.0.1:8000/studentapi/"

def get_data(id = None):
    data = {}
    if id is not None:
        data = {'id':id}
    headers = {'content-Type': 'application/json'}
    json_data = json.dumps(data)
    res = requests.get(url=URL, headers=headers, data = json_data)
    data = res.json()
    print(data)
get_data()

def post_data():
    data = {
        "name": "Francios",
        "roll": 115,
        "city": "Saint Denis"
    }
    headers = {'content-Type': 'application/json'}
    json_data = json.dumps(data)
    res = requests.post(url=URL, headers=headers, data=json_data)
    data = res.json()
    print(data)

# post_data()


def update_data():
    data = {
        "id": 8,
        "name": "Arthur",
        "roll": 188,
        "city": "Hawaii"
    }
    headers = {'content-Type': 'application/json'}

    json_data = json.dumps(data)
    res = requests.put(url=URL, headers=headers, data=json_data)
    data = res.json()
    print(data)

# update_data()


def delete_data():
    data = {
        'id': 6
    }
    json_data = json.dumps(data)
    res = requests.delete(url=URL, data = json_data)
    data = res.json()
    print(data)

# delete_data()