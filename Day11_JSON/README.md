# Day 11 – JSON Handling

## � Objectives
- Read and write JSON files
- Convert Python objects to JSON

## � Theory
`json` module:
- `json.dump()` → Write JSON to file
- `json.load()` → Read JSON from file
- `json.dumps()` → Convert object to JSON string

## � Example Code
```python
import json

data = {"Server": "Server1", "IP": "192.168.1.10"}
with open("server.json", "w") as f:
    json.dump(data, f)

with open("server.json", "r") as f:
    print(json.load(f))
� DevOps Use Case
Store cloud resource metadata in JSON files.
