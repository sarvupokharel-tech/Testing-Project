# file_io.py
# Basic file read/write example.

filename = "sample.txt"

# Write to file
with open(filename, "w", encoding="utf-8") as f:
    f.write("This is a sample file.\nLine 2.\n")

print(f"Wrote to {filename}")

# Read from file
with open(filename, "r", encoding="utf-8") as f:
    content = f.read()

print("File content:")
print(content)
