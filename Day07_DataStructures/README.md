# Day 7 â€“ Data Structures

## í¾¯ Objectives
- Understand lists, tuples, dictionaries
- Iterate over dictionaries

## í³š Theory
Data structures store collections of data.

- **List** â†’ Ordered, mutable
- **Tuple** â†’ Ordered, immutable
- **Dictionary** â†’ Key-value pairs

## í¶¥ Example Code
```python
servers = {"Server1": "192.168.1.1", "Server2": "192.168.1.2"}
for name, ip in servers.items():
    print(f"{name} - {ip}")
í´¹ DevOps Use Case
Store and iterate over server inventory.
