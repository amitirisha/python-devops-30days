# Day 6 – Functions

## � Objectives
- Create reusable code blocks
- Pass arguments to functions

## � Theory
Functions help organize and reuse code.

### Syntax
```python
def function_name(parameters):
    # action
    return value
� Example Code
python
Copy
Edit
def check_disk():
    import shutil
    usage = shutil.disk_usage("/")
    percent = (usage.used / usage.total) * 100
    return percent

print(f"Disk Usage: {check_disk():.2f}%")
� DevOps Use Case
Check server resource usage before deployments.
