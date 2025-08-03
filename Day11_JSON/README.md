# Day 11 â€“ JSON Handling

## í¾¯ Objectives
- Read and write JSON files
- Convert Python objects to JSON

## í³š Theory
`json` module:
- `json.dump()` â†’ Write JSON to file
- `json.load()` â†’ Read JSON from file
- `json.dumps()` â†’ Convert object to JSON string

## í¶¥ Example Code
```python
import json

data = {"Server": "Server1", "IP": "192.168.1.10"}
with open("server.json", "w") as f:
    json.dump(data, f)

with open("server.json", "r") as f:
    print(json.load(f))
í´¹ DevOps Use Case
Store cloud resource metadata in JSON files.
