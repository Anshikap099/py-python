print("import os
from pathlib import Path

# Directory to list
directory = "."  # Current directory

print("=== Using os.listdir() ===")
for item in os.listdir(directory):
    print(item)

print("\n=== Using os.scandir() ===")
with os.scandir(directory) as entries:
    for entry in entries:
        print(entry.name)

print("\n=== Using pathlib.Path.iterdir() ===")
path = Path(directory)
for item in path.iterdir():
    print(item.name)")