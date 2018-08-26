import json

d = dict(name="Bob", age=23, gender="Male")
json.dumps(d)
with open('dump.txt', 'w') as f:
    json.dump(d, f)
