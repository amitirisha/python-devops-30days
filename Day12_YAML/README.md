# Day 12 – YAML Handling

## � Objectives
- Read and write YAML files

## � Theory
`PyYAML` is used for YAML in Python:
- Install → `pip install pyyaml`
- `yaml.dump()` → Write YAML
- `yaml.safe_load()` → Read YAML

## � Example Code
```python
import yaml

data = {"Server": "Server1", "IP": "192.168.1.10"}
with open("server.yaml", "w") as f:
    yaml.dump(data, f)

with open("server.yaml", "r") as f:
    print(yaml.safe_load(f))
� DevOps Use Case
Manage Kubernetes manifests or Ansible inventories.
