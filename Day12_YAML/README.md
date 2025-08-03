# Day 12 â€“ YAML Handling

## í¾¯ Objectives
- Read and write YAML files

## í³š Theory
`PyYAML` is used for YAML in Python:
- Install â†’ `pip install pyyaml`
- `yaml.dump()` â†’ Write YAML
- `yaml.safe_load()` â†’ Read YAML

## í¶¥ Example Code
```python
import yaml

data = {"Server": "Server1", "IP": "192.168.1.10"}
with open("server.yaml", "w") as f:
    yaml.dump(data, f)

with open("server.yaml", "r") as f:
    print(yaml.safe_load(f))
í´¹ DevOps Use Case
Manage Kubernetes manifests or Ansible inventories.
