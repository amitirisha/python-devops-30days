# Day 9 â€“ OS Module

## í¾¯ Objectives
- Interact with the operating system
- Manage files & directories

## í³š Theory
The `os` module provides functions to interact with the OS:
- Get current directory â†’ `os.getcwd()`
- List files â†’ `os.listdir()`
- Create directory â†’ `os.mkdir()`

## í¶¥ Example Code
```python
import os

print("Current Directory:", os.getcwd())
print("Files:", os.listdir())

os.mkdir("test_folder")
print("Created folder: test_folder")
í´¹ DevOps Use Case
Automate log file management and directory creation.
