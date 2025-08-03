```python
import json

data = {"Server": "Server1", "IP": "192.168.1.10"}
with open("server.json", "w") as f:
    json.dump(data, f)

with open("server.json", "r") as f:
    print(json.load(f))
