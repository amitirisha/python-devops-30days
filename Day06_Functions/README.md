# Day 6 â€“ Functions

## í¾¯ Objectives
- Create reusable code blocks
- Pass arguments to functions

## í³š Theory
Functions help organize and reuse code.

### Syntax
```python
def function_name(parameters):
    # action
    return value
í¶¥ Example Code
python
Copy
Edit
def check_disk():
    import shutil
    usage = shutil.disk_usage("/")
    percent = (usage.used / usage.total) * 100
    return percent

print(f"Disk Usage: {check_disk():.2f}%")
í´¹ DevOps Use Case
Check server resource usage before deployments.
