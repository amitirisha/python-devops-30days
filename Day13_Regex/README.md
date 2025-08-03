# Day 13 â€“ Regex

## í¾¯ Objectives
- Match patterns in text
- Use `re` module

## í³š Theory
Regex (Regular Expressions) are used to search and validate text.

## í¶¥ Example Code
```python
import re

log = "Error: Server down at 10:45"
if re.search(r"Error", log):
    print("Error found in log")
í´¹ DevOps Use Case
Search logs for error keywords.
