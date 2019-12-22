import os

types=set()

for file in os.listdir():
    types.add(file[:file.index(".")])

print(types)