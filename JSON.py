import json

data = {"name": "Ramesh", "age": 30}

json_str = json.dumps(data)  # Convert dict to JSON string
print(json_str)

parsed_data = json.loads(json_str)  # Convert JSON string back to dict
print(parsed_data["name"])
