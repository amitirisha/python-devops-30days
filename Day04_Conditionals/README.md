# Day 4 – Conditional Statements

## � Objectives
- Understand if-else conditions
- Use multiple conditions

## � Theory
Conditional statements allow scripts to make decisions.

### Syntax
```python
if condition:
    # action
elif another_condition:
    # action
else:
    # action
� Example Code
python
Copy
Edit
service_status = "running"
if service_status == "running":
    print("Service is active")
else:
    print("Service is down")
� DevOps Use Case
Checking service status before deployment.
