# Day 9 – OS Module

## � Objectives
- Interact with the operating system
- Manage files & directories

## � Theory
The `os` module provides functions to interact with the OS:
- Get current directory → `os.getcwd()`
- List files → `os.listdir()`
- Create directory → `os.mkdir()`

## � Example Code
```python
import os

print("Current Directory:", os.getcwd())
print("Files:", os.listdir())

os.mkdir("test_folder")
print("Created folder: test_folder")
� DevOps Use Case
Automate log file management and directory creation.
