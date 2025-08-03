# Day 1 – Python Setup & Basics

## ��� Objectives
- Install Python
- Run first script
- Understand comments & indentation

## ��� Theory
Python is widely used in DevOps to write automation scripts, interact with APIs, and manage infrastructure.

### **Installation**
**Windows**:  
1. Download from [python.org](https://www.python.org/downloads/)  
2. Check `Add to PATH` during installation.

**Linux**:  
```bash
sudo apt update
sudo apt install python3 -y
Verify Installation
bash
Copy
Edit
python3 --version
Key Points
Python uses indentation instead of {}.

# for single-line comments.

""" for multi-line comments.

🖥 Example Code
python
Copy
Edit
# hello.py
# My first Python script
print("Hello, DevOps World!")
🔹 DevOps Use Case
Check Python installation before running automation scripts.

bash
Copy
Edit

**💻 `Day01_PythonSetup/hello.py`**
```python
# My first Python script
print("Hello, DevOps World!")