# Day 14 – Error Handling

## � Objectives
- Use try-except blocks
- Handle specific exceptions

## � Theory
Error handling prevents scripts from crashing.

## � Example Code
```python
try:
    with open("file.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found!")
� DevOps Use Case
Prevent automation scripts from failing when files or connections are missing.
