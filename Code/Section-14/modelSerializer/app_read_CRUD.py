import requests
import json

URL = "http://127.0.0.1:8000/studentapi/"

def get_data(id = None):
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    res = requests.get(url=URL, data = json_data)
    data = res.json()
    print(data)
# get_data()

def post_data():
    data = {
        "name": "Fig",
        "roll": 140,
        "city": "Dakota"
    }

    json_data = json.dumps(data)
    res = requests.post(url=URL,data=json_data)
    data = res.json()
    print(data)

post_data()


def update_data():
    data = {
        "id": 4,
        "name": "Ken",
        "roll": 133,
        "city": "Kyoto"
    }

    json_data = json.dumps(data)
    res = requests.put(url=URL,data=json_data)
    data = res.json()
    print(data)

# update_data()


def delete_data():
    data = {
        'id': 1
    }
    json_data = json.dumps(data)
    res = requests.delete(url=URL, data = json_data)
    data = res.json()
    print(data)

# delete_data()