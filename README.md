# Day 8 â€“ File Handling

## í¾¯ Objectives
- Read and write files
- Use `with open()` for safe file handling

## í³š Theory
File handling in Python allows reading from and writing to files.  
Modes:
- `r` â†’ Read
- `w` â†’ Write (overwrite)
- `a` â†’ Append
- `rb` / `wb` â†’ Binary read/write

## í¶¥ Example Code
```python
# Writing to a file
with open("server_list.txt", "w") as f:
    f.write("Server1\nServer2\n")

# Reading from a file
with open("server_list.txt", "r") as f:
    for line in f:
        print(line.strip())
í´¹ DevOps Use Case
Store and retrieve server inventory from files for automation tasks.
