```python
import re

log = "Error: Server down at 10:45"
if re.search(r"Error", log):
    print("Error found in log")
