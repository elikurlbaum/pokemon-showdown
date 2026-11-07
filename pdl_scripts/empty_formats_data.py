import re

file_path = "data/formats-data.ts"

with open(file_path, "r") as file:
    content = file.read()

content = re.sub(
    r'(\w+):\s*\{[^{}]*\}',
    r'\1: {}',
    content
)

with open(file_path, "w") as file:
    file.write(content)