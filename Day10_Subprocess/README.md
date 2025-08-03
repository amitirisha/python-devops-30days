# Day 10 â€“ Subprocess Module

## í¾¯ Objectives
- Run system commands from Python

## í³š Theory
The `subprocess` module allows executing shell commands from Python scripts.

## í¶¥ Example Code
```python
import subprocess

result = subprocess.run(["ls", "-l"], capture_output=True, text=True)
print(result.stdout)
í´¹ DevOps Use Case
Run server commands like df -h or systemctl status from automation scripts.


