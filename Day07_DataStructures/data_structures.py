```python
servers = {"Server1": "192.168.1.1", "Server2": "192.168.1.2"}
for name, ip in servers.items():
    print(f"{name} - {ip}")
