# Day 2 â€“ Variables & Data Types

## í¾¯ Objectives
- Store data in variables
- Learn data types: int, float, str, bool
- Use f-strings for formatting

## í³š Theory
A variable is used to store values.  
Common types in DevOps:
- Server names â†’ string
- IP addresses â†’ string
- Resource usage â†’ int/float
- Status flags â†’ boolean

### **Syntax**
```python
name = "Server1"
ip = "192.168.1.10"
is_active = True
í¶¥ Example Code
python
Copy
Edit
name = "Server1"
ip = "192.168.1.10"
print(f"Connecting to {name} at {ip}")
í´¹ DevOps Use Case
Store configuration details in variables before automation tasks.

python
Copy
Edit

**í²» `Day02_Variables/variables.py`**
```python
name = "Server1"
ip = "192.168.1.10"
print(f"Connecting to {name} at {ip}")
