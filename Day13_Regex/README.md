# Day 13 – Regex

## � Objectives
- Match patterns in text
- Use `re` module

## � Theory
Regex (Regular Expressions) are used to search and validate text.

## � Example Code
```python
import re

log = "Error: Server down at 10:45"
if re.search(r"Error", log):
    print("Error found in log")
� DevOps Use Case
Search logs for error keywords.
