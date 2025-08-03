# Day 7 – Data Structures

## � Objectives
- Understand lists, tuples, dictionaries
- Iterate over dictionaries

## � Theory
Data structures store collections of data.

- **List** → Ordered, mutable
- **Tuple** → Ordered, immutable
- **Dictionary** → Key-value pairs

## � Example Code
```python
servers = {"Server1": "192.168.1.1", "Server2": "192.168.1.2"}
for name, ip in servers.items():
    print(f"{name} - {ip}")
� DevOps Use Case
Store and iterate over server inventory.
