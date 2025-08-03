# Day 5 – Loops

## � Objectives
- Learn for loop & while loop
- Iterate over lists

## � Theory
Loops allow scripts to repeat actions multiple times.

### Syntax
```python
for item in list:
    # action

while condition:
    # action
� Example Code
python
Copy
Edit
servers = ["192.168.1.1", "192.168.1.2"]
for s in servers:
    print(f"Pinging {s}")
� DevOps Use Case
Loop through server list to run health checks.


