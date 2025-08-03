# Day 4 â€“ Conditional Statements

## í¾¯ Objectives
- Understand if-else conditions
- Use multiple conditions

## í³š Theory
Conditional statements allow scripts to make decisions.

### Syntax
```python
if condition:
    # action
elif another_condition:
    # action
else:
    # action
í¶¥ Example Code
python
Copy
Edit
service_status = "running"
if service_status == "running":
    print("Service is active")
else:
    print("Service is down")
í´¹ DevOps Use Case
Checking service status before deployment.
