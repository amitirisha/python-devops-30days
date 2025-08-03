```python
def check_disk():
    import shutil
    usage = shutil.disk_usage("/")
    percent = (usage.used / usage.total) * 100
    return percent

print(f"Disk Usage: {check_disk():.2f}%")
