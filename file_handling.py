
```python   `
with open("server_list.txt", "w") as f:
    f.write("Server1\nServer2\n")

with open("server_list.txt", "r") as f:
    for line in f:
        print(line.strip())
