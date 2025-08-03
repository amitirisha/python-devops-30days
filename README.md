# Day 8 – File Handling

## � Objectives
- Read and write files
- Use `with open()` for safe file handling

## � Theory
File handling in Python allows reading from and writing to files.  
Modes:
- `r` → Read
- `w` → Write (overwrite)
- `a` → Append
- `rb` / `wb` → Binary read/write

## � Example Code
```python
# Writing to a file
with open("server_list.txt", "w") as f:
    f.write("Server1\nServer2\n")

# Reading from a file
with open("server_list.txt", "r") as f:
    for line in f:
        print(line.strip())
� DevOps Use Case
Store and retrieve server inventory from files for automation tasks.
