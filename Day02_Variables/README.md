# Day 2 – Variables & Data Types

## � Objectives
- Store data in variables
- Learn data types: int, float, str, bool
- Use f-strings for formatting

## � Theory
A variable is used to store values.  
Common types in DevOps:
- Server names → string
- IP addresses → string
- Resource usage → int/float
- Status flags → boolean

### **Syntax**
```python
name = "Server1"
ip = "192.168.1.10"
is_active = True
� Example Code
python
Copy
Edit
name = "Server1"
ip = "192.168.1.10"
print(f"Connecting to {name} at {ip}")
� DevOps Use Case
Store configuration details in variables before automation tasks.

python
Copy
Edit

**� `Day02_Variables/variables.py`**
```python
name = "Server1"
ip = "192.168.1.10"
print(f"Connecting to {name} at {ip}")
