# External App: just to check the deserializer API -> This is not the part of django project.
import requests
import json
URL = "http://127.0.0.1:8000/add/"

data = {
    "name": "Henry",
    "roll": 121,
    "city": "New Jersey"
}

json_data = json.dumps(data)
req = requests.post(url=URL,data=json_data)
data = req.json()
print(data)