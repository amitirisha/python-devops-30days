# Day 10 – Subprocess Module

## � Objectives
- Run system commands from Python

## � Theory
The `subprocess` module allows executing shell commands from Python scripts.

## � Example Code
```python
import subprocess

result = subprocess.run(["ls", "-l"], capture_output=True, text=True)
print(result.stdout)
� DevOps Use Case
Run server commands like df -h or systemctl status from automation scripts.


