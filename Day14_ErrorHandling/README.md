# Day 14 â€“ Error Handling

## í¾¯ Objectives
- Use try-except blocks
- Handle specific exceptions

## í³š Theory
Error handling prevents scripts from crashing.

## í¶¥ Example Code
```python
try:
    with open("file.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found!")
í´¹ DevOps Use Case
Prevent automation scripts from failing when files or connections are missing.
