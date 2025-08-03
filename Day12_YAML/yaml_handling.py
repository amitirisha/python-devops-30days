import yaml

data = {"Server": "Server1", "IP": "192.168.1.10"}
with open("server.yaml", "w") as f:
    yaml.dump(data, f)

with open("server.yaml", "r") as f:
    print(yaml.safe_load(f))
